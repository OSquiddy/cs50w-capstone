<template>
  <div class="overview-main height">
    <div class="grid-container" v-if="menu">
      <div class="grid-item" @click="toggleMenu">
        <div class="grid-item-img">
          <img src="../../assets/undraw/undraw_progress_overview_red.svg" alt="overwiew-icon">
        </div>
        <div class="grid-item-text">Overview</div>
      </div>
      <router-link to="/appointments">
        <div class="grid-item">
          <div class="grid-item-img">
            <img src="../../assets/undraw/undraw_online_calendar_blue.svg" alt="overwiew-icon">
          </div>
          <div class="grid-item-text">Appointments</div>
        </div>
      </router-link>
      <router-link to="/directory">
      <div class="grid-item">
        <div class="grid-item-img">
          <img src="../../assets/undraw/undraw_folder_files_red.svg" alt="overwiew-icon">
        </div>
        <div class="grid-item-text">Patient Directory</div>
      </div>
      </router-link>
      <router-link to="/settings">
      <div class="grid-item">
        <div class="grid-item-img">
          <img src="../../assets/undraw/undraw_personal_settings_blue.svg" alt="overwiew-icon">
        </div>
        <div class="grid-item-text">Settings</div>
      </div>
      </router-link>
      <div class="grid-item" @click="logout">
        <div class="grid-item-img">
          <img src="../../assets/undraw/undraw_login_blue.svg" alt="overwiew-icon">
        </div>
        <div class="grid-item-text">Logout</div>
      </div>
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
  mounted () {

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
.overview-main {
  background: var(--lightest-gray);
  border: 1px solid transparent;
  height: 100%;
}

.height {
  height: var(--height);
}

.grid-container {
  margin-top: 30px;
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
    background: #fff;
    height: 145px;
    box-shadow: 0 3px 3px 0px rgba(0, 0, 0, 0.2);
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow: hidden;
    .grid-item-img {
      width: 100%;
      height: 75%;
      // border: 1px solid green;
      display: flex;
      align-items: center;
      justify-content: center;
      img {
        width: inherit;
        object-fit: contain;
        height: inherit;
      }
    }
    .grid-item-text {
      // justify-content: center;
      width: 100%;
      text-align: center;
      margin-top: auto;
      padding: 5px 0;
      // border: 1px solid;
    }
  }
}

.tile {
  height: 150px;
}

@media screen and (min-width: 768px) {
  .grid-container {
    padding: 10px 50px;
    grid-template-columns: repeat(auto-fill, 40%);
    grid-gap: 30px;
    .grid-item {
      display: flex;
      height: 250px;
      padding: 15px;
      .grid-item-img {
        padding: 0 20px;
        background: #fff;
        img {
          width: 150px;
          object-fit: contain;
        }
      }
    }
  }
}
</style>
