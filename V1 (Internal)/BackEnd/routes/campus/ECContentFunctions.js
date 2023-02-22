const config = require("../../dbConfig");
const sql = require('mssql')
var getECContentQuery = "select * from ECContent"

const getECContent = async () => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          let data = await pool.request().query(getECContentQuery);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

const postECContent = async (req) => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          const ECContentID = Math.floor(1000 + Math.random() * 9000);
          const Title = req.body.Title;
          const DueDate = req.body.DueDate;
          const Category = req.body.Category;
          const EventContent = req.body.EventContent;
          const EventCategoryID = Math.floor(1000 + Math.random() * 9000)
          let data = await pool.request().query(`Insert into ECContent values(${ECContentID},${Title},'',${DueDate},${Category},${EventContent},${EventCategoryID},'23','','','','')`);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

module.exports = { getECContent, postECContent }