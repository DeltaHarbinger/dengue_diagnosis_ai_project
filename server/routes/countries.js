const express = require('express')
const router = express.Router()

const db = require('../config/database')
const Country = require('../models/country')

router.get('/', (req, res) => 
	Country.findAll()
		.then(countries => res.send({countries}))
		.catch(console.log)
)

router.post('/', (req, res) => {
	let {country_code, country_name} = req.body
	Country.create({country_code, country_name})
		.then(result => res.send(result.dataValues))
		.catch(console.log)
})

router.put('/', (req, res) => {
	let payload = {id: req.body.id, country_code: req.body.country_code, country_name: req.body.country_name}
	if(payload.id === undefined) {
		res.send({error: "no ID given"})
		return
	}
	Object.keys(payload).forEach(key => payload[key] === undefined && delete payload[key])
	Country.update(payload, {where: {id: payload.id}, returning: true})
		.then(result => res.send({updates: result}))
		.catch(console.log)
})

router.delete('/', (req, res) => {
	let {id} = req.body
	if(id === undefined) {
		res.send({error: "no ID given"})
		return
	}
	Country.destroy({
		where: {id: id},
	})
	.then(result => res.send({deletions: result}))
	.catch(console.log)
})

module.exports = router