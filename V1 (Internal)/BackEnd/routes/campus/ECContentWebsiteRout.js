const config =require("../../dbConfig");
var ECContentWebsite = require("../../models/ECContentWebsite");
const router = require("express").Router();
const sql = require('mssql')
const ab = require("./ECContentWebsiteFunctions")

router.get("/getECContentWebsite",async(req,res)=>{
    ab.getECContentWebsite().then(result=>{
        console.log("The Results are:",result)
        res.json({status:true,result:result})
     })
})

router.post("/addECContentWebsite",async(req,res)=>{
    ab.postECContentWebsite(req).then(result=>{
        console.log("The Results are:",result)
     })
})

module.exports = router