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

		Diagnosis.findOne({
			where: {
				id: id
			}
		})
			.then(diagnosis => {
				let data = diagnosis.dataValues
				data.symptoms = symptoms
				data.countries = countries
				res.send({
					diagnosis: data
				})
			})
			.catch(console.log)
	} else {
		Diagnosis.findAll()
			.then(diagnoses => res.send({diagnoses}))
			.catch(console.log)
	}
	
})

router.post('/', async (req, res) => {
	let {name, result, temperature, symptomIds, countryIds} = req.body
	let diagnosisResult = null
	await Diagnosis.create({name, result, temperature})
		.then(result => {
			diagnosisResult = result.dataValues
		})
		.catch(console.log)
	if(diagnosisResult.id !== undefined) {
		if(Array.isArray(symptomIds)) {
			await Promise.all(symptomIds.map(async symptomId => {
				await DiagnosisSymptom.create({diagnosisId: diagnosisResult.id, symptomId})
			}))
		}
		if(Array.isArray(countryIds)) {
			await Promise.all(countryIds.map(async countryId => {
				await DiagnosisCountry.create({diagnosisId: diagnosisResult.id, countryId})
			}))
		}
	}
	res.send(diagnosisResult)
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