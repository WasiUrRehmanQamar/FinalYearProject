class Department {
     #departmentID;
     #departmentName;
     #departmentShortName;
     #campusID;
     #parentDepartmentID;
     #createdBy;
     #modifiedBy;
     #modifiedDate;
     #active;
   
     constructor(
       departmentID,
       departmentName,
       departmentShortName,
       campusID,
       parentDepartmentID,
       createdBy,
       modifiedBy,
       modifiedDate,
       active
     ) {
       this.#departmentID = departmentID;
       this.#departmentName = departmentName;
       this.#departmentShortName = departmentShortName;
       this.#campusID = campusID;
       this.#parentDepartmentID = parentDepartmentID;
       this.#createdBy = createdBy;
       this.#modifiedBy = modifiedBy;
       this.#modifiedDate = modifiedDate;
       this.#active = active;
     }
   
     get departmentID() {
       return this.#departmentID;
     }
   
     set departmentID(value) {
       this.#departmentID = value;
     }
   
     get departmentName() {
       return this.#departmentName;
     }
   
     set departmentName(value) {
       this.#departmentName = value;
     }
   
     get departmentShortName() {
       return this.#departmentShortName;
     }
   
     set departmentShortName(value) {
       this.#departmentShortName = value;
     }
   
     get campusID() {
       return this.#campusID;
     }
   
     set campusID(value) {
       this.#campusID = value;
     }
   
     get parentDepartmentID() {
       return this.#parentDepartmentID;
     }
   
     set parentDepartmentID(value) {
       this.#parentDepartmentID = value;
     }
   
     get createdBy() {
       return this.#createdBy;
     }
   
     set createdBy(value) {
       this.#createdBy = value;
     }
   
     get modifiedBy() {
       return this.#modifiedBy;
     }
   
     set modifiedBy(value) {
       this.#modifiedBy = value;
     }
   
     get modifiedDate() {
       return this.#modifiedDate;
     }
   
     set modifiedDate(value) {
       this.#modifiedDate = value;
     }
   
     get active() {
       return this.#active;
     }
   
     set active(value) {
       this.#active = value;
     }
    }
    module.exports = { Department };