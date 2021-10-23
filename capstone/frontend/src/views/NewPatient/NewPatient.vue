<template>
  <div class="add-patient-main">
    <form action="" class="add-patient-form" method="POST" @submit.prevent="submitForm">
    <input type="submit" value="Save" class="save-button">
    <div class="container-fluid new-section">
      <div class="row">
        <div class="col image-section">
          <div class="row">
            <div class="col-6 section-info">
              <div class="section-info-container">
                <div class="image-container">
          <img src="../../assets/camera.svg" alt="camera-icon">
        </div>
                <div class="image-button-group">
                  <button class="image-button upload">Upload</button>
                  <button class="image-button discard">Discard</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid new-section">
      <div class="row">
        <div class="col name-section">
          <div class="row">
            <div class="col-3 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="first_name">First Name<span class="required">*</span> :</label>
                  <input type="text" name="first_name" id="first_name" autocomplete="off" v-model="first_name" />
                </div>
              </div>
            </div>
            <div class="col-3 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="last_name">Last Name<span class="required">*</span> :</label>
                  <input type="text" name="last_name" id="last_name" autocomplete="off" v-model="last_name" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- <div class="container-fluid new-section">
      <div class="row">
        <div class="col username-section">
          <div class="row">
            <div class="col-6 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="username">Username<span class="required">*</span> :</label>
                  <input type="username" name="username" id="username" autocomplete="off" v-model="username" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div> -->
    <div class="container-fluid new-section">
      <div class="row">
        <div class="col email-section">
          <div class="row">
            <div class="col-6 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="email">Email<span class="required">*</span> :</label>
                  <input type="email" name="email" id="email" autocomplete="off" v-model="email" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid new-section">
      <div class="row">
        <div class="col">
          <div class="row mobile-section justify-content-between">
            <div class="col-6 section-info">
              <div class="section-info-container">
                <div class="section-title">Mobile<span class="required">*</span> :</div>
                <vue-tel-input :autoDefaultCountry="true" :dropdownOptions="{ showDialCodeInSelection: true, showDialCodeInList: true, showFlags: true }" v-model="mobile">
                  <template v-slot:arrow-icon>
                    <svg width="10" height="6" viewBox="0 0 10 6" fill="none" style="margin-left: 3px;" xmlns="http://www.w3.org/2000/svg">
                      <path
                        d="M4.99998 5.51227C4.82076 5.51227 4.64156 5.44609 4.50493 5.31403L0.205142 1.15603C-0.0683806 0.89153 -0.0683806 0.462688 0.205142 0.198295C0.478554 -0.0660983 0.921935 -0.0660983 1.19548 0.198295L4.99998 3.87752L8.80451 0.198423C9.07803 -0.0659698 9.52137 -0.0659698 9.79476 0.198423C10.0684 0.462817 10.0684 0.891658 9.79476 1.15616L5.49504 5.31416C5.35834 5.44625 5.17914 5.51227 4.99998 5.51227Z"
                        fill="#666666"
                      />
                    </svg>
                  </template>
                </vue-tel-input>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid new-section">
      <div class="row">
        <div class="col dob-section">
          <div class="row">
            <div class="col-6 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="dob">Date of Birth:<span class="required">*</span></label>
                  <datetime v-model="dob" type="date" name="dob" id="dob" :format="'MMMM dd, yyyy'" class="theme-red"></datetime>
                  <!-- <input type="date" name="dob" id="dob" autocomplete="off" v-model="dob" /> -->
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid new-section">
      <div class="row">
        <div class="col address-section">
          <div class="row">
            <div class="col-6 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="address">Address:<span class="required">*</span></label>
                  <input type="text" name="address" id="address" autocomplete="off" v-model="address" />
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-3 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="city">City:</label>
                  <input type="text" name="city" id="city" autocomplete="off" v-model="city" />
                </div>
              </div>
            </div>
            <div class="col-3 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="state">State:</label>
                  <input type="text" name="state" id="state" autocomplete="off" v-model="state" />
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-3 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="zipcode">Zipcode:</label>
                  <input type="text" name="zipcode" id="zipcode" autocomplete="off" v-model="zipcode" />
                </div>
              </div>
            </div>
            <div class="col-3 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="country">Country<span class="required">*</span> :</label>
                  <input type="text" name="Country" id="Country" autocomplete="off" v-model="country"/>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid new-section">
      <div class="row">
        <div class="col gender-section">
          <div class="row">
            <div class="col-6 section-info">
              <div class="section-info-container">
                <div class="section-title">Gender<span class="required">*</span> :</div>
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
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid new-section">
      <div class="row">
        <div class="col age-section">
          <div class="row">
            <div class="col-6 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="age">Age<span class="required">*</span> :</label>
                  <input type="number" name="age" id="age" autocomplete="off" v-model="age"/>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid new-section">
      <div class="row">
        <div class="col occupation-section">
          <div class="row">
            <div class="col-3 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="blood_type">Blood Type :</label>
                  <input list="blood_type_list" type="text" name="blood_type" id="blood_type" autocomplete="off" v-model="blood_type"/>
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
                </div>
              </div>
            </div>
            <div class="col-3 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="patient_type">Patient Type :</label>
                  <input type="text" name="patient_type" id="patient_type" autocomplete="off" v-model="patient_type" list="patient_type_list"/>
                  <datalist id="patient_type_list">
                    <option value="In-Patient Department (IPD)" />
                    <option value="Out-Patient Department (OPD)" />
                  </datalist>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid new-section">
      <div class="row">
        <div class="col father-section">
          <div class="row">
            <div class="col-6 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="fathers_name">Father's Name :</label>
                  <input type="text" name="fathers_name" id="fathers_name" autocomplete="off" v-model="fathers_name"/>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid new-section">
      <div class="row">
        <div class="col mother-section">
          <div class="row">
            <div class="col-6 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="mothers_name">Mother's Name :</label>
                  <input type="text" name="mothers_name" id="mothers_name" autocomplete="off" v-model="mothers_name" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid new-section">
      <div class="row">
        <div class="col occupation-section">
          <div class="row">
            <div class="col-6 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="occupation">Occupation :</label>
                  <input type="text" name="occupation" id="occupation" autocomplete="off" v-model="occupation"/>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    </form>
  </div>
