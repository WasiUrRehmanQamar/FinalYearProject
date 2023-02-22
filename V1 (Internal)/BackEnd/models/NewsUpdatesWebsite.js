class NewUpdateWebsite {
     #newUpdateWebsiteID;
     #newUpdateID;
     #websiteID;
     #departmentID;
     #societyID;
     #createdBy;
     #createdDate;
     #modifiedBy;
     #modifiedDate;
     #active;
     
     constructor(
     newUpdateWebsiteID,
     newUpdateID,
     websiteID,
     departmentID,
     societyID,
     createdBy,
     createdDate,
     modifiedBy,
     modifiedDate,
     active
     ) {
     this.#newUpdateWebsiteID = newUpdateWebsiteID;
     this.#newUpdateID = newUpdateID;
     this.#websiteID = websiteID;
     this.#departmentID = departmentID;
     this.#societyID = societyID;
     this.#createdBy = createdBy;
     this.#createdDate = createdDate;
     this.#modifiedBy = modifiedBy;
     this.#modifiedDate = modifiedDate;
     this.#active = active;
     }
     
     get newUpdateWebsiteID() {
     return this.#newUpdateWebsiteID;
     }
     
     set newUpdateWebsiteID(value) {
     this.#newUpdateWebsiteID = value;
     }
     
     get newUpdateID() {
     return this.#newUpdateID;
     }
     
     set newUpdateID(value) {
     this.#newUpdateID = value;
     }
     
     get websiteID() {
     return this.#websiteID;
     }
     
     set websiteID(value) {
     this.#websiteID = value;
     }
     
     get departmentID() {
     return this.#departmentID;
     }
     
     set departmentID(value) {
     this.#departmentID = value;
     }
     
     get societyID() {
     return this.#societyID;
     }
     
     set societyID(value) {
     this.#societyID = value;
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
     module.exports = {NewUpdateWebsite };
     
     
     
     