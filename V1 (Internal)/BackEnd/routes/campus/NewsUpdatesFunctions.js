const config = require("../../dbConfig");
const sql = require('mssql')
var getNewsUpdatesQuery = "select * from NewsUpdates"

const getNewsUpdates = async () => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          let data = await pool.request().query(getNewsUpdatesQuery);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

const postNewsUpdates = async (req) => {
     try {
          let pool = await sql.connect(config);
          console.log("The Pool is", pool)
          const NewsUpdatesID = Math.floor(1000 + Math.random() * 9000);
          const Title = req.body.Title;
          const NewsContent = req.body.NewsContent;
          const DueDate = req.body.DueDate;
          const TitleImage = req.body.TitleImage;
          let data = await pool.request().query(`Insert into NewsUpdates values(${NewsUpdatesID},${Title},${NewsContent},'',${DueDate},${TitleImage},'23','','','','')`);
          return data.recordset
     } catch (e) {
          console.log("Here is Error", e)
     }
}

module.exports = { getNewsUpdates, postNewsUpdates }