const Sequelize = require('sequelize')
const db = require('../config/database')

const Symptom = db.define('symptom', {
	id: {
		type: Sequelize.INTEGER,
		primaryKey: true,
		autoIncrement: true
	},
	name: {
		type: Sequelize.STRING
	}
})

module.exports = Symptom