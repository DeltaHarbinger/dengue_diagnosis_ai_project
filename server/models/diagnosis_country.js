const Sequelize = require("sequelize")
const db = require("../config/database")

const DiagnosisCountry = db.define('diagnosis_country', {
	diagnosisId: {
		type: Sequelize.INTEGER
	},
	countryId: {
		type: Sequelize.INTEGER
	}
})

module.exports = DiagnosisCountry