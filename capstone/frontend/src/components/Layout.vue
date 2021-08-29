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
              <li class="menu-item" @click="selectTab(0)">
                <img src="../../src/assets/overview.svg" alt="main-page" class="menu-icon"/>
                <span class="menu-item-text">Overview</span>
              </li>
            </router-link>
            <router-link to="/directory">
              <li class="menu-item" @click="selectTab(1)">
                <img src="../../src/assets/patientsDesktop.svg" alt="patients-page" class="menu-icon"/>
                <span class="menu-item-text">Patients</span>
              </li>
            </router-link>
            <router-link to="/appointments">
              <li class="menu-item" @click="selectTab(2)">
                <img src="../../src/assets/calendar.svg" alt="appointments-page" class="menu-icon"/>
                <span class="menu-item-text">Appointments</span>
              </li>
            </router-link>
            <router-link to="/settings">
              <li class="menu-item" @click="selectTab(3)">
                <img src="../../src/assets/settings.svg" alt="settings-page" class="menu-icon"/>
                <span class="menu-item-text">Settings</span>
              </li>
            </router-link>
            <li class="menu-item mt-auto">
              <img src="../../src/assets/logout.svg" alt="logout" class="menu-icon" />
              <span class="menu-item-text">Logout</span>
            </li>
          </ul>
        </div>
    </div>
    <div class="main-view-wrapper flex-seven">
      <header>
        <div class="user-options">
          <div class="header-profile-pic"></div>
          <div class="header-username">John Doe</div>
        </div>
      </header>
      <PatientHeader v-if="patientHeader"/>
      <div class="main-view">
        <div class="padding-sides" :class="[patientHeader ?'change-height' : '']">
          <router-view />
        </div>
        <div class="mask" :class="[patientHeader ? 'change-height' : '', isCollapsed ? 'change-width' : '']"></div>
      </div>
    </div>
  </div>
</template>

<script>
import PatientHeader from './PatientHeader.vue'
import { mapState, mapActions } from 'vuex'
export default {
  name: 'Layout',
  components: { PatientHeader },
  data() {
    return {
      patientHeaderRoutes: ['add-appointment']
    }
  },
  computed: {
    ...mapState(['isCollapsed', 'selectedTab']),
    patientHeader() {
      return this.patientHeaderRoutes.includes(this.$route.name)
    }
  },
  mounted () {
    this.setTab()
    if (sessionStorage.getItem('selectedTab')) {
      this.selectTab(sessionStorage.getItem('selectedTab'))
    }
    if (sessionStorage.getItem('isCollapsed') === 'true') {
      this.toggleCollapse()
    }
  },
  methods: {
    ...mapActions(['toggleCollapse', 'updateSelectedTab']),
    selectTab (tabIndex) {
      const tabs = document.querySelectorAll('.menu-item')
      tabs[this.selectedTab].classList.remove('active')
      tabs[tabIndex].classList.add('active')
      this.updateSelectedTab(tabIndex)
    },
    setTab () {
      const tabs = document.querySelectorAll('.menu-item')
      tabs[this.selectedTab].classList.add('active')
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
.menu {
  list-style-type: none;
  color: #c4c4c4;
  margin-left: 30px;
  display: flex;
  flex-direction: column;
  height: 82.5%;
  .menu-item {
    // font-size: 0.875rem;
    .menu-item-text {
      text-align: left;
      transition: font-size 0.3s ease-out;
      color: #c4c4c4;
    }
    img {
      display: none;
      margin: 0 auto;
      // margin-left: 30px;
      // opacity: 0;
      // transition: opacity 0.3s ease-out;
    }
    margin-bottom: 1.25rem;
    &:hover {
      .menu-item-text {
        color: white;
      }
      cursor: pointer;
      .menu-icon{
        filter: brightness(100) saturate(100%);
      }
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
      // display: none;
      font-size: 0.625rem;
    }
    img {
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
    }
  .main-view {
    width: 100%;
    overflow-y: auto;
    height: 100vh;
  }
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
  transition: 0.3s ease-out;
  pointer-events: none;
}

.change-width {
  width: calc(100% - 85px);
}

.change-height {
  height: calc(100% - 175px);
  top: 175px;
}

.isCollapsed {
  width: 85px;
}

.active {
  color: white;
  filter: brightness(100) saturate(100%);
}
</style>
