const express = require('express')
const router = express.Router()

const db = require('../config/database')
const DiagnosisCountry = require("../models/diagnosis_country")

router.get('/', (req, res) => {
	let {diagnosisId, countryId} = req.query
	if(diagnosisId) {
		DiagnosisCountry.findAll({where: {diagnosisId}})
			.then(diagnosis_countries => res.send({diagnosis_countries}))
			.catch(console.log)
		return
	}
	if(countryId) {
		DiagnosisCountry.findAll({where: {countryId}})
			.then(diagnosis_countries => res.send({diagnosis_countries}))
			.catch(console.log)
	}
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
		.then(result => res.send({deletions:result}))
		.catch(console.log)
})

module.exports = router