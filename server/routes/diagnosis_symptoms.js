const express = require('express')
const router = express.Router()

const db = require('../config/database')
const DiagnosisSymptom = require("../models/diagnosis_symptom")

router.get('/', (req, res) => {
	let {diagnosisId, symptomId} = req.query
	if(diagnosisId){
		DiagnosisSymptom.findAll({where: {diagnosisId}})
			.then(diagnosis_symptoms => res.send({diagnosis_symptoms}))
			.catch(console.log)
		return
	} 
	if(symptomId) {
		DiagnosisSymptom.findAll({where: {symptomId}})
			.then(diagnosis_symptoms => res.send({diagnosis_symptoms}))
			.catch(console.log)
		return
	}
	DiagnosisSymptom.findAll()
		.then(diagnosis_symptoms => res.send({diagnosis_symptoms}))
		.catch(console.log)
})

router.post('/', (req, res) => {
	let {diagnosisId, symptomId} = req.body
	if(diagnosisId && symptomId) {
		DiagnosisSymptom.create({diagnosisId, symptomId})
			.then(result => res.send(result.dataValues))
			.catch(console.log)
	}
})

router.delete('/', (req, res) => {
	let {diagnosisId, symptomId} = req.body
	DiagnosisSymptom.destroy({
		where: {
			diagnosisId: diagnosisId, 
			symptomId: symptomId
		}
	})
		.then(result => res.send({deletions:result}))
		.catch(console.log)
})

module.exports = router