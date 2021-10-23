<template>
  <div class="add-patient-main">
    <header>
      <div class="container-fluid">
        <div class="row">
          <div class="col header px-4 py-3">
            <button class="cancel" @click="$router.go(-1)">
              <img src="../../assets/cancel.svg" alt="cross/cancel-icon" />
            </button>
            <div class="page-header">New Patient</div>
            <button class="accept"  type="submit" form="add-patient-form">
              <img src="../../assets/tick.svg" alt="accept-icon" />
            </button>
          </div>
        </div>
      </div>
    </header>
    <form action="" method="post" id="add-patient-form" @submit.prevent="submitForm">
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
                <button class="upload-button" @click.prevent="upload">Upload photo</button>
              </div>
              <div class="form-floating section-input-group">
                <input type="text" class="form-control patient-info-input " id="firstName" placeholder="First Name" v-model="first_name">
                <label for="firstName">First Name<span class="required">*</span></label>
              </div>
              <div class="form-floating section-input-group">
                <input type="text" class="form-control patient-info-input " id="lastName" placeholder="Last Name" v-model="last_name">
                <label for="lastName">Last Name<span class="required">*</span></label>
              </div>
              <div class="form-floating section-input-group">
                <input type="text" class="form-control patient-info-input " id="age" placeholder="Age" v-model="age">
                <label for="age">Age<span class="required">*</span></label>
              </div>
              <div class="form-floating section-input-group">
                <input type="text" class="form-control patient-info-input " id="mobile" placeholder="Mobile Number" v-model="mobile">
                <label for="mobile">Mobile Number<span class="required">*</span></label>
              </div>
              <div class="form-floating section-input-group">
                <datetime v-model="dob" type="date" name="dob" id="dob" :format="'MMMM dd, yyyy'" class="theme-red" :class="'form-control patient-info-input'" :input-class="'override'" :placeholder="'Date of Birth'"></datetime>
                <!-- <input type="text" class="form-control patient-info-input " id="dob" placeholder="Date of Birth"> -->
                <label for="dob">Date of Birth<span class="required">*</span></label>
              </div>
              <div class="form-floating section-input-group">
                <input type="text" class="form-control patient-info-input " v-model="email" id="email" placeholder="Email ">
                <label for="email">Email</label>
              </div>
              <div class="form-floating section-input-group">
                <input type="text" class="form-control patient-info-input " id="address" v-model="address" placeholder="Address">
                <label for="address">Address<span class="required">*</span></label>
              </div>
              <div class="form-floating section-input-group">
                <input type="text" class="form-control patient-info-input " id="city" v-model="city" placeholder="City">
                <label for="city">City</label>
              </div>
              <div class="form-floating section-input-group">
                <input type="text" class="form-control patient-info-input " id="state" v-model="state" placeholder="State">
                <label for="state">State</label>
              </div>
              <div class="form-floating section-input-group">
                <input type="text" class="form-control patient-info-input " id="zipcode" v-model="zipcode" placeholder="Zipcode">
                <label for="zipcode">Zipcode</label>
              </div>
              <div class="form-floating section-input-group">
                <input type="text" class="form-control patient-info-input " id="country" v-model="country" placeholder="Country">
                <label for="country">Country<span class="required">*</span></label>
              </div>
              <div class="form-floating section-input-group">
                <!-- <input type="text" class="form-control patient-info-input " id="sex" placeholder="Sex" v-model="sex">
                <label for="sex">Sex</label> -->
                <div class="patient-info-input gender-section">
                  <div class="gender-title">Gender<span class="required">*</span> :</div>
                  <div class="section-data gender-options-container">
                    <div class="gender-option">
                      <input type="radio" name="sex" id="male" v-model="sex" value="M" />
                      <label for="male">M</label>
                    </div>
                    <div class="gender-option">
                      <input type="radio" name="sex" id="female"  v-model="sex" value="F" />
                      <label for="female">F</label>
                    </div>
                    <div class="gender-option">
                      <input type="radio" name="sex" id="other" v-model="sex" value="O" />
                      <label for="other">O</label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="form-floating section-input-group">
                <input type="text" class="form-control patient-info-input " id="father-name" placeholder="Father's Name" v-model="fathers_name">
                <label for="father-name">Father's Name</label>
              </div>
              <div class="form-floating section-input-group">
                <input type="text" class="form-control patient-info-input " id="mother-name" placeholder="Mother's Name" v-model="mothers_name">
                <label for="mother-name">Mother's Name</label>
              </div>
              <div class="form-floating section-input-group">
                <input type="text" class="form-control patient-info-input " id="occupation" placeholder="Occupation" v-model="occupation">
                <label for="occupation">Occupation</label>
              </div>
              <div class="form-floating section-input-group">
                <datalist id="blood_type_list">
                  <option value="A+" />
                  <option value="A-" />
                  <option value="B+" />
                  <option value="B-" />
                  <option value="O+" />
                  <option value="O-" />
                  <option value="AB+" />
                  <option value="AB-" />
                </datalist>
                <input list="blood_type_list" type="text" class="form-control patient-info-input " id="blood_type" placeholder="Blood Type" v-model="blood_type">
                <label for="blood_type">Blood Type</label>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- <section class="mb-5">
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
      </section> -->
    </form>
  </div>
