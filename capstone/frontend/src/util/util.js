const { Toast } = require('bootstrap')

export function debounce (func, wait, immediate) {
  let timeout, args, context, timestamp, result
  if (wait == null) wait = 100

  function later () {
    const last = Date.now() - timestamp

    if (last < wait && last >= 0) {
      timeout = setTimeout(later, wait - last)
    } else {
      timeout = null
      if (!immediate) {
        result = func.apply(context, args)
        context = args = null
      }
    }
  };

  const debounced = function () {
    context = this
    args = arguments
    timestamp = Date.now()
    const callNow = immediate && !timeout
    if (!timeout) timeout = setTimeout(later, wait)
    if (callNow) {
      result = func.apply(context, args)
      context = args = null
    }

    return result
  }

  debounced.clear = function () {
    if (timeout) {
      clearTimeout(timeout)
      timeout = null
    }
  }

  debounced.flush = function () {
    if (timeout) {
      result = func.apply(context, args)
      context = args = null

      clearTimeout(timeout)
      timeout = null
    }
  }

  return debounced
};

export function Snackbar (body, color) {
  const html = `<div class="toast" role="alert" aria-live="assertive" aria-atomic="true" data-bs-animation="true">
    <div class="toast-header">
      ${body}
      <button type="button" class="close-btn snackbar-close" data-bs-dismiss="toast" aria-label="Close" style="color: ${color}">OK</button>
    </div>
  </div>`

  const toastElement = htmlToElement(html)
  const toastConainerElement = document.querySelector('.toast-container')
  toastConainerElement.appendChild(toastElement)
  const toast = new Toast(toastElement, { delay: 5000, animation: true })
  toast.show()
  // if (isMobile) {
  // toastConainerElement.style.display = 'flex'
  // toastConainerElement.style.flexDirection = 'column-reverse'
  // toastConainerElement.style.position = 'fixed'
  // toastConainerElement.style.top = '0'
  // toastConainerElement.style.height = 'var(--full-height)'

  // toastElement.style.position = 'fixed'
  // toastElement.style.left = `calc(50% - ${toastElement.clientWidth / 2}px)`
  // toastElement.style.margin = '0 auto 8px'
  // }

  toastElement.addEventListener('hidden.bs.toast', () => {
    toastElement.remove()
  })

  function htmlToElement (html) {
    var template = document.createElement('template')
    html = html.trim() // Never return a text node of whitespace as the result
    template.innerHTML = html
    return template.content.firstChild
  }
}
