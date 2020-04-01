const express = require('express')
const router = express.Router()

const db = require('../config/database')
const DiagnosisSymptom = require("../models/diagnosis_symptom")

router.get('/', (req, res) => {
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
})

module.exports = router