</template>

<script>
// import { VueTelInput } from 'vue-tel-input'
import axios from 'axios'
import { DateTime } from 'luxon'
import { Datetime } from 'vue-datetime'
import { Snackbar } from '../../util/util'

export default {
  name: 'NewPatientMobile',
  components: {
    // VueTelInput,
    Datetime
  },
  data () {
    return {
      username: '',
      first_name: '',
      last_name: '',
      sex: null,
      country: '',
      address: '',
      city: '',
      zipcode: '',
      state: '',
      dob: '',
      email: '',
      fathers_name: '',
      mothers_name: '',
      occupation: '',
      mobile: null,
      blood_type: '',
      patient_type: '',
      age: null
    }
  },
  watch: {
    // dob(newValue, oldValue) {
    //   console.log(this.dob)
    //   console.log(DateTime.fromISO(this.dob).toFormat('yyyy-MM-dd'))
    // }
  },
  mounted () {
    this.dob = DateTime.now().toFormat('yyyy-MM-dd')
    // console.log(this.dob)
    // In-Patient Department (IPD)
  },
  methods: {
    async submitForm () {
      const formData = {
        // username: this.username,
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
        mobile: this.mobile,
        dob: DateTime.fromISO(this.dob).toFormat('yyyy-MM-dd'),
        address: this.address,
        city: this.city,
        state: this.state,
        zipcode: this.zipcode,
        country: this.country,
        fathers_name: this.fathers_name,
        mothers_name: this.mothers_name,
        occupation: this.occupation,
        blood_type: this.blood_type,
        patient_type: this.patient_type,
        sex: this.sex,
        age: this.age
      }
      try {
        const response = await axios.post(process.env.VUE_APP_API_URL + '/create/p', formData)
        if (response.status === 200) {
          this.$router.push('/')
          if (response.status === 200) {
            Snackbar('Patient Created!', 'var(--success)')
          }
        }
      } catch (error) {
        Snackbar('Creation Unsuccessful', 'var(--error-text)')
      }
    },
    upload () {
      // Do something
    }
  }
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
    background: transparent;
    border: none;
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
    background: var(--input-border-color);
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

::v-deep .override {
  border: none;
  background: transparent;
}

.gender-options-container {
  display: flex;
  margin-top: 1.25rem;
  margin-bottom: .875rem;
  justify-content: space-evenly;
  .gender-option {
    text-align: center;
    position: relative;
    margin-right: 1rem;
    label {
      z-index: 5;
      position: absolute;
      color: white;
      top: 0;
      left: 0;
      width: 40px;
      height: 40px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    input[name='sex'] {
      width: 40px;
      height: 40px;
      position: relative;
      display: flex;
      background: var(--dark-gray);
      border-radius: 50%;
      appearance: none;
      & ~ label {
        cursor: pointer;
      }
      &:checked {
        background: var(--primary-accent-dark);
        & ~ label {
          color: white;
        }
      }
    }
  }
}

.gender-section {
  padding: 15px;
}
</style>
