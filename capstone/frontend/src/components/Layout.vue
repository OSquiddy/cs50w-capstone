<template>
  <div class="background-main">
    <div class="sidepanel-wrapper d-flex h-100 flex-three">
      <div class="sidepanel"  :class="[isCollapsed ? 'isCollapsed' : '']">
        <div class="container-fluid">
          <div class="row">
            <div class="logo">
            <img src="../../src/assets/avicennaLogo.svg" alt="Logo" />
            <button class="toggle" @click="toggleCollapse" v-if="isCollapsed">
              <img src="../assets/doubleChevron.svg" alt="toggle-collapse">
            </button>
            <span class="logo-text" :class="isCollapsed ? 'hide' : ''">Avicenna Hospital</span>
          <button class="toggle" @click="toggleCollapse" v-if="!isCollapsed">
            <img src="../assets/doubleChevron.svg" alt="toggle-collapse" class="mirror">
          </button>
        </div>
          </div>
        </div>
          <ul class="menu my-4" :class="[isCollapsed ? 'font-small' : '']">
            <router-link to="/">
              <li class="menu-item" @click="selectTab(0)" :class="selectedTab == 0 ? 'active' : ''">
                <img src="../../src/assets/overview.svg" svg-inline alt="main-page" class="menu-icon"/>
                <span class="menu-item-text">Overview</span>
              </li>
            </router-link>
            <router-link to="/directory">
              <li class="menu-item" @click="selectTab(1)" :class="selectedTab == 1 || patientHeader ? 'active' : ''">
                <img src="../../src/assets/patientsDesktop.svg" svg-inline alt="patients-page" class="menu-icon"/>
                <span class="menu-item-text">Patients</span>
              </li>
            </router-link>
            <router-link to="/appointments">
              <li class="menu-item" @click="selectTab(2)" :class="selectedTab == 2 ? 'active' : ''">
                <img src="../../src/assets/calendar.svg" svg-inline alt="appointments-page" class="menu-icon"/>
                <span class="menu-item-text">Appointments</span>
              </li>
            </router-link>
            <router-link to="/settings">
              <li class="menu-item" @click="selectTab(3)" :class="selectedTab == 3 ? 'active' : ''">
                <img src="../../src/assets/settings.svg" svg-inline alt="settings-page" class="menu-icon"/>
                <span class="menu-item-text">Settings</span>
              </li>
            </router-link>
            <li class="menu-item mt-auto" @click="logout">
              <img src="../../src/assets/logout.svg" alt="logout" class="menu-icon" />
              <span class="menu-item-text">Logout</span>
            </li>
          </ul>
        </div>
    </div>
    <div class="main-view-wrapper flex-seven">
      <header>
        <router-link :to="{name: 'add-appointment' }" class="button-link">
          <button class="add-button">
            <img src="../assets/add-appointment.svg" class="button-logo" alt="new-appointment-logo">
            <div class="add-button-text">New Appointment</div>
          </button>
        </router-link>
        <router-link :to="{name: 'add-patient' }" class="button-link">
          <button class="add-button">
            <img src="../assets/add-patient.svg" class="button-logo" alt="new-patient-logo">
            <div class="add-button-text">New Patient</div>
          </button>
        </router-link>
        <div class="user-options">
          <div class="header-profile-pic"></div>
          <div class="header-username">{{currentUser.fullname}}</div>
        </div>
      </header>
      <template v-if="patientHeader">
        <PatientHeader/>
        <LocalTabs />
      </template>
      <div class="main-view">
        <div class="padding-sides" :class="[patientHeader ?'change-height' : '']">
          <router-view />
        </div>
        <div class="mask" :class="[patientHeader ? 'change-height' : '', isCollapsed ? 'change-width' : '']"></div>
        <div class="toast-container" ></div>
      </div>
    </div>
  </div>
</template>

<script>
import PatientHeader from './PatientHeader.vue'
import LocalTabs from '../components/LocalTabs.vue'
import { mapState, mapActions } from 'vuex'
import axios from 'axios'
export default {
  name: 'Layout',
  components: { PatientHeader, LocalTabs },
  data() {
    return {
      pageNames: ['mainPage', 'directory', 'appointments', 'settings'],
      selectedTab: null
    }
  },
  computed: {
    ...mapState(['isCollapsed', 'patient', 'currentUser']),
    patientHeader() {
      return this.$route.matched.some(({ name }) => name === 'patient-main')
    }
  },
  watch: {
    patientHeader(newValue, oldValue) {
      if (this.patientHeader) {
        const patientID = this.$route.path.split('/')[2]
        this.getPatientInfo(patientID)
      }
    },
    '$route.path' () {
      this.setTab()
    }
  },
  mounted () {
    this.setTab()
    if (this.patientHeader) {
      const patientID = this.$route.path.split('/')[2]
      this.getPatientInfo(patientID)
    }
  },
  methods: {
    ...mapActions(['toggleCollapse', 'getPatientInfo', 'removeToken']),
    selectTab (tabIndex) {
      this.selectedTab = tabIndex
    },
    setTab () {
      if (this.pageNames.indexOf(this.$route.name) !== -1) {
        this.selectedTab = this.pageNames.indexOf(this.$route.name)
      }
    },
    async logout () {
      // console.log(axios.defaults.headers.common)
      await axios.post(process.env.VUE_APP_API_URL + '/token/logout')
      axios.defaults.headers.common.Authorization = ''
      // console.log(axios.defaults.headers.common)

      localStorage.removeItem('token')
      localStorage.setItem('isAuthenticated', false)
      this.removeToken()

      this.$router.push('/login')
    }
  }
}
</script>

