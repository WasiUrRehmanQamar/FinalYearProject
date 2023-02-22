class EventCategory {
  #eventCategoryID;
  #eventCategoryName;
  #createdBy;
  #modifiedBy;
  #modifiedDate;
  #active;

  constructor(
    eventCategoryID,
    eventCategoryName,
    createdBy,
    modifiedBy,
    modifiedDate,
    active
  ) {
    this.#eventCategoryID = eventCategoryID;
    this.#eventCategoryName = eventCategoryName;
    this.#createdBy = createdBy;
    this.#modifiedBy = modifiedBy;
    this.#modifiedDate = modifiedDate;
    this.#active = active;
  }

  get eventCategoryID() {
    return this.#eventCategoryID;
  }

  set eventCategoryID(value) {
    this.#eventCategoryID = value;
  }

  get eventCategoryName() {
    return this.#eventCategoryName;
  }

  set eventCategoryName(value) {
    this.#eventCategoryName = value;
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

module.exports = { EventCategory };
