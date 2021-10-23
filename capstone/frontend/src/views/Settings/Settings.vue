<template>
  <div class="settings-container">
    <form action="" method="post" enctype="multipart/form-data" class="settings-form" @submit.prevent="upload">
    <aside class="settings-sidepanel">
      <div class="container-fluid new-section">
        <div class="row">
          <div class="col image-section">
            <div class="row">
              <div class="col section-info">
                <div class="section-info-container">
                  <div class="image-container">
                    <img :src="photo" class="profilePic" id="image">
                  </div>
                  <div class="image-button-group" v-if="edit">
                    <input type="file" name="profilePic" id="id_profilePic" accept="image/*" @change="showPreview($event)" class="d-none">
                    <label class="image-button upload" for="id_profilePic">Upload</label>
                    <button class="image-button discard" @click="removePic" type="button">Discard</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </aside>
    <section class="settings-main">
      <div class="container-fluid new-section" v-if="!edit">
        <div class="row">
          <div class="col-6">
            <div class="user-title-section">
              <div class="user-title">Dr. {{currentUser.fullname}}</div>
              <img src="../../assets/edit.svg" alt="edit-icon" class="edit-icon" @click="toggleEdit"/>
            </div>
          </div>
        </div>
      </div>
      <div class="container-fluid new-section" v-if="edit">
        <div class="row">
          <div class="col name-section">
            <div class="row">
              <div class="col-3 section-info">
                <div class="section-info-container">
                  <div class="section-title">Name:</div>
                  <div class="section-data">{{currentUser.fullname}}</div>
                </div>
              </div>
              <div class="col-3 section-info">
                <div class="section-info-container">
                  <div class="section-title">ID Number:</div>
                  <div class="section-data">{{currentUser.id}}</div>
                </div>
              </div>
              <!-- <div class="col-3 section-info">
                <div class="section-info-container">
                  <div class="section-input-group">
                    <label for="first-name">First Name:</label>
                    <input type="text" name="first-name" id="first-name" autocomplete="off" v-if="edit" :value="currentUser.first_name" readonly/>
                  </div>
                </div>
              </div>
              <div class="col-3 section-info">
                <div class="section-info-container">
                  <div class="section-input-group">
                    <label for="last-name">Last Name:</label>
                    <input type="text" name="last-name" id="last-name" autocomplete="off" :value="currentUser.last_name" v-if="edit" readonly/>
                  </div>
                </div>
              </div> -->
            </div>
          </div>
        </div>
      </div>
      <div class="container-fluid new-section" v-if="!edit">
        <div class="row">
          <div class="col id-section">
            <div class="row">
              <div class="col-6 section-info">
                <div class="section-info-container">
                  <div class="section-title">ID Number:</div>
                  <div class="section-data">{{currentUser.id}}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="container-fluid new-section">
        <div class="row">
          <div class="col id-section">
            <div class="row">
              <div class="col-6 section-info">
                <div class="section-info-container">
                  <div class="section-input-group">
                    <label for="username">Username:</label>
                    <input type="text" name="username" id="username" autocomplete="off" v-if="edit" v-model="username" />
                  </div>
                    <div class="section-data" v-if="!edit">{{currentUser.username}}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="container-fluid new-section">
        <div class="row">
          <div class="col email-section">
            <div class="row">
              <div class="col-6 section-info">
                <div class="section-info-container">
                  <div class="section-input-group">
                    <label for="last-name">Email:</label>
                    <input type="email" name="email" id="email" autocomplete="off" v-if="edit" v-model="email"/>
                  </div>
                  <div class="section-data" v-if="!edit">{{currentUser.email}}</div>
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
                  <div class="section-title">Mobile:</div>
                  <vue-tel-input :autoDefaultCountry="true" :dropdownOptions="{ showDialCodeInSelection: true, showDialCodeInList: true, showFlags: true }" v-if="edit" v-model="mobile">
                    <template v-slot:arrow-icon>
                      <svg width="10" height="6" viewBox="0 0 10 6" fill="none" style="margin-left: 3px;" xmlns="http://www.w3.org/2000/svg">
                        <path
                          d="M4.99998 5.51227C4.82076 5.51227 4.64156 5.44609 4.50493 5.31403L0.205142 1.15603C-0.0683806 0.89153 -0.0683806 0.462688 0.205142 0.198295C0.478554 -0.0660983 0.921935 -0.0660983 1.19548 0.198295L4.99998 3.87752L8.80451 0.198423C9.07803 -0.0659698 9.52137 -0.0659698 9.79476 0.198423C10.0684 0.462817 10.0684 0.891658 9.79476 1.15616L5.49504 5.31416C5.35834 5.44625 5.17914 5.51227 4.99998 5.51227Z"
                          fill="#666666"
                        />
                      </svg>
                    </template>
                  </vue-tel-input>
                  <div class="section-data" v-if="!edit">{{currentUser.Phone_Number}}</div>
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
                    <label for="dob">Date of Birth:</label>
                    <input type="date" name="dob" id="dob" autocomplete="off" v-if="edit" v-model="dob"/>
                  </div>
                  <div class="section-data" v-if="!edit">{{currentUser.date_of_birth}}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="container-fluid new-section">
        <div class="row">
          <div class="col address-section" v-if="edit">
            <div class="row">
              <div class="col-6 section-info">
                <div class="section-info-container">
                  <div class="section-input-group">
                    <label for="last-name">Address:</label>
                    <input type="text" name="address" id="address" autocomplete="off" v-model="address" />
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-3 section-info">
                <div class="section-info-container">
                  <div class="section-input-group">
                    <label for="last-name">City:</label>
                    <input type="text" name="city" id="city" autocomplete="off" v-model="city" />
                  </div>
                </div>
              </div>
              <div class="col-3 section-info">
                <div class="section-info-container">
                  <div class="section-input-group">
                    <label for="last-name">State:</label>
                    <input type="text" name="state" id="state" autocomplete="off" v-model="state" />
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-3 section-info">
                <div class="section-info-container">
                  <div class="section-input-group">
                    <label for="last-name">Zipcode:</label>
                    <input type="text" name="zipcode" id="zipcode" autocomplete="off" v-model="zipcode" />
                  </div>
                </div>
              </div>
              <div class="col-3 section-info">
                <div class="section-info-container">
                  <div class="section-input-group">
                    <label for="last-name">Country:</label>
                    <input type="text" name="Country" id="Country" autocomplete="off" v-model="country" />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col address-section" v-if="!edit">
            <div class="col-6">
              <div class="section-info-container">
                <div class="section-title">Address:</div>
                <div class="section-data" >{{currentUser.address}}</div>
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
                  <div class="section-title">Gender:</div>
                  <div class="section-data gender-options-container">
                    <div class="gender-option">
                      <input type="radio" name="sex" id="male" :disabled="!edit" v-model="sex" value="M" />
                      <label for="male">M</label>
                    </div>
                    <div class="gender-option">
                      <input type="radio" name="sex" id="female" :disabled="!edit" v-model="sex" value="F" />
                      <label for="female">F</label>
                    </div>
                    <div class="gender-option">
                      <input type="radio" name="sex" id="other" :disabled="!edit" v-model="sex" value="O" />
                      <label for="other">O</label>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="container-fluid">
        <div class="row">
          <div class="col-6 d-flex">
            <input type="button" value="Cancel" @click="toggleEdit" class="cancel-button" v-if="edit">
            <input type="submit" value="Save" class="save-button" v-if="edit">
          </div>
        </div>
      </div>
    </section>
    </form>
  </div>
