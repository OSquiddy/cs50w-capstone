<template>
  <div class="earnings-chart-container"></div>
</template>

<script>
import axios from 'axios'
import * as d3 from 'd3'
import tooltip from '../util/tooltip'
import { DateTime } from 'luxon'

export default {
  name: 'EarningsLineChart',
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
      const earnings = await axios.get(process.env.VUE_APP_API_URL + '/getEarnings')
      this.data = earnings.data.earningsData
      this.totalEarnings = earnings.data.earnings
    },
    resizeWindow () {
      this.observer = new ResizeObserver(() => {
        if (this.data.length) {
          this.renderChart(this.data)
        }
      })
      this.observer.observe(document.querySelector('.earnings'))
    },
    tooltipFun (event, d, type) {
      let data = {}
      switch (type) {
        case 'in':
          data = {
            Day: DateTime.fromISO(d.date).toFormat('MMM dd, yyyy'),
            Earnings: `$${d.value}`
          }
          break
      }
      tooltip(event, data, type)
    },
    renderChart (data) {
      // set the dimensions and margins of the graph
      d3.select('.earnings-chart-container > *').remove()
      const container = document.querySelector('.earnings-chart-container')
      const margin = { top: 10, right: 30, bottom: 30, left: 50 }
      const width = container.clientWidth - margin.left - margin.right
      const height = container.clientHeight - margin.top - margin.bottom

      // append the svg object to the body of the page
      const svg = d3.select('.earnings-chart-container')
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`)

      // Now I can use this dataset:
      function drawChart(data, vueComponent) {
        // Add X axis --> it is a date format
        const x = d3.scaleTime()
          .domain(d3.extent(data, function(d) { return d3.timeParse('%Y-%m-%d')(d.date) }))
          .range([0, width])

        // Add Y axis
        const y = d3.scaleLinear()
          .domain([0, d3.max(data, function(d) { return d.value })])
          .range([height, 0])

        // Bisect Date function
        const bisectDate = d3.bisector(function(d) {
          return d3.timeParse('%Y-%m-%d')(d.date)
        }).left
        const formatValue = d3.format(',.2f')
        // eslint-disable-next-line no-unused-vars
        const formatCurrency = function(d) {
          return '$' + formatValue(d)
        }

        // Add the area fill
        const area = d3.area()
          .curve(d3.curveCatmullRom)
          .x(function(d) { return x(d3.timeParse('%Y-%m-%d')(d.date)) })
          .y0(height)
          .y1(function(d) { return y(d.value) })

        // eslint-disable-next-line no-unused-vars
        const line = d3.line()
          .curve(d3.curveCatmullRom)
          .x(function(d) { return x(d3.timeParse('%Y-%m-%d')(d.date)) })
          .y(function(d) { return y(d.value) })

        svg.append('linearGradient')
          .attr('id', 'area-gradient')
          .attr('gradientUnits', 'userSpaceOnUse')
          .attr('x1', '0%').attr('y1', '0%')
          .attr('x2', '0%').attr('y2', '100%')
        // x1 = 100% (red will be on right horz) / y1 = 100% (red will be on bottom vert)
        // x2 = 100% (red will be on left horz) / y2 = 100% (red will be on top vert)
        // mixed values will change the angle of the linear gradient. Adjust as needed.
          .selectAll('stop')
          .data([
            { offset: '0%', color: '#E9ECFF' },
            // add additional steps as needed for gradient.
            { offset: '95%', color: '#FFFFFF' }
          ])
          .enter().append('stop')
          .attr('offset', function(d) { return d.offset })
          .attr('stop-color', function(d) { return d.color })

        svg.append('path')
          .datum(data)
          .attr('fill', 'none')
          .attr('stroke-width', 0)
          .attr('d', area)
          .attr('class', 'area')
          .style('fill', 'url(#area-gradient)')

        svg.append('g')
          .attr('transform', `translate(0, ${height})`).call(d3.axisBottom(x).tickFormat(d3.timeFormat('%b %d')))

        svg.append('g')
          .data(data)
          .call(d3.axisLeft(y).ticks(4).tickFormat(function (d) { return `$${d}` }))

        svg.selectAll('.tick text')
          .style('font-size', '0.625rem')

        // Add the line
        svg.append('path')
          .datum(data)
          .attr('fill', 'none')
          .attr('stroke', '#536DFE')
          .attr('stroke-width', 1.5)
          .attr('d', line)

        const focus = svg.append('g')
          .attr('class', 'focus')
          .style('display', 'none')

        focus.append('circle')
          .attr('r', 4.5)
          .attr('fill', 'none')
          .attr('stroke', 'black')

        focus.append('line')
          .attr('class', 'focus-line')
          .attr('stroke', 'black')
          .attr('stroke-dasharray', '4, 4')
          .attr('y1', 4.5)

        // eslint-disable-next-line no-unused-vars
        const rect = focus.append('rect')
          .attr('x', 9)
          .attr('dy', '.35em')
          .attr('fill', '#eee')
          .attr('stroke', 'var(--medium-gray)')

        // eslint-disable-next-line no-unused-vars
        const text = focus.append('text')
          .attr('x', 15)
          .attr('y', 20)

        svg.append('rect')
          .attr('class', 'curtain')
          .style('fill', 'white')
          .style('float', 'right')
          .attr('width', width + 6)
          .attr('height', height + 5)
          .attr('transform', 'rotate(180)')
          .attr('x', -1 * (width + 6))
          .attr('y', -1 * (height))

        svg.select('.curtain')
          .transition()
          .duration(3000)
          .attr('width', 0)
          .delay((d, i) => { return i * 100 })

        svg.append('rect')
          .attr('class', 'overlay')
          .style('fill', 'none')
          .style('pointer-events', 'all')
          .attr('width', width)
          .attr('height', height)
          // .on('mouseover', function() {
          //   focus.style('display', null)
          // })
          // .on('mouseout', function() {
          //   focus.style('display', 'none')
          // })
          .on('mouseover', mousemove)
          .on('mousemove', mousemove)
          .on('mouseout', (event, d) => {
            focus.style('display', 'none')
            vueComponent.tooltipFun(event, d, 'out')
          })
          // .on('mousemove', (event, d) => vueComponent.tooltipFun(event, d, 'in'))

        // eslint-disable-next-line no-unused-vars
        function mousemove(event) {
          const x0 = x.invert(d3.pointer(event)[0])
          const i = bisectDate(data, x0, 1)
          const d0 = data[i - 1]
          const d1 = data[i]
          const d = x0 - d3.timeParse('%Y-%m-%d')(d0.date) > d3.timeParse('%Y-%m-%d')(d1.date) - x0 ? d1 : d0
          vueComponent.tooltipFun(event, d, 'in')
          focus.style('display', null)
          focus.attr('transform', 'translate(' + x(d3.timeParse('%Y-%m-%d')(d.date)) + ',' + y(d.value) + ')')
          focus.select('.focus-line').attr('y2', height - y(d.value))
        }
      }

      drawChart(data, this)
    }
  }
}
</script>

<style lang="scss" scoped>
.earnings-chart-container {
  width: 100%;
  height: 100%;
}
</style>
