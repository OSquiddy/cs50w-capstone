<template>
  <div class="settings-main">
    <form action="" class="settings-form" method="POST">
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
    <div class="container-fluid new-section" v-if="!edit">
      <div class="row">
        <div class="col-6">
          <div class="user-title-section">
            <div class="user-title">Dr. Severus Snape</div>
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
                <div class="section-input-group">
                  <label for="first-name">First Name:</label>
                  <input type="text" name="first-name" id="first-name" autocomplete="off" v-if="edit"/>
                </div>
              </div>
            </div>
            <div class="col-3 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="last-name">Last Name:</label>
                  <input type="text" name="last-name" id="last-name" autocomplete="off" v-if="edit"/>
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
                <div class="section-title">ID Number:</div>
                <div class="section-data" v-if="!edit">21510</div>
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
                  <input type="email" name="email" id="email" value="severus.snape@hogwarts.com" autocomplete="off" v-if="edit"/>
                </div>
                <div class="section-data" v-if="!edit">severus.snape@hogwarts.com</div>
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
                <vue-tel-input :autoDefaultCountry="true" :dropdownOptions="{ showDialCodeInSelection: true, showDialCodeInList: true, showFlags: true }" v-if="edit">
                  <template v-slot:arrow-icon>
                    <svg width="10" height="6" viewBox="0 0 10 6" fill="none" style="margin-left: 3px;" xmlns="http://www.w3.org/2000/svg">
                      <path
                        d="M4.99998 5.51227C4.82076 5.51227 4.64156 5.44609 4.50493 5.31403L0.205142 1.15603C-0.0683806 0.89153 -0.0683806 0.462688 0.205142 0.198295C0.478554 -0.0660983 0.921935 -0.0660983 1.19548 0.198295L4.99998 3.87752L8.80451 0.198423C9.07803 -0.0659698 9.52137 -0.0659698 9.79476 0.198423C10.0684 0.462817 10.0684 0.891658 9.79476 1.15616L5.49504 5.31416C5.35834 5.44625 5.17914 5.51227 4.99998 5.51227Z"
                        fill="#666666"
                      />
                    </svg>
                  </template>
                </vue-tel-input>
                <div class="section-data" v-if="!edit">+1 (324) 2626 2356</div>
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
                  <label for="last-name">Date of Birth:</label>
                  <input type="date" name="dob" id="dob" autocomplete="off" v-if="edit"/>
                </div>
                <div class="section-data" v-if="!edit">2021-06-12</div>
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
                  <input type="text" name="address" id="address" autocomplete="off" />
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-3 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="last-name">City:</label>
                  <input type="text" name="city" id="city" autocomplete="off" />
                </div>
              </div>
            </div>
            <div class="col-3 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="last-name">State:</label>
                  <input type="text" name="state" id="state" autocomplete="off" />
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-3 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="last-name">Zipcode:</label>
                  <input type="text" name="zipcode" id="zipcode" autocomplete="off" />
                </div>
              </div>
            </div>
            <div class="col-3 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="last-name">Country:</label>
                  <input type="text" name="Country" id="Country" autocomplete="off" />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col address-section" v-if="!edit">
          <div class="col-6">
            <div class="section-info-container">
              <div class="section-title">Address:</div>
              <div class="section-data" >Lorem ipsum dolor sit amet, consectetur adipisicing elit. At recusandae saepe expedita iste quam quibusdam officia perferendis neque eligendi. Quae culpa aliquid rem a illum, quaerat ut nobis recusandae atque.</div>
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
                    <input type="radio" name="gender-option" id="male" />
                    <label for="male">M</label>
                  </div>
                  <div class="gender-option">
                    <input type="radio" name="gender-option" id="female" />
                    <label for="female">F</label>
                  </div>
                  <div class="gender-option">
                    <input type="radio" name="gender-option" id="other" />
                    <label for="other">O</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid new-section" v-if="edit">
      <div class="row">
        <div class="col father-section">
          <div class="row">
            <div class="col-6 section-info">
              <div class="section-info-container">
                <div class="section-input-group">
                  <label for="father">Father's Name:</label>
                  <input type="text" name="father" id="father" autocomplete="off" />
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
          <input type="submit" value="Save" @click.prevent="submitForm" class="save-button" v-if="edit">
        </div>
      </div>
    </div>
    </form>
  <router-view name="default" />
  </div>
</template>

<script>
import { VueTelInput } from 'vue-tel-input'
export default {
  name: 'Upcoming',
  components: {
    VueTelInput
  },
  data () {
    return {
      edit: false
    }
  },
  methods: {
    toggleEdit () {
      this.edit = !this.edit
    }
  }
}
</script>

<style lang="scss" scoped>
.settings-main {
  background-color: var(--background-primary);
  padding: 1rem;
  margin-top: 30px;
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
      top: 19%;
      left: 0;
      width: 40px;
      height: 40px;
    }
    input[name='gender-option'] {
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
      // &::after {
      //   // content: ' ';
      //   position: absolute;
      //   width: 40px;
      //   height: 40px;
      //   border-radius: 50%;
      //   border: none;
      //   background: var(--light-gray);
      //   // background: var(--primary-accent-dark);
      //   top: 0;
      //   left: 0;
      // }
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
</style>
