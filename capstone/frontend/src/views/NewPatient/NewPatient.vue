<template>
  <div class="add-patient-main">
    <header>
      <div class="container">
        <div class="row">
          <div class="col header px-4 py-3">
            <img src="../../assets/cancel.svg" class="cancel" alt="cross/cancel-icon" />
            <div class="page-header">New Patient</div>
            <img src="../../assets/tick.svg" class="accept" alt="accept-icon" />
          </div>
        </div>
      </div>
    </header>
    <section class="my-4">
      <div class="container">
        <div class="row mb-2">
          <div class="col basic-info-section">
            <div class="section-header">
              <img src="../../assets/patient.svg" class="section-image" alt="patient-icon" />
              <div class="section-title">Basic Information</div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col section-container pb-4">
            <div class="img-upload-section">
              <div class="image-container">
                <img src="../../assets/camera.svg" alt="camera-icon">
              </div>
              <button class="upload-button">Upload photo</button>
            </div>
            <div class="form-floating section-input-group">
              <input type="text" class="form-control patient-info-input " id="firstName" placeholder="First Name">
              <label for="firstName">First Name</label>
            </div>
            <div class="form-floating section-input-group">
              <input type="text" class="form-control patient-info-input " id="lastName" placeholder="Last Name">
              <label for="lastName">Last Name</label>
            </div>
            <div class="form-floating section-input-group">
              <input type="text" class="form-control patient-info-input " id="age" placeholder="Age">
              <label for="age">Age</label>
            </div>
            <div class="form-floating section-input-group">
              <input type="text" class="form-control patient-info-input " id="sex" placeholder="Sex">
              <label for="sex">Sex</label>
            </div>
            <div class="form-floating section-input-group">
              <input type="text" class="form-control patient-info-input " id="mobile" placeholder="Mobile Number">
              <label for="mobile">Mobile Number</label>
            </div>
            <div class="form-floating section-input-group">
              <input type="text" class="form-control patient-info-input " id="dob" placeholder="Date of Birth">
              <label for="dob">Date of Birth</label>
            </div>
            <div class="form-floating section-input-group">
              <input type="text" class="form-control patient-info-input " id="father-name" placeholder="Father's Name">
              <label for="father-name">Father's Name</label>
            </div>
            <div class="form-floating section-input-group">
              <input type="text" class="form-control patient-info-input " id="mother-name" placeholder="Mother's Name">
              <label for="mother-name">Mother's Name</label>
            </div>
            <div class="form-floating section-input-group">
              <input type="text" class="form-control patient-info-input " id="occupation" placeholder="Occupation">
              <label for="occupation">Occupation</label>
            </div>
            <div class="form-floating section-input-group">
              <input type="text" class="form-control patient-info-input " id="email" placeholder="Email ">
              <label for="email">Email  </label>
            </div>
            <div class="form-floating section-input-group">
              <textarea type="text" class="form-control patient-info-input " id="address" placeholder="Address"></textarea>
              <label for="address">Address</label>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="mb-5">
      <div class="container">
        <div class="row mb-2">
          <div class="col medical-info-section">
            <div class="section-header">
              <img src="../../assets/bloodbag.svg" class="section-image" alt="bloodbag-icon" />
              <div class="section-title">Medical Information</div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col section-container">
              <div class="main-complaints">Main Complaints:</div>
            <div class="section-input-group">
              <input type="text" class="form-control patient-info-input" id="complaint-1" >
              <input type="text" class="form-control patient-info-input" id="complaint-2" >
              <input type="text" class="form-control patient-info-input" id="complaint-3" >
              <div class="add-remove-buttons">
                <button class="addButton">Add</button>
                <button class="removeButton">Remove</button>
              </div>
            </div>
              <div class="allergies">Allergies:</div>
            <div class="section-input-group">
              <input type="text" class="form-control patient-info-input" id="allergy-1" >
              <input type="text" class="form-control patient-info-input" id="allergy-2" >
              <input type="text" class="form-control patient-info-input" id="allergy-3" >
              <div class="add-remove-buttons">
                <button class="addButton">Add</button>
                <button class="removeButton">Remove</button>
              </div>
            </div>
            <div class="other-info">Other Info:</div>
            <div class="section-input-group mb-5">
              <textarea type="text" class="form-control patient-info-input " id="other"></textarea>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
section {
  padding: 0 1.25rem;
}
.header {
  display: flex;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.25);
  .accept {
    margin-left: auto;
  }
  .cancel {
    margin-right: 1.25rem;
  }
}

.section-container {
  background: var(--light-gray);
  border-radius: 20px;
  padding: 0 1.25rem;
}

.section-header {
  display: flex;
  .section-image {
    margin-right: 1rem;
  }
}

.section-input-group {
  .patient-info-input {
    outline: none;
    box-shadow: none;
    border: none;
    background: #DBDBDB;
    border-radius: 5px;
    margin-bottom: 15px;
    &:focus {
      border-bottom-left-radius: 0;
      border-bottom-right-radius: 0;
      border-bottom: 1px solid var(--focus-blue)
    }
  }
  textarea {
    height: 120px;
  }
}

.img-upload-section {
  margin-top: 25px;
  .image-container {
    display: flex;
    width: 140px;
    height: 140px;
    border-radius: 50%;
    border: 1px solid var(--dark-gray);
    margin: 0 auto;
    img {
      display: flex;
      align-self: center;
      margin: 0 auto;
      width: 36px;
      height: 36px;
    }
  }
  .upload-button {
    padding: 0.25rem 0.625rem;
    outline: none;
    border-radius: 5px;
    border: none;
    background: var(--dark-gray);
    color: white;
    font-size: 0.75rem;
    margin: 1rem auto;
    display: flex;
  }
}

.addButton, .removeButton {
  padding: 0.325rem 0.625rem;
  border: none;
  outline: none;
  width: 70px;
  font-size: 0.75rem;
  border-radius: 5px;
  background: var(--button-gray);
  color: white;
}

.addButton {
  background: var(--button-blue);
  margin-right: 0.75rem;
}

.add-remove-buttons {
  display: flex;
  justify-content: flex-end;
}

.main-complaints, .allergies, .other-info {
  margin-top: 20px;
  margin-bottom: 15px;
}
</style>
