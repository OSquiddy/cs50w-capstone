<template>
  <div>
    <div class="grid-container" v-if="menu">
      <div class="grid-item" @click="toggleMenu">Overview</div>
      <router-link to="/appointments">
        <div class="grid-item">Appointments</div>
      </router-link>
      <router-link to="/directory">
      <div class="grid-item">Patient Directory</div>
      </router-link>
      <router-link to="/settings">
      <div class="grid-item">Settings</div>
      </router-link>
      <div class="grid-item">Dev Support</div>
    </div>
    <div v-else>
      Overview Section <span @click="toggleMenu"> Back </span>
      <div class="total-earnings tile">
        <div class="total-earnings-header">
          <img src="../../assets/income.svg" alt="income-icon">
          Earnings
        </div>
        <BarChart />
      </div>
        <div class="earnings tile">
          <div class="earnings-header">Total Earnings</div>
          <EarningsChart />
        </div>
    </div>
  </div>
</template>

<script>
import BarChart from '../../components/EarningsBarChart.vue'
import EarningsChart from '../../components/EarningsLineChart.vue'
export default {
  components: { BarChart, EarningsChart },
  name: 'MainContainerMobile',
  data() {
    return {
      menu: true
    }
  },
  methods: {
    toggleMenu () {
      this.menu = !this.menu
    }
  }
}
</script>

<style lang="scss" scoped>
.grid-container {
  display: grid;
  justify-content: center;
  grid-template-columns: repeat(auto-fill, 145px);
  grid-gap: 18px;
  a {
    text-decoration: none;
    color: var(--primary-text-color);
  }
  .grid-item {
    background: #c4c4c4;
    height: 145px;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}

.tile {
  height: 150px;
}
</style>
