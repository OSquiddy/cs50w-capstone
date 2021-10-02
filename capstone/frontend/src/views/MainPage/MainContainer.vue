<template>
  <div class="main-container">
    <div class="container-fluid">
      <div class="row">
        <div class="col">
          <div class="row h-100">
            <div class="col-8">
              <div class="row tiles-container">
                <div class="col">
                  <div class="greeting-section tile">
                  <div class="greeting">Hello, <span class="doctor-name">{{currentUser.fullname}}</span></div>
                  <div class="greeting-text">Have a nice day and don't forget to take care of your health!</div>
                  <div class="greetings-img">
                    <img src="../../assets/greetingsBg.svg" alt="greetings-img">
                  </div>
                  </div>
                </div>
              </div>
              <div class="row tiles-container">
                <div class="col-4">
                  <div class="num-patients tile">
                    <div class="num-patients-header">
                      <img src="../../assets/patientsDesktop.svg" class="tile-small-logo" alt="patient-logo">
                      Patients
                    </div>
                    <div class="num-patients-body tile-body">
                      {{numPatients}}
                    </div>
                  </div>
                </div>
                <div class="col-4">
                  <div class="num-appts tile">
                    <div class="num-appts-header">
                      <img src="../../assets/patient.svg" class="tile-small-logo num-appts-logo" alt="patient-logo">
                      Appointments
                    </div>
                    <div class="num-appts-body tile-body">
                      124
                    </div>
                  </div>
                </div>
                <div class="col-4">
                  <div class="total-earnings tile">
                    <div class="total-earnings-header">
                      <img src="../../assets/income.svg" alt="income-icon">
                      Earnings
                    </div>
                    <BarChart />
                  </div>
                </div>
              </div>
              <div class="row tiles-container">
                <div class="col">
                  <div class="earnings tile">
                    <div class="earnings-header">Total Earnings</div>
                    <EarningsChart />
                  </div>
                </div>
              </div>
            </div>
            <div class="col-4">
              <div class="main-page-calendar h-100">
                <div class="tile h-100">
                  <div class="upcoming-appts-section">
                    <div class="upcoming-appts-header mb-3">Upcoming Appointments</div>
                    <CustomCalendar />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import { mapState, mapActions } from 'vuex'
import axios from 'axios'
import CustomCalendar from '../../components/CustomCalendar.vue'
import EarningsChart from '../../components/EarningsLineChart.vue'
import BarChart from '../../components/EarningsBarChart.vue'
import { mapState } from 'vuex'
export default {
  components: { CustomCalendar, EarningsChart, BarChart },
  name: 'MainContainer',
  data() {
    return {
      numPatients: null,
      lastPatient: null
    }
  },
  computed: {
    ...mapState(['currentUser'])
  },
  mounted () {
    this.getLastPatient()
    this.getTotalPatients()
  },
  methods: {
    async getTotalPatients () {
      const list = await axios.get(process.env.VUE_APP_API_URL + '/numPatients')
      this.numPatients = list.data.numPatients
    },
    async getLastPatient () {
      const patient = await axios.get(process.env.VUE_APP_API_URL + '/lastPatient')
      this.lastPatient = patient.data.lastPatient
    }
  }
}
</script>

<style lang="scss" scoped>
.main-container {
  margin-top: 30px;
}

.tiles-container {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}

.tile {
  background: var(--background-primary);
  border-radius: 0.75rem;
  height: inherit;
  height: calc((100vh - 70px)/3.5);
  padding: 1rem;
  position: relative;
}

.upcoming-appts-header {
  font-weight: 500;
  font-size: 1.125rem;
}

.greeting {
  font-size: 1.375rem;
  margin-bottom: 5px;
}

.greeting-text {
    font-size: 0.875rem;
  }

::v-deep .tile-small-logo {
  filter: brightness(0) saturate(0);
  width: 20px;
  height: 20px;
}

::v-deep .num-appts-logo {
  width: 18px;
  height: 18px;
}

.tile-body {
  // border: 1px solid;
  display: flex;
  // justify-content: center;
  align-items: flex-end;
  height: 90%;
  font-size: 3rem;
}

.greetings-img {
  position: absolute;
  right: 20px;
  bottom: 10px;
  // width: 25%;
  width: 200px;
  img {
    width: 100%;
  }
}

.doctor-name {
  font-size: 1.375rem;
  color: var(--primary-accent-light);
  // color: #536DFE;
}
</style>
