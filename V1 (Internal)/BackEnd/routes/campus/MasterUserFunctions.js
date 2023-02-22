const config = require("../../dbConfig");
const sql = require('mssql')
var getMasterUserQuery = "select * from MasterUser"

const getMasterUser = async () => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          let data = await pool.request().query(getMasterUserQuery);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

const postMasterUser = async (req) => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          const MasterUserID = Math.floor(1000 + Math.random() * 9000);
          const FullName = req.body.FullName;
          const Email = req.body.Email;
          const Password = req.body.Password;
          let data = await pool.request().query(`Insert into MasterUser values(${MasterUserID},${FullName},${Email},${Password},'23','','','','')`);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

module.exports = { getMasterUser, postMasterUser }