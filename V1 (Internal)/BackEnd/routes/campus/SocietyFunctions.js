const config = require("../../dbConfig");
const sql = require('mssql')
var getSocietyQuery = "select * from Society"

const getSociety = async () => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          let data = await pool.request().query(getSocietyQuery);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

const postSociety = async (req) => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          const SocietyID = Math.floor(1000 + Math.random() * 9000);
          const SocietyName = req.body.SocietyName;
          const SocietyShortName = req.body.SocietyShortName;
          const CampusID = req.body.CampusID;
          const DepartmentID = req.body.DepartmentID;
          let data = await pool.request().query(`Insert into Society values(${SocietyID},${SocietyName},${SocietyShortName},${CampusID},${DepartmentID},'23','','','','')`);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

module.exports = { getSociety, postSociety }