</template>

<script>
import { VueTelInput } from 'vue-tel-input'
import axios from 'axios'
import { DateTime } from 'luxon'
import { Datetime } from 'vue-datetime'
import { Snackbar } from '../../util/util'

export default {
  name: 'NewPatient',
  components: {
    VueTelInput,
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
        console.log(response)
        if (response.status === 200) {
          this.$router.push('/')
          if (response.status === 200) {
            Snackbar('Patient Created!', 'var(--success)')
          }
        }
      } catch (error) {
        Snackbar('Creation Unsuccessful', 'var(--error-text)')
      }
    }
  }

}
</script>

<style lang="scss" scoped>
.add-patient-main {
  margin-top: 30px;
  background-color: var(--background-primary);
  padding: 1rem;
  padding-top: calc(30px + 1rem);
  border-radius: 0.75rem;
  border: 1px transparent;
}

.new-section, .address-section .row:nth-child(1), .row:nth-child(2) {
  margin-bottom: 25px;
}

  .image-container {
    display: flex;
    width: 135px;
    height: 135px;
    border-radius: 50%;
    border: 1px solid var(--dark-gray);
    margin-left: auto;
    margin-right: 1rem;
    img {
      display: flex;
      align-self: center;
      margin: 0 auto;
      width: 36px;
      height: 36px;
    }
  }

.image-section {
  .section-info-container {
    display: flex;
  }
  .photo {
    background: var(--medium-gray);
    width: 25%;
    aspect-ratio: 1;
    border-radius: 50%;
  }
  .image-button-group {
    align-self: center;
    margin-right: auto;
    .image-button {
      display: block;
      width: 100%;
      background: none;
      border: none;
    }
    .upload {
      color: var(--link-blue);
    }
  }
}

::v-deep .section-info-container {
  .section-title {
    margin-bottom: 5px;
    font-size: 0.875rem;
  }
  .section-data {
    color: var(--section-data-color);
  }
  .section-input-group {
    margin-bottom: 12px;
    label {
      width: 100%;
      font-size: 0.875rem;
    }
    input {
      background: var(--light-gray);
      border: none;
      outline: none;
      width: 100%;
      padding: 5px 10px;
      color: var(--input-text-color);
      border-radius: 5px;
      margin-top: 5px;
      &:focus {
        border-bottom: 1px solid var(--focus-blue);
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 0;
      }
    }
  }
}

.section-info-container > .section-input-group:last-child {
  margin-bottom: 0;
}

.gender-options-container {
  display: flex;
  margin-top: 1.5rem;
  .gender-option {
    text-align: center;
    position: relative;
    margin-right: 1rem;
    label {
      z-index: 5;
      position: absolute;
      color: var(--input-text-color);
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
      background: var(--light-gray);
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

::v-deep .vti__dropdown-list {
  width: 323%;
  top: 105%;
  & li:hover {
    background: var(--light-gray);
  }
}

::v-deep .vue-tel-input {
  border: none;
  box-shadow: none;
   .vti__dropdown {
    background: var(--light-gray);
    border-radius: 5px;
    padding: 5px;
    .vti__country-code {
      color: var(--input-text-color);
    }
  }
  .vti__input {
    margin-left: 1rem;
    border-radius: 5px;
    background: var(--light-gray);
  }
}

.add-patient-form {
  position: relative;
}
.save-button {
  padding: 0.325rem 0.625rem;
  display: flex;
  justify-content: center;
  border: none;
  outline: none;
  width: 100px;
  font-size: 0.75rem;
  border-radius: 5px;
  background: var(--button-blue);
  color: white;
  margin-left: auto;
  position: sticky;
  top: 20px;
  right: 0;
}

.required {
  color: var(--primary-accent-light);
}
</style>
