const config = require("../../dbConfig");
const sql = require('mssql')
var getCampusQuery = "select * from campus"

const getcampus = async () => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          let data = await pool.request().query(getCampusQuery);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

const postCampus = async (req,res) => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          const CampusID = Math.floor(1000 + Math.random() * 9000);
          const CampusName = req.body.campusName;
          const CampusShortName = req.body.campusShortName;
          const CampusAddress = req.body.campusAddress;
          const CampusPhoneNumber = req.body.campusPhoneNumber;
          const CampusEmail = req.body.email;
          console.log("This is Request Bodyy",req.body)
          let data = await pool.request().query(`INSERT INTO campus VALUES('${CampusID}', '${CampusName}', '${CampusShortName}', '${CampusAddress}', '${CampusPhoneNumber}', '${CampusEmail}', '', '', '', '', '')`)
          //Here is Data
          console.log("This is Data",data)
          // await sql.connect(async(config, err) =>{
          //      if (err) {
          //        console.log(err);
          //        return res.status(500).send('Error connecting to database');
          //      }
            
           
          //      // Insert data into the database
          //      const request = new sql.Request();
          //      await request.query(`Insert into Campus values(${CampusID},${CampusName},${CampusShortName},${CampusAddress},${CampusPhoneNumber},${CampusEmail},'','','','','')`, (err, result) => {
          //        if (err) {
          //          console.log(err);
          //          return res.status(500).send('Error inserting data into database');
          //        }
           
          //        res.status(200).send('Data inserted successfully');
          //      });
          //    });
 
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}
// POST API endpoint
// app.post('/api/data', (req, res) => {
//   const { name, age, email } = req.body;

//   // Create a new SQL Server connection
//   sql.connect(config, err => {
//     if (err) {
//       console.log(err);
//       return res.status(500).send('Error connecting to database');
//     }

//     // Insert data into the database
//     const request = new sql.Request();
//     request.query(`INSERT INTO users (name, age, email) VALUES ('${name}', '${age}', '${email}')`, (err, result) => {
//       if (err) {
//         console.log(err);
//         return res.status(500).send('Error inserting data into database');
//       }

//       res.status(200).send('Data inserted successfully');
//     });
//   });
// });



module.exports = { getcampus, postCampus }