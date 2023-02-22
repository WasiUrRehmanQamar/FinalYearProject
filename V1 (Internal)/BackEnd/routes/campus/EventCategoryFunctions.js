const config = require("../../dbConfig");
const sql = require('mssql')
var getEventCategoryQuery = "select * from EventCategory"

const getEventCategory = async () => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          let data = await pool.request().query(getEventCategoryQuery);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

const postEventCategory = async (req) => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          const EventCategoryID = Math.floor(1000 + Math.random() * 9000);
          const EventCategoryName = req.body.EventCategoryName;
          let data = await pool.request().query(`Insert into EventCategory values(${EventCategoryID},${EventCategoryName},'23','','','','')`);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

module.exports = { getEventCategory, postEventCategory }