const Sequelize = require("sequelize")
const db = require("../config/database")

const DiagnosisSymptoms = db.define('diagnosis_symptoms', {
	diagnosisId: {
		type: Sequelize.INTEGER
	},
	symptomId: {
		type: Sequelize.INTEGER
	}
})

DiagnosisSymptoms.add