<template>
  <div class="main">
    <div class="header" :class="[searchURL ? 'sticky-top container-shadow': '']" v-if="displayHeader">
      <div class="logo">
        <router-link to="/">
          <img src="../../src/assets/avicennaLogo.svg" alt="Logo" />
          <span class="logo-text">Avicenna Hospital</span>
        </router-link>
      </div>
      <SearchContainer v-if="searchURL" :searchHeader="searchURL" />
    </div>
    <div class="wrapper">
      <router-view name="mobile"/>
      <div id="mask"></div>
    </div>
  </div>
</template>

<script>
import SearchContainer from './SearchContainer.vue'

export default {
  name: 'LayoutMobile',
  components: {
    SearchContainer
  },
  data() {
    return {
    }
  },
  computed: {
    searchURL () {
      if (this.$route.name === 'appointments') {
        const search = this.$route.name
        return search.charAt(0).toUpperCase() + search.substring(1)
      } else if (this.$route.name === 'directory') {
        return 'Patient Directory'
      }
      return null
    },
    displayHeader () {
      if (this.$route.name === 'settings' || this.$route.name === 'add-patient' || this.$route.name === 'add-appointment') {
        return false
      }
      return true
    }
  },
  methods: {
    async getUsername() {
      //   const user = await apiService.getUsers()
      //   this.username = user.username
    }
  }
}
</script>

<style lang="scss" scoped>
.header {
  background: #fff;
  box-shadow: 0 1px 3px 0px rgba(0, 0, 0, 0.2);
  // margin-bottom: 30px;
  .logo {
    padding: 23px 23px 12px;
    .logo-text {
      margin-left: 15px;
      font-size: 18px;
    }
  }
}

// .main {
//   // overflow: hidden;
// }

.container-shadow {
  box-shadow: 0 1px 3px 0px rgba(0,0,0,0.2);
}

#mask {
  pointer-events: none;
  width: 100%;
  box-shadow: inset 0 1px 3px 0px rgba(0,0,0,0.25);
}
</style>
