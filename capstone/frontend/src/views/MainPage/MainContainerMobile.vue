<template>
  <div class="overview-main height">
    <div class="grid-container" v-if="!overviewMenu">
      <div class="grid-item" @click="toggleOverviewMenu">
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
      <div class="container-fluid">
        <div class="overview-heading">
          OVERVIEW
          <!-- <span @click="toggleOverviewMenu">Back</span> -->
        </div>
        <ul class="chart-menu">
          <li class="overview-menu-item" :class="chart === 0 && 'active'" @click="setChart(0)">Monthly</li>
          <li class="overview-menu-item" :class="chart === 1 && 'active'" @click="setChart(1)">Total</li>
          <li class="overview-menu-item" :class="chart === 2 && 'active'" @click="setChart(2)">Patients</li>
          <!-- <li class="overview-menu-item" :class="chart === 3 && 'active'" @click="setChart(3)">Appointments</li> -->
        </ul>
        <div class="tile" v-if="chart === 0">
          <div class="barchart chart-container">
            <EarningsBarChart />
          </div>
        </div>
        <div class="tile" v-if="chart === 1">
          <div class="linechart chart-container">
            <EarningsLineChart />
          </div>
        </div>
        <div class="tile" v-if="chart === 2">
          <div class="container-fluid h-100">
            <div class="row h-100">
              <div class="col-12 p-0 h-100">
                <div class="chart-container">
                  <div class="patient-breakdown-chart">
                    <DonutChart :data="donutData" />
                  </div>
                  <div class="row">
                    <div class="d-contents d-md-none">
                      <div class="col-12">
                        <table class="patient-dist-table">
                          <thead>
                            <tr>
                              <!-- <td>Patient Type</td>
                              <td>Info</td> -->
                              <td colspan="2"> Patient Distribution</td>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td>Males</td>
                              <td>{{malesPercent}} %</td>
                            </tr>
                            <tr>
                              <td>Females</td>
                              <td>{{femalesPercent}} %</td>
                            </tr>
                            <tr>
                              <td>Others</td>
                              <td>{{othersPercent}} %</td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                      <div class="col-12">
                        <table class="appt-dist-table">
                            <thead>
                              <tr>
                                <!-- <td>Patient Type</td>
                                <td>Info</td> -->
                                <td colspan="2"> Appointment Distribution</td>
                              </tr>
                            </thead>
                            <tbody>
                              <tr>
                                <td>Males</td>
                                <td>{{apptMalesPercent}} %</td>
                              </tr>
                              <tr>
                                <td>Females</td>
                                <td>{{apptFemalesPercent}} %</td>
                              </tr>
                              <tr>
                                <td>Others</td>
                                <td>{{apptOthersPercent}} %</td>
                              </tr>
                            </tbody>
                          </table>
                      </div>
                    </div>
                    <div class="d-none d-md-contents">
                      <div class="col-12">
                        <table class="patient-dist-table">
                          <thead>
                            <tr>
                              <!-- <td>Patient Type</td>
                              <td>Info</td> -->
                              <!-- <td colspan="2"> Patient Distribution</td> -->
                              <td>Type</td>
                              <td>Patient Distribution</td>
                              <td>Appointment Distribution</td>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td>Males</td>
                              <td>{{malesPercent}} %</td>
                              <td>{{apptMalesPercent}} %</td>
                            </tr>
                            <tr>
                              <td>Females</td>
                              <td>{{femalesPercent}} %</td>
                              <td>{{apptFemalesPercent}} %</td>
                            </tr>
                            <tr>
                              <td>Others</td>
                              <td>{{othersPercent}} %</td>
                              <td>{{apptOthersPercent}} %</td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- <div class="tile" v-if="chart === 3">
          <div>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Possimus eius vitae ipsa harum eum veritatis officiis tempora dolore illo modi quisquam labore, aperiam cumque explicabo animi! Dignissimos corporis quaerat consequuntur!</div>
          <br>
          <div>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Possimus eius vitae ipsa harum eum veritatis officiis tempora dolore illo modi quisquam labore, aperiam cumque explicabo animi! Dignissimos corporis quaerat consequuntur!</div>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import EarningsBarChart from '../../components/EarningsBarChart.vue'
