<template>
  <div class="background-main">
    <div class="sidepanel-wrapper d-flex h-100 flex-three">
      <div class="sidepanel">
        <div class="logo">
          <router-link to="/">
            <img src="../../src/assets/avicennaLogo.svg" alt="Logo" />
            <span class="logo-text">Avicenna Hospital</span>
          </router-link>
        </div>
        <ul class="menu my-4">
          <router-link to="/">
            <li class="menu-item">Overview</li>
          </router-link>
          <router-link to="/directory">
            <li class="menu-item">Patients</li>
          </router-link>
          <router-link to="/appointments">
            <li class="menu-item">Appointments</li>
          </router-link>
          <router-link to="/settings">
            <li class="menu-item">Settings</li>
          </router-link>
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
        <div class="padding-sides" :class="patientHeader ?'change-height' : ''">
          <router-view />
        </div>
        <div id="mask" :class="patientHeader ?'change-height' : ''"></div>
      </div>
    </div>
  </div>
</template>

<script>
import PatientHeader from './PatientHeader.vue'
export default {
  name: 'Layout',
  components: { PatientHeader },
  data() {
    return {
      patientHeaderRoutes: ['add-appointment']
    }
  },
  computed: {
    patientHeader() {
      return this.patientHeaderRoutes.includes(this.$route.name)
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
  .menu-item {
    color: #c4c4c4;
    margin-bottom: 1.25rem;
    &:hover {
      color: white;
      cursor: pointer;
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
      padding: 15px;
      width: 100%;
      .user-options {
        margin-left: auto;
        display: flex;
        align-items: center;
        .header-profile-pic {
          width: 40px;
          height: 40px;
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

.sidepanel {
  background: #1a1a1a;
  width: 270px;
  height: inherit;
  .logo {
    padding: 23px 23px 12px;
    .logo-text {
      margin-left: 15px;
      font-size: 18px;
      color: #fff;
    }
  }
}

.padding-sides {
  padding: 0px 20px 0px;
  overflow: auto;
  height: calc(100vh - 70px);
}

#mask {
  position: absolute;
  top: 70px;
  right: 0;
  width: calc(100% - 270px);
  height: calc(100vh - 70px);
  box-shadow: inset 0 1px 8px 0px rgb(0 0 0 / 25%);
  pointer-events: none;
}

.change-height {
  height: calc(100% - 191px);
}
</style>
