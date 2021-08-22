<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <router-view v-if="!$store.state.isMobile"/>
    <router-view v-else name="mobile" />
  </div>
</template>
<script>
export default {
  data () {
    return {
      isMobile: false
    }
  },
  mounted () {
    this.onResize()
    window.addEventListener('resize', this.onResize, { passive: true })
  },
  methods: {
    onResize () {
      this.$store.state.isMobile = window.innerWidth < 600
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
