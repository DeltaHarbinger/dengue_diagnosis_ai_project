const express = require('express')
const expresshbs = require('express-handlebars')
const bodyParser = require('body-parser')

const db = require('./config/database')

app = express()
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get('/', (req, res) => res.send("Index"))

app.use('/countries', require('./routes/countries'))

app.use('/symptoms', require('./routes/symptoms'))

const PORT = process.env.PORT || 5000

app.listen(PORT, console.log(`App on port ${PORT}`)) 