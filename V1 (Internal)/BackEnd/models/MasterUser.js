class MasterUser {
     #masterUserID;
     #fullName;
     #email;
     #password;
     #createdBy;
     #createdDate;
     #modifiedBy;
     #modifiedDate;
     #active;
     
     constructor(
     masterUserID,
     fullName,
     email,
     password,
     createdBy,
     createdDate,
     modifiedBy,
     modifiedDate,
     active
     ) {
     this.#masterUserID = masterUserID;
     this.#fullName = fullName;
     this.#email = email;
     this.#password = password;
     this.#createdBy = createdBy;
     this.#createdDate = createdDate;
     this.#modifiedBy = modifiedBy;
     this.#modifiedDate = modifiedDate;
     this.#active = active;
     }
     
     get masterUserID() {
     return this.#masterUserID;
     }
     
     set masterUserID(value) {
     this.#masterUserID = value;
     }
     
     get fullName() {
     return this.#fullName;
     }
     
     set fullName(value) {
     this.#fullName = value;
     }
     
     get email() {
     return this.#email;
     }
     
     set email(value) {
     this.#email = value;
     }
     
     get password() {
     return this.#password;
     }
     
     set password(value) {
     this.#password = value;
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
     
     module.exports = { MasterUser };

     
     
     
     