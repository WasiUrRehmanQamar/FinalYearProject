class Website {
     #websiteID;
     #websiteName;
     #websiteshortName;
     #campusID;
     #DepartmentID;
     #societyID;
     #researchGroupID;
     #conferenceID;
     #createdBy;
     #createdDate;
     #modifiedBy;
     #modifiedDate;
     #active;
     
     constructor(
     websiteID,
     websiteName,
     websiteshortName,
     campusID,
     DepartmentID,
     societyID,
     researchGroupID,
     conferenceID,
     createdBy,
     createdDate = new Date(),
     modifiedBy,
     modifiedDate,
     active = true
     ) {
     this.#websiteID = websiteID;
     this.#websiteName = websiteName;
     this.#websiteshortName = websiteshortName;
     this.#campusID = campusID;
     this.#DepartmentID = DepartmentID;
     this.#societyID = societyID;
     this.#researchGroupID = researchGroupID;
     this.#conferenceID = conferenceID;
     this.#createdBy = createdBy;
     this.#createdDate = createdDate;
     this.#modifiedBy = modifiedBy;
     this.#modifiedDate = modifiedDate;
     this.#active = active;
     }
     
     get websiteID() {
     return this.#websiteID;
     }
     
     set websiteID(value) {
     this.#websiteID = value;
     }
     
     get websiteName() {
     return this.#websiteName;
     }
     
     set websiteName(value) {
     this.#websiteName = value;
     }
     
     get websiteshortName() {
     return this.#websiteshortName;
     }
     
     set websiteshortName(value) {
     this.#websiteshortName = value;
     }
     
     get campusID() {
     return this.#campusID;
     }
     
     set campusID(value) {
     this.#campusID = value;
     }
     
     get DepartmentID() {
     return this.#DepartmentID;
     }
     
     set DepartmentID(value) {
     this.#DepartmentID = value;
     }
     
     get societyID() {
     return this.#societyID;
     }
     
     set societyID(value) {
     this.#societyID = value;
     }
     
     get researchGroupID() {
     return this.#researchGroupID;
     }
     
     set researchGroupID(value) {
     this.#researchGroupID = value;
     }
     
     get conferenceID() {
     return this.#conferenceID;
     }
     
     set conferenceID(value) {
     this.#conferenceID = value;
     }
     
     get createdBy() {
     return this.#createdBy;
     }
     
     set createdBy(value) {
     this.#createdBy = value;
     }
     
     get createdDate() {
     return this.#createdDate;
     }
     
     set createdDate(value) {
     this.#createdDate = value;
     }
     
     get modifiedBy() {
     return this.#modifiedBy;
     }
     
     set modifiedBy(value) {
     this.#modifiedBy = value;
     }
     
     get modifiedDate() {
          return this.#modifiedDate
     }
     set modifiedDate(value){
          this.#modifiedDate=value
     }
     get active() {
          return this.#active
     }
     set active(value){
          this.#active=value
     }
}
module.exports = { Website };