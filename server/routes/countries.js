const express = require('express')
const router = express.Router()

const db = require('../config/database')
const Country = require('../models/country')
const Diagnosis = require('../models/diagnosis')
const DiagnosisCountry = require('../models/diagnosis_country')

router.get('/', (req, res) => 
	Country.findAll()
		.then(countries => res.send({countries}))
		.catch(console.log)
)

router.get('/probability', async (req, res) => {
	let {countryIds} = req.body
	let likelihood = 0
	
	if(!Array.isArray(countryIds)) {
		if(countryIds === undefined){
			countryIds = []
		} else {
			countryIds = [countryIds]
		}
	}

	countryIds = countryIds.map(id => parseInt(id))

	try{
		await Promise.all(countryIds.map(async countryId => {
		
			let diagnosisCountries = await DiagnosisCountry.findAll({where: {countryId}})
			let total = diagnosisCountries.length
			let positive = 0.0
			await Promise.all(diagnosisCountries.map(async dc => {
				let diagnosis = await Diagnosis.findOne({where: {id: dc.diagnosisId}})
				if(diagnosis.result > 50){
					positive += 1
				}
			}))
			if(total == 0) {
				return
			}
			if(positive / parseFloat(total) > likelihood) {
				likelihood = (positive / parseFloat(total))
			}
		}))
		res.send({probability: likelihood})
	} catch(e) {
		console.log(e)
	}
	
})

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