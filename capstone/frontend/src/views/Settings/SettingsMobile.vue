<template>
  <div class="search-main">
    <div class="header">
      <div class="logo">
        <router-link to="/">
          <svg width="44" height="46" viewBox="0 0 44 46" fill="none" xmlns="http://www.w3.org/2000/svg" class="logo-svg">
            <rect x="14.5332" y="1" width="14.5329" height="43.5986" fill="#DB1111" />
            <rect y="15.533" width="43.5986" height="14.5329" fill="#DB1111" />
            <path d="M14.5327 29.7021L21.4358 1.36302" stroke="white" stroke-width="2" stroke-linecap="round" />
            <path d="M29.0653 30.0651L21.4355 1.36269" stroke="white" stroke-width="2" stroke-linecap="round" />
            <path d="M14.5327 15.8958L21.7991 44.2349" stroke="white" stroke-width="2" stroke-linecap="round" />
            <path d="M29.0644 15.8958L21.7981 44.2349" stroke="white" stroke-width="2" stroke-linecap="round" />
            <path d="M7.26611 22.0723L36.3318 22.4356" stroke="white" stroke-width="2" stroke-linecap="round" />
          </svg>
          <span class="logo-text">Settings</span>
        </router-link>
      </div>
      <!-- <div class="container settings-tabs">
        <div class="row">
          <div class="col tab-item active" @click="toggleActive(this)">General</div>
          <div class="col tab-item" @click="toggleActive(this)">Account</div>
        </div>
      </div> -->
      <nav class="tabs">
        <ul>
          <li class="tab-item active" @click="toggleActive">General</li>
          <li class="tab-item" @click="toggleActive">Account</li>
          <li class="slider"></li>
        </ul>
      </nav>
    </div>
    <div class="settings-outer-container" @scroll="scrollHandler">
      <div class="settings-inner-container">
        <div class="general-settings settings-page">
          <div class="container">
            <div class="row">
              <div class="col">
                <div class="settings-group">
                  <div class="settings-group-item">
                    <img src="../../assets/globe.svg" alt="globe-icon" />
                    <div class="settings-group-option">Language</div>
                    <button class="settings-group-button"><img src="../../assets/right-chevron.svg" alt="right-chevron" /></button>
                  </div>
                  <div class="settings-group-item">
                    <img src="../../assets/notification.svg" alt="notification-icon" />
                    <div class="settings-group-option">Notifications</div>
                    <button class="settings-group-button"><img src="../../assets/right-chevron.svg" alt="right-chevron" /></button>
                  </div>
                  <div class="settings-group-item">
                    <img src="../../assets/dark-mode.svg" alt="dark-mode-icon" />
                    <label class="settings-group-option form-check-label" for="flexSwitchCheckChecked">Dark Mode</label>
                    <button class="settings-group-button"><img src="../../assets/switch.svg" alt="right-chevron" /></button>
                    <!-- <div class="form-check form-switch">
                      <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked" checked>
                    </div> -->
                  </div>
                  <div class="settings-group-item">
                    <img src="../../assets/help.svg" alt="help-icon" />
                    <div class="settings-group-option">Help</div>
                    <button class="settings-group-button"><img src="../../assets/right-chevron.svg" alt="right-chevron" /></button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="account-settings settings-page">
          <div class="container new-section">
            <div class="row">
              <div class="col">
                <div class="user-title-section">
                  <div class="user-title">Dr. Severus Snape</div>
                  <img src="../../assets/edit.svg" alt="edit-icon" class="edit-icon" />
                </div>
              </div>
            </div>
          </div>
          <div class="container new-section">
            <div class="row">
              <div class="col">
                <div class="row image-section justify-content-between">
                  <div class="col-1 section-icon">
                    <img src="../../assets/camera.svg" alt="camera-icon" class="camera-icon" />
                  </div>
                  <div class="col-10 section-info">
                    <div class="section-info-container">
                      <div class="photo"></div>
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
          <hr class="section-divider" />
          <div class="container new-section">
            <div class="row">
              <div class="col">
                <div class="row name-section justify-content-between">
                  <div class="col-1 section-icon">
                    <img src="../../assets/doctor.svg" alt="doctor-icon" class="doctor-icon" />
                  </div>
                  <div class="col-10 section-info">
                    <div class="section-info-container">
                      <div class="section-input-group">
                        <label for="first-name">First Name:</label>
                        <input type="text" name="first-name" id="first-name" autocomplete="off" />
                      </div>
                      <div class="section-input-group">
                        <label for="last-name">Last Name:</label>
                        <input type="text" name="last-name" id="last-name" autocomplete="off" />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <hr class="section-divider" />
          <div class="container new-section">
            <div class="row">
              <div class="col">
                <div class="row name-section justify-content-between">
                  <div class="col-1 section-icon">
                    <img src="../../assets/id-card.svg" alt="id-icon" class="id-icon" />
                  </div>
                  <div class="col-10 section-info">
                    <div class="section-info-container">
                      <div class="section-title">ID Number:</div>
                      <div class="section-data">21510</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <hr class="section-divider" />
          <div class="container new-section">
            <div class="row">
              <div class="col">
                <div class="row email-section justify-content-between">
                  <div class="col-1 section-icon">
                    <img src="../../assets/email.svg" alt="email-icon" class="email-icon" />
                  </div>
                  <div class="col-10 section-info">
                    <div class="section-info-container">
                      <div class="section-title">Email:</div>
                      <div class="section-data">severus.snape@hogwarts.com</div>
                      <div class="section-input-group">
                        <label for="last-name">Email:</label>
                        <input type="email" name="email" id="email" value="severus.snape@hogwarts.com" autocomplete="off" />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <hr class="section-divider" />
          <div class="container new-section">
            <div class="row">
              <div class="col">
                <div class="row mobile-section justify-content-between">
                  <div class="col-1 section-icon">
                    <img src="../../assets/mobile.svg" alt="mobile-icon" class="mobile-icon" />
                  </div>
                  <div class="col-10 section-info">
                    <div class="section-info-container">
                      <div class="section-title">Mobile:</div>
                      <!-- <div class="section-data">+91 9022054573</div> -->
                      <!-- <div class="section-input-group">
                        <label for="last-name">Mobile:</label>
                        <select name="country-codes" id="country-codes">
                          <option value="1">USA (+1)</option>
                          <option value="2">United Arab Emirates (+971)</option>
                          <option value="3">India (+91)</option>
                        </select>
                        <input type="tel" name="mobile" id="mobile" value="" autocomplete="off" />
                      </div> -->
                      <vue-tel-input :autoDefaultCountry="true" :dropdownOptions="{ showDialCodeInSelection: true, showDialCodeInList: true, showFlags: true }">
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
          <hr class="section-divider" />
          <div class="container new-section">
            <div class="row">
              <div class="col">
                <div class="row password-section justify-content-between">
                  <div class="col-1 section-icon">
                    <img src="../../assets/lock.svg" alt="password-icon" class="password-icon" />
                  </div>
                  <div class="col-10 section-info">
                    <div class="section-info-container">
                      <div class="section-title">Password:</div>
                      <div class="section-data">●●●●●●●●●●●●●●●●</div>
                      <div class="section-input-group">
                        <label for="last-name">Current Password:</label>
                        <input type="password" name="curr-pass" id="curr-pass" value="12345" autocomplete="off" />
                      </div>
                      <div class="section-input-group">
                        <label for="last-name">Confirm Password:</label>
                        <input type="password" name="cnfm-pass" id="cnfm-pass" value="12345" autocomplete="off" />
                      </div>
                      <div class="section-input-group">
                        <label for="last-name">New Password:</label>
                        <input type="password" name="new-pass" id="new-pass" value="12345" autocomplete="off" />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <hr class="section-divider" />
          <div class="container new-section">
            <div class="row">
              <div class="col">
                <div class="row gender-section justify-content-between">
                  <div class="col-1 section-icon">
                    <img src="../../assets/gender.svg" alt="gender-icon" class="gender-icon" />
                  </div>
                  <div class="col-10 section-info">
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
          <hr class="section-divider" />
          <div class="container new-section">
            <div class="row">
              <div class="col">
                <div class="row age-section justify-content-between">
                  <div class="col-1 section-icon">
                    <img src="../../assets/age.svg" alt="age-icon" class="age-icon" />
                  </div>
                  <div class="col-10 section-info">
                    <div class="section-info-container">
                      <div class="section-title">Age:</div>
                      <div class="section-data">47</div>
                      <div class="section-input-group">
                        <label for="age">Age:</label>
                        <input type="number" name="age" id="age" value="47" autocomplete="off" />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <hr class="section-divider" />
          <div class="container new-section">
            <div class="row">
              <div class="col">
                <div class="row doj-section justify-content-between">
                  <div class="col-1 section-icon">
                    <img src="../../assets/clock.svg" alt="clock-icon" class="clock-icon" />
                  </div>
                  <div class="col-10 section-info">
                    <div class="section-info-container">
                      <div class="section-title">Date of Joining:</div>
                      <div class="section-data">Sat, Jul 14, 2020</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <hr class="section-divider" />
        </div>
      </div>
      <div id="mask"></div>
    </div>
  </div>
