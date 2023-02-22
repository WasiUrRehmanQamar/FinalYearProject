class ECContent {
  #ECContentID;
  #Title;
  #UploadDate;
  #DueDate;
  #Catagory;
  #EventCatagoryID;
  #createdBy;
  #createdDate;
  #modifiedBy;
  #modifiedDate;
  #active;

  constructor(
    ECContentID,
    Title,
    UploadDate,
    DueDate,
    Catagory,
    EventCatagoryID,
    createdBy,
    createdDate,
    modifiedBy,
    modifiedDate,
    active
  ) {
    this.#ECContentID = ECContentID;
    this.#Title = Title;
    this.#UploadDate = UploadDate;
    this.#DueDate = DueDate;
    this.#Catagory = Catagory;
    this.#EventCatagoryID = EventCatagoryID;
    this.#createdBy = createdBy;
    this.#createdDate = createdDate;
    this.#modifiedBy = modifiedBy;
    this.#modifiedDate = modifiedDate;
    this.#active = active;
  }

  get ECContentID() {
    return this.#ECContentID;
  }

  set ECContentID(value) {
    this.#ECContentID = value;
  }

  get Title() {
    return this.#Title;
  }

  set Title(value) {
    this.#Title = value;
  }

  get UploadDate() {
    return this.#UploadDate;
  }

  set UploadDate(value) {
    this.#UploadDate = value;
  }

  get DueDate() {
    return this.#DueDate;
  }

  set DueDate(value) {
    this.#DueDate = value;
  }

  get Catagory() {
    return this.#Catagory;
  }

  set Catagory(value) {
    this.#Catagory = value;
  }

  get EventCatagoryID() {
    return this.#EventCatagoryID;
  }

  set EventCatagoryID(value) {
    this.#EventCatagoryID = value;
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

module.exports = {ECContent };
