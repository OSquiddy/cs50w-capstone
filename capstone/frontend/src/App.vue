<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <div class="custom-tooltip bottom-arrow" id="common-tooltip"></div>
    <router-view v-if="!isMobile"/>
    <router-view v-else name="mobile" />
  </div>
</template>
<script>
/* eslint-disable dot-notation */
import axios from 'axios'
import { mapActions, mapState } from 'vuex'
export default {
  data () {
    return {}
  },
  computed: {
    ...mapState(['isMobile', 'token', 'isAuthenticated', 'currentUser', 'patient'])
  },
  beforeCreate () {
    this.$store.commit('CHECK_TOKEN')
  },
  created () {
    // this.checkToken()
    if (localStorage.getItem('currentUser')) {
      const user = JSON.parse(localStorage.getItem('currentUser'))
      this.setCurrentUser(user)
    }
    if (sessionStorage.getItem('patient')) {
      const patient = JSON.parse(sessionStorage.getItem('patient'))
      this.$store.commit('GET_PATIENT_INFO', patient)
    }
  },
  mounted () {
    const token = this.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token ' + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
    this.onResize()
    window.addEventListener('resize', this.onResize, { passive: true })
    if (sessionStorage.getItem('isCollapsed') === 'true') {
      this.toggleCollapse()
    }
  },
  methods: {
    ...mapActions(['toggleCollapse', 'setMobileView', 'checkToken', 'setCurrentUser']),
    onResize () {
      const payload = window.innerWidth < 1200
      this.setMobileView(payload)
    }
  },
  beforeDestroy () {
    if (typeof window !== 'undefined') {
      window.removeEventListener('resize', this.onResize, { passive: true })
    }
  }
}
</script>
<style lang="scss" src="./App.scss" />