</template>

<script>
import { VueTelInput } from 'vue-tel-input'

export default {
  name: 'SettingsMobile',
  components: {
    VueTelInput
  },
  data() {
    return {
      phone: null
    }
  },
  methods: {
    toggleActive(event) {
      // console.log(event.target)
      const elem = document.querySelector('.settings-outer-container')
      const midpoint = elem.clientWidth / 2
      document.querySelectorAll('.tab-item').forEach((tab) => {
        tab.classList.remove('active')
      })

      event.target.classList.add('active')

      if (event.target.innerText === 'ACCOUNT') {
        elem.scrollTo({ top: 0, left: midpoint + 10, behavior: 'smooth' })
      } else {
        elem.scrollTo({ top: 0, left: midpoint - 10, behavior: 'smooth' })
      }
    },
    scrollHandler(event) {
      const elem = event.target
      const width = document.querySelector('.settings-outer-container').clientWidth
      const left = elem.scrollLeft
      const leftPercent = (left / width) * 50
      const slider = document.querySelector('.slider')
      slider.style.left = `${leftPercent}%`
    }
  }
}
</script>
<style src="vue-tel-input/dist/vue-tel-input.css"></style>
<style lang="scss" scoped>
.header {
  // box-shadow: 0 3px 2px 0px rgba(0, 0, 0, 0.25);
  background: var(--primary-accent-dark);
  .logo {
    padding: 23px 23px 12px;
    .logo-text {
      margin-left: 15px;
      font-size: 18px;
      color: #fff;
    }
  }
  .settings-tabs {
    .tab-item {
      color: #fff;
      text-transform: uppercase;
      text-align: center;
      font-size: 0.9375rem;
      padding-top: 8px;
      padding-bottom: 8px;
      cursor: pointer;
    }
    .active {
      border-bottom: 3px solid #fff;
    }
  }
}

