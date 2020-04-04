const express = require('express')
const router = express.Router()

const db = require('../config/database')
const Symptom = require('../models/symptom')
const Diagnosis = require('../models/diagnosis')
const DiagnosisSymptom = require('../models/diagnosis_symptom')

router.get('/', (req, res) => {
	Symptom.findAll()
		.then(symptoms => res.send({symptoms}))
		.catch(console.log)
})

router.get('/probability', async (req, res) => {
	let {symptomIds} = req.body
	let totalLikelihood = 0.0
	let currentLikelihood = 0.0
	let symptoms = await Symptom.findAll()

	if(!Array.isArray(symptomIds)) {
		if(symptomIds === undefined){
			symptomIds = []
		} else {
			symptomIds = [symptomIds]
		}
	}

	symptomIds = symptomIds.map(id => parseInt(id))
	
	await Promise.all(symptoms.map(async symptom => {
		let symptomId = symptom.id
		let diagnosisSymptoms = await DiagnosisSymptom.findAll({where: {symptomId}})
		let total = diagnosisSymptoms.length
		let positive = 0
		await Promise.all(diagnosisSymptoms.map(async ds => {
			let diagnosis = await Diagnosis.findOne({where: {id: ds.diagnosisId}})
			if(diagnosis.result > 50) {
				positive += 1
			}
		}))
		if(total == 0) {
			return
		}
		totalLikelihood += positive / parseFloat(total)
		if(symptomIds.includes(symptomId)){
			currentLikelihood += positive / parseFloat(total)
		}
	}))

	if(totalLikelihood == 0){
		res.send({probability: 0})
	} else {
		res.send({probability: currentLikelihood / parseFloat(totalLikelihood)})
	}
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
		.then(result => res.send({updates: result}))
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