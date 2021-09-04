<template>
  <div class="barchart-container"></div>
</template>

<script>
import axios from 'axios'
import * as d3 from 'd3'
import tooltip from '../util/tooltip'
import { DateTime } from 'luxon'
export default {
  name: 'BarChart',
  data () {
    return {
      data: null,
      totalEarnings: null,
      observer: null
    }
  },
  watch: {
    data () {
      this.resizeWindow()
    }
  },
  mounted () {
    this.getData()
  },
  beforeDestroy () {
    if (this.observer) this.observer.disconnect()
  },
  methods: {
    async getData () {
      const earnings = await axios.get(process.env.VUE_APP_API_URL + '/getEarnings/m')
      this.data = earnings.data.earningsData
      this.totalEarnings = earnings.data.earnings
    },
    resizeWindow () {
      this.observer = new ResizeObserver(() => {
        if (this.data.length) {
          this.renderChart(this.data)
        }
      })
      this.observer.observe(document.querySelector('.total-earnings'))
    },
    tooltipFun (event, d, type) {
      let data = {}
      switch (type) {
        case 'in':
          data = {
            Month: DateTime.fromISO(d.date).toFormat('MMMM yyyy'),
            Earnings: `$${d.value}`
          }
          break
      }
      tooltip(event, data, type)
    },
    renderChart (data) {
      d3.select('.barchart-container > *').remove()
      const container = document.querySelector('.barchart-container')
      const margin = { top: 10, right: 10, bottom: 20, left: 30 }
      const width = container.clientWidth - margin.left - margin.right
      const height = container.clientHeight - margin.top - margin.bottom

      // append the svg object to the body of the page
      const svg = d3.select('.barchart-container')
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`)

      function drawChart(data, vueComponent) {
        // X axis
        const x = d3.scaleBand()
          .range([0, width])
          .domain(data.map(d => d3.timeFormat('%b %y')(d3.timeParse('%Y-%m-%d')(d.date))))
          .padding(0.2)
        svg.append('g')
          .attr('transform', `translate(0,${height})`)
          .call(d3.axisBottom(x))
          .selectAll('text')
          // .attr('transform', 'translate(-10,0)rotate(-45)')
          .style('text-anchor', 'middle')

        // Add Y axis
        const y = d3.scaleLinear()
          .domain([0, d3.max(data, function (d) { return d.value })])
          .range([height, 0])
        svg.append('g')
          .call(d3.axisLeft(y).ticks(4))

        svg.selectAll('text')
          .style('font-size', '0.5rem')

        // Bars
        svg.selectAll('mybar')
          .data(data)
          .join('rect')
          .attr('x', d => x(d3.timeFormat('%b %y')(d3.timeParse('%Y-%m-%d')(d.date))))
          .attr('width', x.bandwidth())
          .attr('fill', 'steelblue')
          .style('transition', '0.3s ease-out')
        // no bar at the beginning thus:
          .attr('height', d => height - y(0)) // always equal to 0
          .attr('y', d => y(0))
          .on('mouseover', function (event, d) {
            d3.select(this).attr('fill', 'var(--primary-accent-light)')
            vueComponent.tooltipFun(event, d, 'in')
          })
          .on('mousemove', (event, d) => vueComponent.tooltipFun(event, d, 'in'))
          .on('mouseout', function (event, d) {
            d3.select(this).attr('fill', 'steelblue')
            vueComponent.tooltipFun(event, d, 'out')
          })

        // Animation
        svg.selectAll('rect')
          .transition()
          .duration(800)
          .attr('y', d => y(d.value))
          .attr('height', d => height - y(d.value))
          .delay((d, i) => { return i * 100 })
      }

      drawChart(data, this)
    }
  }
}
</script>

<style lang="scss" scoped>
.barchart-container {
  width: 100%;
  height: 80%;
}
</style>