</template>

<script>
import { VueTelInput } from 'vue-tel-input'
// import { DateTime } from 'luxon'
import { mapActions, mapState } from 'vuex'
import axios from 'axios'
import { Snackbar } from '../../util/util'

export default {
  name: 'Settings',
  components: {
    VueTelInput
  },
  data () {
    return {
      edit: false,
      imageURL: null,
      image: null,
      sex: null,
      country: '',
      address: '',
      city: '',
      zipcode: '',
      state: '',
      dob: '',
      email: '',
      mobile: null,
      username: ''
    }
  },
  computed: {
    ...mapState(['currentUser']),
    photo () {
      if (this.currentUser.profilePic) {
        if (this.currentUser.profilePic.includes('http')) {
          return this.currentUser.profilePic
        } else {
          return 'http://localhost:8080/assets' + this.currentUser.profilePic
        }
      }
      return ''
    }
  },
  created () {
    this.populateForm()
  },
  methods: {
    ...mapActions(['setCurrentUser']),
    toggleEdit () {
      this.edit = !this.edit
      if (this.edit === false) {
        this.populateForm()
      }
    },
    showPreview (event) {
      const img = document.querySelector('#image')
      this.image = event.target.files[0]
      img.src = URL.createObjectURL(event.target.files[0])
      console.log(img.src)
      this.imageURL = img.src
    },
    removePic () {
      const img = document.querySelector('#image')
      img.src = ''
    },
    async upload () {
      const imgData = new FormData()
      const formData = {
        email: this.email,
        sex: this.sex,
        address: this.address,
        city: this.city,
        state: this.state,
        zipcode: this.zipcode,
        country: this.country,
        dob: this.dob,
        mobile: this.mobile,
        username: this.username
      }
      imgData.append('imageURL', this.imageURL)
      imgData.append('image', this.image)

      try {
        const resp1 = await axios.post(process.env.VUE_APP_API_URL + '/uploadImage', imgData)
        if (resp1.status === 200) {
          Snackbar('Profile Picture Updated', 'var(--success)')
          this.setCurrentUser(resp1.data.user)
          this.edit = false
        }
      } catch (error) {
        Snackbar('Profile pic not updated', 'var(--error-text')
      }
      try {
        const resp2 = await axios.post(process.env.VUE_APP_API_URL + '/updateUser', formData)
        if (resp2.status === 200) {
          Snackbar('Settings Updated', 'var(--success)')
          this.setCurrentUser(resp2.data.user)
          this.edit = false
        }
      } catch (error) {
        Snackbar('Update Unsuccessful', 'var(--error-text')
      }
    },
    populateForm () {
      this.sex = this.currentUser.sex
      this.dob = this.currentUser.date_of_birth
      this.email = this.currentUser.email
      this.mobile = this.currentUser.Phone_Number
      this.username = this.currentUser.username
      this.imageURL = this.currentUser.profilePic

      const addressArray = this.currentUser.address.split(/\r?\n/)
      this.address = addressArray[0]
      this.city = addressArray[1]
      this.state = addressArray[2]
      this.zipcode = addressArray[3]
      this.country = addressArray[4]
    }
  }
}
</script>

