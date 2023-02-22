class Campus {
  #campusID;
  #campusName;
  #campusShortName;
  #campusAddress;
  #campusPhone;
  #campusEmail;
  #createdBy;
  #createdDate;
  #modifiedBy;
  #active;

  constructor(
    campusID,
    campusName,
    campusShortName,
    campusAddress,
    campusPhone,
    campusEmail,
    createdBy,
    createdDate,
    modifiedBy,
    active
  ) {
    this.#campusID = campusID;
    this.#campusName = campusName;
    this.#campusShortName = campusShortName;
    this.#campusAddress = campusAddress;
    this.#campusPhone = campusPhone;
    this.#campusEmail = campusEmail;
    this.#createdBy = createdBy;
    this.#createdDate = createdDate;
    this.#modifiedBy = modifiedBy;
    this.#active = active;
  }

  get campusID() {
    return this.#campusID;
  }

  set campusID(value) {
    this.#campusID = value;
  }

  get campusName() {
    return this.#campusName;
  }

  set campusName(value) {
    this.#campusName = value;
  }

  get campusShortName() {
    return this.#campusShortName;
  }

  set campusShortName(value) {
    this.#campusShortName = value;
  }

  get campusAddress() {
    return this.#campusAddress;
  }

  set campusAddress(value) {
    this.#campusAddress = value;
  }

  get campusPhone() {
    return this.#campusPhone;
  }

  set campusPhone(value) {
    this.#campusPhone = value;
  }

  get campusEmail() {
    return this.#campusEmail;
  }

  set campusEmail(value) {
    this.#campusEmail = value;
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

  get active() {
    return this.#active;
  }

  set active(value) {
    this.#active = value;
  }
}
module.exports = { Campus }
