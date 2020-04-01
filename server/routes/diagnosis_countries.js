const express = require('express')
const router = express.Router()

const db = require('../config/database')
const DiagnosisCountry = require("../models/diagnosis_country")

router.get('/', (req, res) => {
	DiagnosisCountry.findAll()
		.then(diagnosis_countries => res.send({diagnosis_countries}))
		.catch(console.log)
})

router.post('/', (req, res) => {
	let {diagnosisId, countryId} = req.body
	if(diagnosisId && countryId) {
		DiagnosisCountry.create({diagnosisId, countryId})
			.then(result => res.send(result.dataValues))
			.catch(console.log)
	}
})

router.delete('/', (req, res) => {
	let {diagnosisId, countryId} = req.body
	DiagnosisCountry.destroy({
		where: {
			diagnosisId: diagnosisId, 
			countryId: countryId
		}
	})
})

module.exports = router