document.addEventListener('DOMContentLoaded', (event) => {
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port)

  socket.on('connect', (event) => {
    document.querySelectorAll('button').forEach(button => {
      button.onclick = () => {
        const message = document.querySelector('#message').value
        console.log('message1')
        socket.emit('submit message', { message: message })
      }
    })
  })

  socket.on('transmit message', (data, event) => {
    event.preventDefault()
    const di = document.createElement('li')
    di.innerHTML = `${data.message}`
    console.log('data.message')
    document.querySelector('#messages').append(di)
  })
})
