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
      <div class="grid-item" @click="logout">Logout</div>
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
import axios from 'axios'
import { mapActions } from 'vuex'
export default {
  components: { BarChart, EarningsChart },
  name: 'MainContainerMobile',
  data() {
    return {
      menu: true
    }
  },
  methods: {
    ...mapActions(['removeToken']),
    toggleMenu () {
      this.menu = !this.menu
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

@media screen and (min-width: 768px) {
  .grid-container {
    // display: flex;
    // flex-direction: column;
    padding: 10px 50px;
    grid-template-columns: 100%;
    grid-gap: 30px;
    .grid-item {
      display: flex;
    }
  }
}
</style>