import EarningsLineChart from '../../components/EarningsLineChart.vue'
import DonutChart from '../../components/DonutChart.vue'
import axios from 'axios'
import { mapActions, mapState } from 'vuex'
export default {
  components: { EarningsBarChart, EarningsLineChart, DonutChart },
  name: 'MainContainerMobile',
  data() {
    return {
      chart: 0,
      appointmentsData: null
    }
  },
  computed: {
    ...mapState(['overviewMenu']),
    donutData () {
      if (this.numPatients) {
        const obj = {}
        obj.Male = this.numPatients.male
        obj.Female = this.numPatients.female
        obj.Other = this.numPatients.other
        return obj
      }
      return null
    },
    malesPercent () {
      return (this.numPatients.male / (this.numPatients.male + this.numPatients.female + this.numPatients.other) * 100).toFixed(2)
    },
    femalesPercent () {
      return (this.numPatients.female / (this.numPatients.male + this.numPatients.female + this.numPatients.other) * 100).toFixed(2)
    },
    othersPercent () {
      return (this.numPatients.other / (this.numPatients.male + this.numPatients.female + this.numPatients.other) * 100).toFixed(2)
    },
    apptMalesPercent () {
      return (this.appointmentsData.Males.length / (this.appointmentsData.Males.length + this.appointmentsData.Females.length + this.appointmentsData.Others.length) * 100).toFixed(2)
    },
    apptFemalesPercent () {
      return (this.appointmentsData.Females.length / (this.appointmentsData.Males.length + this.appointmentsData.Females.length + this.appointmentsData.Others.length) * 100).toFixed(2)
    },
    apptOthersPercent () {
      return (this.appointmentsData.Others.length / (this.appointmentsData.Males.length + this.appointmentsData.Females.length + this.appointmentsData.Others.length) * 100).toFixed(2)
    }
  },
  created () {
    this.getTotalPatients()
    this.getAppointmentData()
  },
  methods: {
    ...mapActions(['removeToken', 'toggleOverviewMenu']),
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
    },
    async getTotalPatients () {
      const list = await axios.get(process.env.VUE_APP_API_URL + '/numPatients')
      this.numPatients = list.data.numPatients
    },
    async getAppointmentData () {
      const list = await axios.get(process.env.VUE_APP_API_URL + '/getAppointments')
      this.appointmentsData = list.data.appointments
    },
    setChart (index) {
      this.chart = index
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
  min-height: var(--height);
}

.overview-heading {
  margin-top: 15px;
}

.donut-legend {
  background-color: black;
  width: 5px;
  height: 5px;
}

.d-contents, .d-sm-contents, .d-md-contents, .d-lg-contents, .d-xl-contents {
  display: contents;
}

:where(.patient-dist-table, .appt-dist-table) {
  border: 1px solid #ccc;
  margin: 0 auto 20px;
  width: 100%;
  thead tr {
    background-color: var(--primary-accent-light);
    td {
      color: var(--background-primary);
    }
  }
  td {
    border: 1px solid #ccc;
    padding: 10px 15px;
  }
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
  // height: calc(var(--height) - 40px);
  // height: calc(var(--height) / 1.5);
  min-height: calc(var(--height) / 1.5);
  background: var(--background-primary);
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  // box-shadow: 0 0 3px 0 rgba(0, 0, 0, 0.2);
  border: 1px solid #ccc;
  padding: 20px;
  margin: -2px 3px 25px;
  overflow-x: auto;
}

.linechart {
  min-width: 700px;
  display: flex;
  margin-left: auto;
  height: 100%;
}

.patient-breakdown-chart {
  width: 100%;
  height: 75%;
}

.chart-container {
  height: calc(var(--height) / 1.5);
  width: 100%;
}

.chart-menu {
  display: flex;
  list-style: none;
  padding: 5px 0 0 3px;
  margin: 10px 0 0;
  overflow-x: auto;
  .overview-menu-item {
    // margin-right: 5px;
    // border: 1px solid;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    padding: 10px 10px;
    font-size: 0.875rem;
    z-index: 2;
  }
  .active {
    background: var(--background-primary);
    color: var(--primary-accent-dark);
    font-weight: 500;
    border: 1px solid #ccc;
    // border-top: 2px solid var(--primary-accent-dark);
    border-bottom: 2px solid white;
    // box-shadow: 0 -2px 3px 0 rgba(0, 0, 0, 0.2);
  }
}

@media screen and (min-width: 576px) {
  .d-sm-contents {
    display: contents;
  }
}

@media screen and (min-width: 768px) {
  .d-md-contents {
    display: contents !important;
  }

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

@media screen and (min-width: 992px) {
  .d-lg-contents {
    display: contents;
  }
}

@media screen and (min-width: 1200px) {
  .d-xl-contents {
    display: contents;
  }
}
</style>
