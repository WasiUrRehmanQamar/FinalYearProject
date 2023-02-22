const config =require("../../dbConfig");
var Website = require("../../models/Website");
const router = require("express").Router();
const sql = require('mssql')
const ab = require("./WebsiteFunctions")

router.get("/getWebsite",async(req,res)=>{
    ab.getWebsite().then(result=>{
        console.log("The Results are:",result)
        res.json({status:true,result:result})
     })
})

router.post("/addWebsite",async(req,res)=>{
    ab.postWebsite(req).then(result=>{
        console.log("The Results are:",result)
     })
})

module.exports = router