class ECContentWebsite {
     #ECContentWebsiteID;
     #ECContentID;
     #WebsiteID;
     #createdBy;
     #createdDate;
     #modifiedBy;
     #modifiedDate;
     #active;
     
     constructor(
     ECContentWebsiteID,
     ECContentID,
     WebsiteID,
     createdBy,
     createdDate,
     modifiedBy,
     modifiedDate,
     active
     ) {
     this.#ECContentWebsiteID = ECContentWebsiteID;
     this.#ECContentID = ECContentID;
     this.#WebsiteID = WebsiteID;
     this.#createdBy = createdBy;
     this.#createdDate = createdDate;
     this.#modifiedBy = modifiedBy;
     this.#modifiedDate = modifiedDate;
     this.#active = active;
     }
     
     get ECContentWebsiteID() {
     return this.#ECContentWebsiteID;
     }
     
     set ECContentWebsiteID(value) {
     this.#ECContentWebsiteID = value;
     }
     
     get ECContentID() {
     return this.#ECContentID;
     }
     
     set ECContentID(value) {
     this.#ECContentID = value;
     }
     
     get WebsiteID() {
     return this.#WebsiteID;
     }
     
     set WebsiteID(value) {
     this.#WebsiteID = value;
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
     
     module.exports = { ECContentWebsite };

     
     
     
     