<template>
  <div class="main">
    <div class="header" :class="[searchURL ? 'sticky-top container-shadow': '']">
      <div class="logo">
        <router-link to="/">
          <img src="../../src/assets/avicennaLogo.svg" alt="Logo" />
          <span class="logo-text">Avicenna Hospital</span>
        </router-link>
      </div>
      <SearchContainer v-if="searchURL" :searchHeader="searchURL" />
    </div>
    <div class="wrapper">
      <router-view />
      <div id="mask"></div>
    </div>
  </div>
</template>

<script>
import SearchContainer from './SearchContainer.vue'

export default {
  name: 'Layout',
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
  .logo {
    padding: 23px 23px 12px;
    .logo-text {
      margin-left: 15px;
      font-size: 18px;
    }
  }
}

.container-shadow {
  box-shadow: 0 1px 3px 0px rgba(0,0,0,0.2);
}

#mask {
  pointer-events: none;
  width: 100%;
  box-shadow: inset 0 1px 3px 0px rgba(0,0,0,0.25);
}
</style>
