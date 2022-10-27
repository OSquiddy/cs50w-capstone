require('dotenv').config()
const port = process.env.PORT || 8080
const express = require('express')
const serveStatic = require('serve-static')
const history = require('connect-history-api-fallback')
const app = express()

app.use(history())
app.use(serveStatic(__dirname + '/dist'))

app.listen(port, () => { console.log(`Connected. Listening on port ${port}`) })
