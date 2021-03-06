const Sequelize = require("sequelize")
const db = require("../config/database")

const DiagnosisSymptom = db.define('diagnosis_symptom', {
	diagnosisId: {
		type: Sequelize.INTEGER
	},
	symptomId: {
		type: Sequelize.INTEGER
	}
})

module.exports = DiagnosisSymptom