<style lang="scss" scoped>
.background-main {
  height: 100vh;
  overflow: hidden;
  display: flex;
}
::v-deep .menu {
  list-style-type: none;
  color: #c4c4c4;
  margin-left: 30px;
  display: flex;
  flex-direction: column;
  height: 82.5%;
  .menu-item {
    .menu-item-text {
      text-align: left;
      transition: font-size 0.3s ease-out;
      color: #c4c4c4;
    }
    img, svg {
      display: none;
      margin: 0 auto;
      outline: none;
    }
    padding-bottom: 1.25rem;
    &:hover {
      .menu-item-text {
        color: white;
      }
      cursor: pointer;
      .menu-icon{
        // filter: brightness(100) saturate(100%);
        * {
          fill: white;
        }
      }
    }
  }
  .active{
    color: white;
    * {
      fill: white;
    }
    .menu-item-text {
      color: white;
    }
  }
}

.font-small {
  padding: 0;
  margin: 0;
  margin-top: 45px !important;
  .menu-item {
    text-align: center;
    .menu-item-text{
      display: none;
      font-size: 0.625rem;
    }
    img, svg {
      display: block;
      margin-bottom: 5px;
      width: 25px;
    }
  }
}

.main-view-wrapper {
  background: var(--background);
  width: 100%;
  header {
      // height: 70px;
      display: flex;
      background: white;
      padding: 9px 15px;
      width: 100%;
      z-index: 5;
      .user-options {
        margin-left: auto;
        display: flex;
        align-items: center;
        .header-profile-pic {
          width: 35px;
          height: 35px;
          background: var(--medium-gray);
          border-radius: 50%;
          margin-right: 0.625rem;
        }
      }
      .button-link {
        display: flex;
        .add-button {
          display: flex;
          border: none;
          padding: 0 10px;
          background-color: #2785FF;
          background-color: var(--primary-accent-light);
          border-radius: 50px;
          width: max-content;
          align-items: center;
          margin-right: 10px;
          .add-button-text {
            // border: 1px solid yellow;
            color: #FFFFFF;
            width: 100%;
            margin: 0 10px;
            font-size: 0.875rem;
          }
        }
      }
    }
  .main-view {
    width: 100%;
    overflow-y: auto;
    height: 100vh;
    .toast-container {
      width: fit-content !important;
      position: absolute;
      right: 15px;
      bottom: 15px;
    }
  }
}

::v-deep .button-logo {
  display: flex;
  filter: invert(100);
  fill: white;
}

.sidepanel-wrapper {
  transition: 0.3s ease-out;
  // width: 270px;
}
.sidepanel {
  background: #1a1a1a;
  width: 270px;
  transition: 0.3s ease-out;
  height: inherit;
  .logo {
    padding: 23px 0px 12px 15px;
    min-width: 270px;
    img {
      width: 35px;
      object-fit: contain;
    }
    .logo-text {
      margin-left: 12px;
      font-size: 18px;
      color: #fff;
      transition: 0.3s ease-out;
    }
    .hide {
      opacity: 0;
      pointer-events: none;
    }
  }
  .toggle {
    background: transparent;
    outline: none;
    border: none;
    box-shadow: none;
    width: fit-content;
    margin: 0 auto;
    img {
      width: 14px;
      object-fit: contain;
    }
  }
}

.padding-sides {
  padding: 0px 20px 0px;
  overflow: auto;
  height: calc(100vh - 70px);
}

.mask {
  position: absolute;
  top: 53px;
  right: 0;
  width: calc(100% - 270px);
  height: calc(100vh - 53px);
  box-shadow: inset 0 1px 8px 0px rgb(0 0 0 / 25%);
  transition: width 0.3s ease-out;
  pointer-events: none;
}

.change-width {
  width: calc(100% - 85px);
}

.change-height {
  height: calc(100% - 218px);
  top: 218px;
}

.isCollapsed {
  width: 85px;
}

</style>
