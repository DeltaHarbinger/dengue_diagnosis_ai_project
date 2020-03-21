const express = require('express')
const router = express.Router()

const db = require('../config/database')
const Symptom = require('../models/symptom')

router.get('/', (req, res) => {
	Symptom.findAll()
		.then(symptoms => res.send({symptoms}))
		.catch(console.log)
})

router.post('/', (req, res) => {
	let {name} = req.body
	Symptom.create({name})
		.then(result => res.send(result))
		.catch(console.log)
})

router.put('/', (req, res) => {
	let payload = {id: req.body.id, name: req.body.name}
	if(payload.id === undefined) {
		res.send({error: "no ID given"})
		return
	}
	Object.keys(payload).forEach(key => payload[key] === undefined && delete payload[key])
	Symptom.update(payload, {where: {id: payload.id}, returning: true})
		.then(result => res.send(result))
		.catch(console.log)
})

router.delete('/', (req, res) => {
	let {id} = req.body
	if(id === undefined) {
		res.send({error: "no ID given"})
		return
	}
	Symptom.destroy({where: {id: id}})
		.then(result => res.send({deletions: result}))
		.catch(console.log)
})

module.exports = router