const config = require("../../dbConfig");
const sql = require('mssql')
var getWebsiteQuery = "select * from Website"

const getWebsite = async () => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          let data = await pool.request().query(getWebsiteQuery);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

const postWebsite = async (req) => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          const WebsiteID = Math.floor(1000 + Math.random() * 9000);
          const WebsiteName = req.body.WebsiteName;
          const WebsiteShortName = req.body.WebsiteShortName;
          const CampusID = req.body.CampusID;
          const DepartmentID = req.body.DepartmentID;
          const SocietyID = req.body.SocietyID;
          const ResearchGroupID = req.body.ResearchGroupID;
          const ConferenceID = req.body.ConferenceID;
          let data = await pool.request().query(`Insert into Website values(${WebsiteID},${WebsiteName},${WebsiteShortName},${CampusID},${DepartmentID},${SocietyID},${ResearchGroupID},${ConferenceID},'23','','','','')`);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

module.exports = { getWebsite, postWebsite }