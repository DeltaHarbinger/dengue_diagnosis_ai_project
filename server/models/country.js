const Sequelize = require('sequelize')
const db = require('../config/database')

const Country = db.define('country', {
	country_code: {
		type: Sequelize.STRING
	},
	country_name: {
		type: Sequelize.STRING
	},
	id: {
		type: Sequelize.STRING,
		primaryKey: true,
		autoIncrement: true
	}
})

module.exports = Country