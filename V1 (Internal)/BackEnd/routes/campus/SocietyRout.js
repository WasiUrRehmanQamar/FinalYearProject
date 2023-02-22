const config =require("../../dbConfig");
var Society = require("../../models/Society");
const router = require("express").Router();
const sql = require('mssql')
const ab = require("./SocietyFunctions")

router.get("/getSociety",async(req,res)=>{
    ab.getSociety().then(result=>{
        console.log("The Results are:",result)
        res.json({status:true,result:result})
     })
})

router.post("/addSociety",async(req,res)=>{
    ab.postSociety(req).then(result=>{
        console.log("The Results are:",result)
     })
})

module.exports = router