const express = require('express')
const router = express.Router()

const db = require('../config/database')
const Diagnosis = require('../models/diagnosis')
const DiagnosisSymptom = require('../models/diagnosis_symptom')
const DiagnosisCountry = require('../models/diagnosis_country')

router.get('/', async (req, res) => {
	let {id} = req.query
	
	if(id){
		let symptoms = await DiagnosisSymptom.findAll({where: {diagnosisId: id}})
		let countries = await DiagnosisCountry.findAll({where: {diagnosisId: id}})

		Diagnosis.findAll({
			where: {
				id: id
			}
		})
			.then(diagnoses => res.send({
				...diagnoses,
				symptoms,
				countries
			}))
			.catch(console.log)
	} else {
		Diagnosis.findAll()
			.then(diagnoses => res.send({diagnoses}))
			.catch(console.log)
	}
	
})

router.post('/', (req, res) => {
	let {name, result, temperature} = req.body
	Diagnosis.create({name, result, temperature})
		.then(result => res.send(result.dataValues))
		.catch(console.log)
})

router.put('/', (req, res) => {
	let payload = {id: req.body.id, name: req.body.name, result: req.body.result, temperature: req.body.temperature}
	if(payload.id === undefined) {
		res.send({error: "no ID given"})
		return
	}
	Object.keys(payload).forEach(key => payload[key] === undefined && delete payload[key])
	Diagnosis.update(payload, {where: {id: payload.id}, returning: true})
		.then(result => res.send({updates: result}))
		.catch(console.log)
})

router.delete('/', (req, res) => {
	let {id} = req.body
	Diagnosis.destroy({where: {id: id}})
		.then(result => res.send({deletions:result}))
		.catch(console.log)
})

module.exports = router