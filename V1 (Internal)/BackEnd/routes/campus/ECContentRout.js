const config =require("../../dbConfig");
var ECContent = require("../../models/ECContent");
const router = require("express").Router();
const sql = require('mssql')
const ab = require("./ECContentFunctions")

router.get("/getECContent",async(req,res)=>{
    ab.getECContent().then(result=>{
        console.log("The Results are:",result)
        res.json({status:true,result:result})
     })
})

router.post("/addECContent",async(req,res)=>{
    ab.postECContent(req).then(result=>{
        console.log("The Results are:",result)
     })
})

module.exports = router