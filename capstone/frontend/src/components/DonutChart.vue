<template>
  <div class="donutchart-container"></div>
</template>

<script>
import axios from 'axios'
import * as d3 from 'd3'
import tooltip from '../util/tooltip'
import { mapState } from 'vuex'
export default {
  name: 'DonutChart',
  data() {
    return {
      observer: null,
      numPatients: null
    }
  },
  computed: {
    ...mapState(['isMobile', 'isCollapsed']),
    data () {
      if (this.numPatients) {
        const obj = {}
        obj.Male = this.numPatients.male
        obj.Female = this.numPatients.female
        obj.Other = this.numPatients.other
        return obj
      }
      return null
    }
  },
  mounted () {
    this.resizeWindow()
    this.getTotalPatients()
  },
  beforeDestroy () {
    if (this.observer) this.observer.disconnect()
  },
  watch: {
    data(newValue, oldValue) {
      this.resizeWindow()
    }
  },
  methods: {
    resizeWindow () {
      this.observer = new ResizeObserver(() => {
        this.renderChart()
      })
      this.observer.observe(document.querySelector('.donutchart-container'))
    },
    tooltipFun (event, d, type) {
      let data = {}
      switch (type) {
        case 'in':
          data = {
            Gender: d.data[0],
            'No. of Patients': d.value
          }
          break
      }
      tooltip(event, data, type)
    },
    async getTotalPatients () {
      const list = await axios.get(process.env.VUE_APP_API_URL + '/numPatients')
      this.numPatients = list.data.numPatients
    },
    renderChart() {
      // set the dimensions and margins of the graph
      d3.select('.donutchart-container > *').remove()
      const container = document.querySelector('.donutchart-container')
      // const margin = { top: 10, right: 0, bottom: 20, left: 0 }
      const width = container.clientWidth
      const height = container.clientHeight
      const vueComponent = this
      // The radius of the pieplot is half the width or half the height (smallest one). I subtract a bit of margin.
      let radius
      if (this.isMobile) {
        radius = Math.min(width, height) / 3.1
      } else {
        if (this.isCollapsed) {
          radius = Math.min(width, height) / 2.2
        } else {
          radius = Math.min(width, height) / 2.7
        }
      }

      // append the svg object to the div called 'my_dataviz'
      const svg = d3
        .select('.donutchart-container')
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr('transform', `translate(${width / 2},${height / 2})`)

      // Create dummy data
      // const data = { Males: 9, Females: 20 }
      const data = this.data

      // set the color scale
      const color = d3.scaleOrdinal().domain(['Male', 'Female', 'Other']).range(['var(--success)', 'var(--blue)', 'var(--yellow)'])

      // Compute the position of each group on the pie:
      const pie = d3
        .pie()
        .sort(null) // Do not sort group by size
        .value((d) => d[1])
      const dataReady = pie(Object.entries(data))

      // The arc generator
      const arc = d3
        .arc()
        .innerRadius(radius * 0.6) // This is the size of the donut hole
        .outerRadius(radius * 0.8)

      // Another arc that won't be drawn. Just for labels positioning
      const outerArc = d3
        .arc()
        .innerRadius(radius * 0.9)
        .outerRadius(radius * 0.9)

      // Add the polylines between chart and labels:
      svg
        .selectAll('allPolylines')
        .data(dataReady)
        .join('polyline')
        .attr('stroke', '#bbb')
        .style('fill', 'none')
        .attr('stroke-width', 1)
        .attr('points', function (d) {
          const posA = arc.centroid(d) // line insertion in the slice
          const posB = outerArc.centroid(d) // line break: we use the other arc generator that has been built only for that
          const posC = outerArc.centroid(d) // Label position = almost the same as posB
          const midangle = d.startAngle + (d.endAngle - d.startAngle) / 2 // we need the angle to see if the X position will be at the extreme right or extreme left
          posC[0] = radius * 0.95 * (midangle < Math.PI ? 1 : -1) // multiply by 1 or -1 to put it on the right or on the left
          return [posA, posB, posC]
        })

      // Add the polylines between chart and labels:
      svg
        .selectAll('allLabels')
        .data(dataReady)
        .join('text')
        .text((d) => d.data[0])
        .attr('y', radius / 15)
        .attr('transform', function (d) {
          const pos = outerArc.centroid(d)
          const midangle = d.startAngle + (d.endAngle - d.startAngle) / 2
          pos[0] = radius * 0.99 * (midangle < Math.PI ? 1 : -1)
          return `translate(${pos})`
        })
        .style('text-anchor', function (d) {
          const midangle = d.startAngle + (d.endAngle - d.startAngle) / 2
          return midangle < Math.PI ? 'start' : 'end'
        })
        .style('font-size', radius / 7)

      // Build the pie chart: Basically, each part of the pie is a path that we build using the arc function.
      svg
        .selectAll('allSlices')
        .data(dataReady)
        .join('path')
        .attr('d', arc)
        .attr('fill', (d) => color(d.data[1]))
        .attr('stroke', 'white')
        .style('stroke-width', '2px')
        .style('transition', '0.3s ease-out')
        .on('mouseover', function (event, d) {
          d3.select(this).attr('fill', 'var(--error)')
          d3.select(this).attr('transform', 'scale(1.05)')
          vueComponent.tooltipFun(event, d, 'in')
        })
        .on('mousemove', (event, d) => vueComponent.tooltipFun(event, d, 'in'))
        .on('mouseout', function (event, d) {
          if (d.data[0] === 'Male') {
            d3.select(this).attr('fill', 'var(--success)')
          } else if (d.data[0] === 'Female') {
            d3.select(this).attr('fill', 'var(--blue)')
          } else {
            d3.select(this).attr('fill', 'var(--yellow)')
          }
          d3.select(this).attr('transform', 'scale(1)')
          vueComponent.tooltipFun(event, d, 'out')
        })
        // .style('opacity', 0.7)

      const donutText = svg.append('text').attr('text-anchor', 'middle').attr('x', 0)
        .attr('y', radius / 15)

      donutText
        .append('tspan')
        .attr('class', 'numPatients')
        .text(data.Male + data.Female + data.Other)
        .style('font-size', radius / 2.5)

      donutText
        .append('tspan')
        .attr('x', 0)
        .attr('dy', radius / 6)
        .text('Patients')
        .style('font-size', radius / 7)
    }
  }
}
</script>

<style lang="scss" scoped>
.donutchart-container {
  width: 100%;
  height: 100%;
  display: flex;
}
</style>
