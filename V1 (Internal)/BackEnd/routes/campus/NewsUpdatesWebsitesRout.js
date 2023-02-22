const config =require("../../dbConfig");
var NewsUpdatesWebsite = require("../../models/NewsUpdatesWebsite");
const router = require("express").Router();
const sql = require('mssql')
const ab = require("./NewsUpdatesWebsiteFunctions")

router.get("/getNewsUpdatesWebsite",async(req,res)=>{
    ab.getNewsUpdatesWebsite().then(result=>{
        console.log("The Results are:",result)
        res.json({status:true,result:result})
     })
})

router.post("/addNewsUpdatesWebsite",async(req,res)=>{
    ab.postNewsUpdatesWebsite(req).then(result=>{
        console.log("The Results are:",result)
     })
})

module.exports = router