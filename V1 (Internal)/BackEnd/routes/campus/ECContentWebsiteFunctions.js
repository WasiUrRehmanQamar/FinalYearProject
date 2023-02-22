const config = require("../../dbConfig");
const sql = require('mssql')
var getECContentWebsiteQuery = "select * from ECContentWebsite"

const getECContentWebsite = async () => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          let data = await pool.request().query(getECContentWebsiteQuery);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

const postECContentWebsite = async (req) => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          const ECContentWebsiteID = Math.floor(1000 + Math.random() * 9000);
          const ECContentID = req.body.ECContentID;
          const WebsiteID = req.body.WebsiteID;
          let data = await pool.request().query(`Insert into ECContentWebsite values(${ECContentWebsiteID},${ECContentID},${WebsiteID},'23','','','','')`);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

module.exports = { getECContentWebsite, postECContentWebsite }