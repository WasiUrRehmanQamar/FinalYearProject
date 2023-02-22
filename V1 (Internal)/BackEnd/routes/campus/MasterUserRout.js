const config =require("../../dbConfig");
var MasterUser = require("../../models/MasterUser");
const router = require("express").Router();
const sql = require('mssql')
const ab = require("./MasterUserFunctions")

router.get("/getMasterUser",async(req,res)=>{
    ab.getMasterUser().then(result=>{
        console.log("The Results are:",result)
        res.json({status:true,result:result})
     })
})

router.post("/addMasterUser",async(req,res)=>{
    ab.postMasterUser(req).then(result=>{
        console.log("The Results are:",result)
     })
})

module.exports = router