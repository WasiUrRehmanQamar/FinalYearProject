const config =require("../../dbConfig");
var EventCategory = require("../../models/EventCategory");
const router = require("express").Router();
const sql = require('mssql')
const ab = require("./EventCategoryFunctions")

router.get("/getEventCategory",async(req,res)=>{
    ab.getEventCategory().then(result=>{
        console.log("The Results are:",result)
        res.json({status:true,result:result})
     })
})

router.post("/addEventCategory",async(req,res)=>{
    ab.postEventCategory(req).then(result=>{
        console.log("The Results are:",result)
     })
})

module.exports = router