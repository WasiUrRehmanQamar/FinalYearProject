const express = require("express")
const chalk = require("chalk")
const app = express()
const dotenv = require("dotenv")
const cors = require("cors")
const sql = require('mssql');
const CampusRout = require('./routes/campus/CampusRout')
const DepartmentRout = require('./routes/campus/DepartmentRout')
const ECContentRout = require('./routes/campus/ECContentRout')
const ECContentWebsiteRout = require('./routes/campus/ECContentWebsiteRout')
const EventCategoryRout = require('./routes/campus/EventCategoryRout')
const MasterUserRout = require('./routes/campus/MasterUserRout')
const NewsUpdatesRout = require('./routes/campus/NewsUpdatesRout')
const NewsUpdatesWebsitesRout = require('./routes/campus/NewsUpdatesWebsitesRout')
const SocietyRout = require('./routes/campus/SocietyRout')
const WebsiteRout = require('./routes/campus/WebsiteRout')

dotenv.config()

app.use(cors())

app.use(express.json())

app.use("/api/v1", CampusRout)
app.use("/api/v1", DepartmentRout)
app.use("/api/v1", ECContentRout)
app.use("/api/v1", ECContentWebsiteRout)
app.use("/api/v1", EventCategoryRout)
app.use("/api/v1", MasterUserRout)
app.use("/api/v1", NewsUpdatesRout)
app.use("/api/v1", NewsUpdatesWebsitesRout)
app.use("/api/v1", SocietyRout)
app.use("/api/v1", WebsiteRout)


app.listen(process.env.PORT || 5000, () => {
  console.log(chalk.yellow.inverse("Hurrah! App is Running at" + chalk.green(process.env.PORT) + "Port"))
})
