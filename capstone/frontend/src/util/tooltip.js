import * as d3 from 'd3'

function tooltip (event, data, type, centered = false) {
  let string = ''
  switch (type) {
    case 'in':
      if (typeof data === 'object') {
        for (const object in data) {
          string += `<span>${object.length ? object + ':' : ''} ${data[object]}</span><br>`
        }
      } else {
        string = data
      }
      d3.select('#common-tooltip')
        .html(`${string}`)
        .style('font-family', 'Roboto')
        .style('left', `${event.pageX - (d3.select('#common-tooltip').node().getBoundingClientRect().width / 2)}px`)
        .style('top', `${event.pageY - d3.select('#common-tooltip').node().getBoundingClientRect().height - 10}px`)
        .style('display', 'inline')
        .style('text-align', `${centered ? 'center' : 'left'}`)
      break
    case 'out':
      d3.select('#common-tooltip').style('display', 'none')
      break
  }
}

export default tooltip
