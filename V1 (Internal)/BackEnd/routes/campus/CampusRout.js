const config =require("../../dbConfig");
var Campus = require("../../models/Campus");
const router = require("express").Router();
const sql = require('mssql')
const ab = require("./CampusFunctions")

router.get("/getCampus",async(req,res)=>{
    ab.getcampus().then(result=>{
        console.log("The Results are:",result)
        res.json({status:true,result:result})
     })
})

router.post("/addCampus",async(req,res)=>{
    ab.postCampus(req,res).then(result=>{
        console.log("The Results are:",result)
     })
})

module.exports = router