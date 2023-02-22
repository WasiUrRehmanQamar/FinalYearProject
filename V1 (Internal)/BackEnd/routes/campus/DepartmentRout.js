const config =require("../../dbConfig");
var Department = require("../../models/Department");
const router = require("express").Router();
const sql = require('mssql')
const ab = require("./DepartmentFunctions")

router.get("/getDepartment",async(req,res)=>{
    ab.getDepartment().then(result=>{
        console.log("The Results are:",result)
        res.json({status:true,result:result})
     })
})

router.post("/addDepartment",async(req,res)=>{
    ab.postDepartment(req).then(result=>{
        console.log("The Results are:",result)
     })
})

module.exports = router