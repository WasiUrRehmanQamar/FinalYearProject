class Society {
     #SocietyID;
     #SocietyName;
     #SocietyShortName;
     #campusID;
     #departmentID;
     #createdBy;
     #createdDate;
     #modifiedBy;
     #modifiedDate;
     #active;
     
     constructor(
     SocietyID,
     SocietyName,
     SocietyShortName,
     campusID,
     departmentID,
     createdBy,
     createdDate,
     modifiedBy,
     modifiedDate,
     active
     ) {
     this.#SocietyID = SocietyID;
     this.#SocietyName = SocietyName;
     this.#SocietyShortName = SocietyShortName;
     this.#campusID = campusID;
     this.#departmentID = departmentID;
     this.#createdBy = createdBy;
     this.#createdDate = createdDate;
     this.#modifiedBy = modifiedBy;
     this.#modifiedDate = modifiedDate;
     this.#active = active;
     }
     
     get SocietyID() {
     return this.#SocietyID;
     }
     
     set SocietyID(value) {
     this.#SocietyID = value;
     }
     
     get SocietyName() {
     return this.#SocietyName;
     }
     
     set SocietyName(value) {
     this.#SocietyName = value;
     }
     
     get SocietyShortName() {
     return this.#SocietyShortName;
     }
     
     set SocietyShortName(value) {
     this.#SocietyShortName = value;
     }
     
     get campusID() {
     return this.#campusID;
     }
     
     set campusID(value) {
     this.#campusID = value;
     }
     
     get departmentID() {
     return this.#departmentID;
     }
     
     set departmentID(value) {
     this.#departmentID = value;
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
     module.exports = { Society };
     