.settings-outer-container {
  overflow-x: auto;
  scrollbar-color: transparent;
  background: var(--background-primary);
  &::-webkit-scrollbar-thumb {
    background-color: transparent;
  }
  scroll-snap-type: x mandatory;
  .settings-inner-container {
    display: flex;
    flex-wrap: no-wrap;
    position: relative;
    width: 200%;
    // box-shadow: inset 0 3px 2px 0px rgba(0, 0, 0, 0.25);
    .settings-page {
      // box-shadow: inset 0 3px 2px 0px rgba(0, 0, 0, 0.25);
      // position: relative;
      scroll-snap-align: start;
      height: calc(100vh - 119px);
      overflow: auto;
      width: 100%;
      z-index: 0;
    }
  }
}

.new-section {
  padding: 0 25px;
}

.tabs {
  position: relative;
  ul {
    display: flex;
    list-style: none;
    justify-content: center;
    width: 100%;
    padding: 0;
    margin: 0;
    .tab-item {
      width: 100%;
      text-align: center;
      color: #fff;
      font-size: 0.9375rem;
      padding: 8px 0;
      text-transform: uppercase;
    }
  }
  .slider {
    position: absolute;
    background-color: #fff;
    width: 50%;
    height: 3px;
    bottom: 0;
    z-index: 5;
    // transition: left 0.2s linear;
  }
}

.tab-item:first-child.active ~ .slider {
  left: 0;
}
.tab-item:nth-child(2).active ~ .slider {
  left: 50%;
}

::v-deep .logo-svg {
  rect {
    fill: #fff;
  }
  path {
    stroke: var(--primary-accent-dark);
  }
}

.user-title-section {
  display: flex;
  margin-top: 30px;
  margin-bottom: 25px;
  .user-title {
    font-size: 1.5rem;
    display: flex;
  }
  .edit-icon {
    display: flex;
    align-self: center;
    margin-left: auto;
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
    margin-left: auto;
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

.section-divider {
  width: 80%;
  margin-left: auto;
  margin-top: 0.5rem;
  margin-bottom: 1.25rem;
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
      padding: 2px 7px;
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

.settings-group {
  padding: 5rem 1.5rem;
  .settings-group-item {
    display: flex;
    margin-bottom: 40px;
    align-items: center;
    .settings-group-option {
      margin-left: 1.62rem;
    }
    .settings-group-button {
      margin-left: auto;
      background: none;
      outline: none;
      box-shadow: none;
      border: none;
    }
  }
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
    input[name='gender-option'] {
      width: 40px;
      height: 40px;
      position: relative;
      display: flex;
      background: var(--light-gray);
      border-radius: 50%;
      appearance: none;
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

#mask {
  position: absolute;
  top: 119px;
  left: 0;
  width: 100%;
  height: calc(100vh - 119px);
  box-shadow: inset 0 3px 2px 0px rgb(0 0 0 / 25%);
  pointer-events: none;
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
</style>
