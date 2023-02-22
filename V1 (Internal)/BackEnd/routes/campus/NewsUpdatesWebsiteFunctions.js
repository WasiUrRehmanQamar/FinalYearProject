const config = require("../../dbConfig");
const sql = require('mssql')
var getNewsUpdatesWebsiteQuery = "select * from NewsUpdatesWebsite"

const getNewsUpdatesWebsite = async () => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          let data = await pool.request().query(getNewsUpdatesWebsiteQuery);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

const postNewsUpdatesWebsite = async (req) => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          const NewsUpdatesWebsiteID = Math.floor(1000 + Math.random() * 9000);
          const NewsUpdatesID = req.body.NewsUpdatesID;
          const WebsiteID = req.body.WebsiteID;
          const DepartmentID = req.body.DepartmentID;
          const SocietyID = req.body.SocietyID;
          let data = await pool.request().query(`Insert into NewsUpdatesWebsite values(${NewsUpdatesWebsiteID},${NewsUpdatesID},${WebsiteID},${DepartmentID},${SocietyID},'23','','','','')`);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

module.exports = { getNewsUpdatesWebsite, postNewsUpdatesWebsite }