<template>
  <div class="add-appointment-main">
    <header>
      <div class="container-fluid">
        <div class="row">
          <div class="col header px-4 py-3">
            <button class="cancel" @click="$router.go(-1)">
              <img src="../../assets/cancel.svg" alt="cross/cancel-icon" />
            </button>
            <div class="page-header">New Appointment</div>
            <button class="accept" type="submit" form="add-appt-form">
              <img src="../../assets/tick.svg" alt="accept-icon" />
            </button>
          </div>
        </div>
      </div>
    </header>
    <div class="add-appointment-container">
      <form action="" method="post" id="add-appt-form" @submit.prevent="createAppointment">
        <div class="container new-section">
          <div class="row">
            <div class="col">
              <div class="row email-section justify-content-between">
                <div class="col-1 section-icon">
                  <img src="../../assets/patient.svg" alt="patient-icon" class="patient-icon" />
                </div>
                <div class="col-10 section-info">
                  <div class="section-info-container">
                    <div class="section-input-group">
                      <SearchableDropdown :id="'patient'" :placeholder="'Patient Name'" :dataList="patientsList" :isPatient="true"/>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <hr class="section-divider" />
        <div class="container new-section">
          <div class="row">
            <div class="col">
              <div class="row name-section justify-content-between">
                <div class="col-1 section-icon align-self-start">
                  <img src="../../assets/clock.svg" alt="clock-icon" class="clock-icon" />
                </div>
                <div class="col-10 section-info">
                  <div class="section-info-container">
                    <div class="section-input-group">
                      <label for="first-name">Date:</label>
                      <datetime v-model="date" type="date" :format="'ccc, MMM dd, yyyy'" class="theme-red"></datetime>
                    </div>
                    <div class="section-input-group">
                      <label for="last-name">Time:</label>
                      <div class="time-input-group">
                        <datetime type="time" v-model="time1" use12-hour :format="'hh:mm a'" class="theme-red"></datetime>
                        <img src="../../assets/right-arrow.svg" alt="right-arrow" />
                        <datetime type="time" v-model="time2" use12-hour :format="'hh:mm a'" class="theme-red"></datetime>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <hr class="section-divider" />
        <div class="container new-section">
          <div class="row">
            <div class="col">
              <div class="row name-section justify-content-between">
                <div class="col-1 section-icon">
                  <img src="../../assets/doctor.svg" alt="doctor-icon" class="doctor-icon" />
                </div>
                <div class="col-10 section-info">
                  <div class="section-info-container">
                    <div class="section-input-group">
                      <SearchableDropdown :id="'doctor'" :placeholder="'Doctor Name'" :dataList="doctorsList"/>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <hr class="section-divider" />
        <div class="container new-section">
          <div class="row">
            <div class="col">
              <div class="row name-section justify-content-between">
                <div class="col-1 section-icon">
                  <img src="../../assets/doctor.svg" alt="doctor-icon" class="doctor-icon" />
                </div>
                <div class="col-10 section-info">
                  <div class="section-info-container">
                    <div class="section-input-group">
                      <input type="number" name="payment" id="payment" placeholder="Payment" autocomplete="off" v-model="payment" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { Datetime } from 'vue-datetime'
import { DateTime } from 'luxon'
import SearchableDropdown from '../../components/SearchableDropdown.vue'
import axios from 'axios'
import { mapState } from 'vuex'
import { Snackbar } from '../../util/util'

// import vSelect from 'vue-select'
export default {
  name: 'NewPatientMobile',
  components: {
    Datetime,
    SearchableDropdown
    // vSelect
  },
  data() {
    return {
      time1: '07:00',
      time2: '07:30',
      patientsList: [],
      doctorsList: [],
      date: DateTime.now().toFormat('yyyy-MM-dd'),
      payment: 0
    }
  },
  computed: {
    ...mapState(['patient', 'doctor'])
  },
  watch: {
    date(newValue, oldValue) {
      // console.log(newValue, typeof (newValue))
    }
  },
  mounted () {
    this.getPatientsList()
    this.getDoctorsList()
  },
  methods: {
    async getPatientsList () {
      const list = await axios.get(process.env.VUE_APP_API_URL + '/patientList/id')
      this.patientsList = list.data.patientList
    },
    async getDoctorsList () {
      const list = await axios.get(process.env.VUE_APP_API_URL + '/doctorList')
      this.doctorsList = list.data.doctorList
    },
    async createAppointment () {
      const data = {
        date: DateTime.fromISO(this.date).toFormat('yyyy-MM-dd'),
        time1: DateTime.fromISO(this.time1).toFormat('HH:mm'),
        time2: DateTime.fromISO(this.time2).toFormat('HH:mm'),
        payment: this.payment
      }
      try {
        const response = await axios.post(process.env.VUE_APP_API_URL + '/createAppointment/' + this.patient.id + '/' + this.doctor.id, data)
        if (response.status === 200) {
          this.$router.push({ name: 'appointments' })
          Snackbar('Appointment Created!', 'var(--success)')
        }
      } catch (error) {
        Snackbar('Creation Unsuccessful', 'var(--error)')
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.25);
  .accept {
    margin-left: auto;
  }
  .cancel {
    margin-right: 1.25rem;
  }
}

.new-section {
  padding: 0 25px;
}

.add-appointment-container {
  padding-top: 1.5rem;
  height: var(--height);
}
.section-divider {
  width: 80%;
  margin-left: auto;
  margin-top: 0.5rem;
  margin-bottom: 1.25rem;
}

::v-deep .section-info-container {
  .section-input-group {
    margin-bottom: 12px;
    input {
      background: transparent;
      border: none;
      outline: none;
      width: 90%;
      font-size: 1.125rem;
      padding: 2px 0px;
      color: var(--input-text-color);
      margin-top: 5px;
      &:focus {
        border-bottom: 1px solid var(--focus-blue);
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 0;
      }
    }

    .time-input-group {
      display: flex;
      input.vdatetime-input {
        background: transparent;
        border: none;
        outline: none;
        width: 6rem;
        font-size: 1.125rem;
        padding: 2px 0px;
        color: var(--input-text-color);
        margin-top: 5px;
      }
      .vdatetime {
        &:first-of-type {
          margin-right: 0.5rem;
        }
        &:last-of-type {
          margin-left: 1.5rem;
        }
      }
    }
  }
}

::v-deep .vdatetime-popup__year, ::v-deep .vdatetime-popup__date {
  color: white;
  opacity: 1;
}

.section-info-container > .section-input-group:last-child {
  margin-bottom: 0;
}

.section-info {
  padding-left: 0;
}

.section-icon {
  align-self: center;
}

.img {
  background: var(--medium-gray);
  width: 30px;
  aspect-ratio: 1;
  display: flex;
  align-self: center;
  border-radius: 50%;
  margin-right: 20px;
}

.dropdown-row-container {
  display: flex;
}

// .vs__dropdown-menu {
//   background: green;
// }

</style>
