const config = require("../../dbConfig");
const sql = require('mssql')
var getDepartmentQuery = "select * from Department"

const getDepartment = async () => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          let data = await pool.request().query(getDepartmentQuery);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

const postDepartment = async (req) => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          const DepartmentID = Math.floor(1000 + Math.random() * 9000);
          const DepartmentName = req.body.DepartmentName;
          const DepartmentShortName = req.body.DepartmentShortName;
          const CampusID = req.body.CampusID;
          const ParentDepartmentID = req.body.ParentDepartmentID;
          let data = await pool.request().query(`Insert into Department values(${DepartmentID},${DepartmentName},${DepartmentShortName},${CampusID},${ParentDepartmentID},'23','','','','')`);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

module.exports = { getDepartment, postDepartment }