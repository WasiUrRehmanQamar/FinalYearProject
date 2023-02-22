const config =require("../../dbConfig");
var NewsUpdates = require("../../models/NewsUpdates");
const router = require("express").Router();
const sql = require('mssql')
const ab = require("./NewsUpdatesFunctions")

router.get("/getNewsUpdates",async(req,res)=>{
    ab.getNewsUpdates().then(result=>{
        console.log("The Results are:",result)
        res.json({status:true,result:result})
     })
})

router.post("/addNewsUpdates",async(req,res)=>{
    ab.postNewsUpdates(req).then(result=>{
        console.log("The Results are:",result)
     })
})

module.exports = router