<style lang="scss" scoped>
.settings-container {
  background-color: var(--background-primary);
  margin-top: 30px;
  border-radius: 0.75rem;
  // border: 1px solid transparent;
  display: flex;
}

.settings-sidepanel {
  display: flex;
  height: inherit;
  padding: 1rem;
  border-top-left-radius: 0.75rem;
  border-bottom-left-radius: 0.75rem;
  width: 25%;
  background-color: var(--sidepanel-color);
}

.settings-main {
  padding: 1rem;
  display: flex;
  width: 75%;
  flex-direction: column;
}

.new-section, .address-section .row:nth-child(1), .row:nth-child(2) {
  margin-bottom: 25px;
}

::v-deep .image-container {
  display: flex;
  width: 135px;
  height: 135px;
  border-radius: 50%;
  // border: 1px solid var(--dark-gray);
  border: 1px solid var(--light-gray);
  // margin-left: auto;
  // margin-right: 1rem;
  overflow: hidden;
  margin: auto;
  background-image: url('data:image/svg+xml, <svg width="20" height="16" viewBox="0 0 20 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M17.6087 2.78261H15.5217L14.3696 1.04348C13.9348 0.391304 13.1739 0 12.3913 0H7.6087C6.82609 0 6.06522 0.391304 5.63043 1.04348L4.47826 2.78261H2.3913C1.06522 2.78261 0 3.84783 0 5.17391V13.6087C0 14.9348 1.06522 16 2.3913 16H17.6087C18.9348 16 20 14.9348 20 13.6087V5.17391C20 3.84783 18.9348 2.78261 17.6087 2.78261ZM10 14.0435C7.02174 14.0435 4.6087 11.6304 4.6087 8.65217C4.6087 5.67391 7.02174 3.28261 10 3.28261C12.9783 3.28261 15.3913 5.69565 15.3913 8.67391C15.3913 11.6304 12.9783 14.0435 10 14.0435ZM17.3043 6.15217C17.2826 6.15217 17.2609 6.15217 17.2174 6.15217H16.3478C15.9565 6.13043 15.6522 5.80435 15.6739 5.41304C15.6957 5.04348 15.9783 4.76087 16.3478 4.73913H17.2174C17.6087 4.71739 17.9348 5.02174 17.9565 5.41304C17.9783 5.80435 17.6957 6.13043 17.3043 6.15217Z" fill="white"/><path d="M9.99978 5.67397C8.34761 5.67397 6.99978 7.02179 6.99978 8.67397C6.99978 10.3261 8.34761 11.6522 9.99978 11.6522C11.6519 11.6522 12.9998 10.3044 12.9998 8.65223C12.9998 7.00005 11.6519 5.67397 9.99978 5.67397Z" fill="white"/></svg>');
  background-position: center;
  background-repeat: no-repeat;
  background-size: 45px;
  .camera-icon {
    display: flex;
    align-self: center;
    margin: 0 auto;
    width: 36px;
    height: 36px;
    // filter: invert(100);
    * {
      fill: white;
    }
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
      color: white;
      padding: 1px 6px;
      cursor: pointer;
    }
    .upload {
      color: lightblue;
    }
  }
}

.user-title-section {
  display: flex;
  .user-title {
    font-size: 1.5rem;
    display: flex;
  }
  .edit-icon {
    display: flex;
    align-self: center;
    margin-left: auto;
    cursor: pointer;
  }
}

.section-info-container {
  .section-title {
    margin-bottom: 5px;
    font-size: 0.875rem;
  }
  .section-data {
    color: var(--section-data-color);
  }
  .section-input-group {
    margin-bottom: 5px;
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
      &:not(:read-only):focus {
        border-bottom: 1px solid var(--focus-blue);
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 0;
      }
      &:read-only {
        background: var(--lightest-gray);
      }
    }
  }
}

// .section-info-container > .section-input-group:last-child {
//   margin-bottom: 0;
// }

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
      &:not(:disabled) ~ label {
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

.settings-form {
  position: relative;
  display: contents;
}
.save-button, .cancel-button {
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
  // position: sticky;
  // top: 20px;
  // right: 0;
}

.cancel-button {
  margin-left: auto;
  margin-right: 0.625rem;
  background-color: var(--light-gray);
  color: var(--primary);
  border: 1px solid #ccc;
}

.profilePic {
  width: 100%;
  object-fit: fill;
}
</style>
