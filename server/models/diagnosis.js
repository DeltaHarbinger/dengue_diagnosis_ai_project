const Sequelize = require("sequelize")
const db = require("../config/database")

const Diagnosis = db.define('diagnosis', {
	id: {
		type: Sequelize.INTEGER,
		primaryKey: true,
		autoIncrement: true
	},
	name: {
		type: Sequelize.STRING
	},
	result: {
		type: Sequelize.INTEGER
	},
	temperature: {
		type: Sequelize.REAL
	}
})

module.exports = Diagnosis