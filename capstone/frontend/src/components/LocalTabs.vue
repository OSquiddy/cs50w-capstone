<template>
  <div class="local-tabs-container">
    <ul class="tablist">
      <li class="tab active" @click="selectTab(0, $event)">Overview</li>
      <li class="tab" @click="selectTab(1, $event)">History</li>
      <li class="tab" @click="selectTab(2, $event)">Reports</li>
      <!-- <li class="tab" @click="selectTab(3, $event)">Notes</li> -->
    </ul>
  </div>
</template>

<script>
export default {
  name: 'LocalTabs',
  data () {
    return {
      selectedTab: 0,
      tabPaths: ['overview', 'history', 'reports', 'notes']
    }
  },
  watch: {
    selectedTab (newValue, oldValue) {
      if (this.$route.name !== this.tabPaths[newValue]) {
        this.$router.push({ name: this.tabPaths[newValue] })
      }
      document.querySelectorAll('.tab')[oldValue].classList.remove('active')
    },
    '$route.path' () {
      this.setTab()
    }
  },
  mounted () {
    this.setTab()
  },
  methods: {
    selectTab (index, event) {
      this.selectedTab = index
      // const elem = event.target
      // elem.classList.add('active')
    },
    setTab () {
      const index = this.tabPaths.findIndex((elem) => {
        return elem === this.$route.name
      })
      this.selectedTab = index
      document.querySelectorAll('.tab')[index].classList.add('active')
    }
  }
}
</script>

<style lang="scss" scoped>
.local-tabs-container {
  display: flex;
  background: white;
}

.tablist {
  display: flex;
  list-style-type: none;
  margin: 0;
  padding: 0;
  .tab {
    margin: 0 1.5rem;
    padding: 0.5rem 0;
    // border: 1px solid;
    cursor: pointer;
  }
}

.active {
  color: var(--focus-blue);
  border-bottom: 4px solid var(--focus-blue);
}
</style>
