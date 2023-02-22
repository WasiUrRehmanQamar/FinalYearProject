class Content {
     #title;
     #uploadDate;
     #dueDate;
     #titleImage;
     #createdBy;
     #createdDate;
     #modifiedBy;
     #modifiedDate;
     #active;
   
     constructor(
       title,
       uploadDate,
       dueDate,
       titleImage,
       createdBy,
       createdDate,
       modifiedBy,
       modifiedDate,
       active
     ) {
       this.#title = title;
       this.#uploadDate = uploadDate;
       this.#dueDate = dueDate;
       this.#titleImage = titleImage;
       this.#createdBy = createdBy;
       this.#createdDate = createdDate;
       this.#modifiedBy = modifiedBy;
       this.#modifiedDate = modifiedDate;
       this.#active = active;
     }
   
     get title() {
       return this.#title;
     }
   
     set title(value) {
       this.#title = value;
     }
   
     get uploadDate() {
       return this.#uploadDate;
     }
   
     set uploadDate(value) {
       this.#uploadDate = value;
     }
   
     get dueDate() {
       return this.#dueDate;
     }
   
     set dueDate(value) {
       this.#dueDate = value;
     }
   
     get titleImage() {
       return this.#titleImage;
     }
   
     set titleImage(value) {
       this.#titleImage = value;
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
   
   module.exports = {Content };

   