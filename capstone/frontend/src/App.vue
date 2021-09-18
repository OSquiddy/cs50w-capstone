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
    ...mapState(['isMobile', 'token', 'isAuthenticated'])
  },
  beforeCreate () {
    const token = this.token
    this.$store.commit('CHECK_TOKEN')

    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token ' + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  created () {
    // this.checkToken()
  },
  mounted () {
    this.onResize()
    window.addEventListener('resize', this.onResize, { passive: true })
    if (sessionStorage.getItem('isCollapsed') === 'true') {
      this.toggleCollapse()
    }
  },
  methods: {
    ...mapActions(['toggleCollapse', 'setMobileView', 'checkToken']),
    onResize () {
      const payload = window.innerWidth < 600
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
