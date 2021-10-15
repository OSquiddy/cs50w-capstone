<template>
  <div class="add-appt-main">
    <div class="container-fluid">
      <div class="row">
        <div class="col-4">
          <div class="section-header">Add Appointment</div>
          <form action="" method="post" @submit.prevent="createAppointment">
            <div class="section-input">
              <label for="patient">
                  <!-- <img src="../../assets/patient.svg" alt="patient-icon" class="patient-icon" /> -->
                Patient :</label>
              <div>
                <SearchableDropdown :id="'patient'" :placeholder="'Patient Name'" :dataList="patientsList" :isPatient="true"/>
              </div>
            </div>
            <div class="section-input">
              <label for="date">
                  <!-- <img src="../../assets/clock.svg" alt="patient-icon" class="patient-icon" /> -->
                Date :</label>
              <datetime v-model="date" type="date" :format="'ccc, MMM dd, yyyy'" class="theme-red"></datetime>
            </div>
            <div class="section-input">
              <label for="patient">Time :</label>
              <div class="time-input-group">
                <datetime type="time" v-model="time1" use12-hour :format="'hh:mm a'" class="theme-red"></datetime>
                <!-- <img src="../../assets/right-arrow.svg" alt="right-arrow" /> -->
                <datetime type="time" v-model="time2" use12-hour :format="'hh:mm a'" class="theme-red"></datetime>
              </div>
            </div>
            <div class="section-input">
              <label for="doctor">
                  <!-- <img src="../../assets/doctor.svg" alt="doctor-icon" class="doctor-icon" /> -->
                Doctor :</label>
              <div>
                <SearchableDropdown :id="'doctor'" :placeholder="'Doctor Name'" :dataList="doctorsList"/>
              </div>
            </div>
            <div class="section-input">
              <label for="payment">
                  <!-- <img src="../../assets/cash.svg" svg-inline alt="cash-icon" class="cash-icon" /> -->
                Payment :</label>
              <input type="number" name="payment" id="payment" v-model="payment" min="10">
            </div>
            <div class="button-group">
              <button class="cancel-button" @click="$router.push('/')">Cancel</button>
              <button type="submit" class="submit-button">Submit</button>
            </div>
          </form>
        </div>
      </div>
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

export default {
  name: 'NewAppointment',
  components: {
    Datetime,
    SearchableDropdown
  },
  data () {
    return {
      time1: '07:00',
      time2: '07:30',
      patientsList: [],
      doctorsList: [],
      date: null,
      payment: 0
    }
  },
  computed: {
    ...mapState(['patient', 'doctor'])
  },
  watch: {
    // date(newValue, oldValue) {
    // },
    // doctorsList (newValue, oldValue) {
    //   console.log('Doctors List', newValue)
    // },
    // patientsList (newValue, oldValue) {
    //   console.log('Patients List', newValue)
    // }
  },
  mounted () {
    this.getPatientsList()
    this.getDoctorsList()
    this.date = DateTime.now().toFormat('yyyy-MM-dd')
  },
  methods: {
    async getPatientsList () {
      try {
        const list = await axios.get(process.env.VUE_APP_API_URL + '/patientList/id')
        this.patientsList = list.data.patientList
      } catch (error) {
        this.getPatientsList()
      }
    },
    async getDoctorsList () {
      try {
        const list = await axios.get(process.env.VUE_APP_API_URL + '/doctorList')
        this.doctorsList = list.data.doctorList
      } catch (error) {
        this.getDoctorsList()
      }
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
          Snackbar('Appointment Created!', 'var(--success)')
        }
      } catch (error) {
        Snackbar('Creation Unsuccessful', 'var(--error-text')
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.add-appt-main {
  background-color: var(--background-primary);
  padding: 1rem;
  margin-top: 30px;
  border-radius: 0.75rem;
  border: 1px transparent;
}

.section-header {
  font-size: 1.125rem;
  margin-bottom: 15px;
}

::v-deep .section-input {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
    label {
      // width: 100%;
      font-size: 0.875rem;
    }
    input {
      background: var(--light-gray);
      border: none;
      outline: none;
      width: 200px;
      width: 100%;
      padding: 5px 10px;
      color: var(--input-text-color);
      border-radius: 5px;
      margin-top: 5px;
      &:focus {
        border-bottom: 1px solid var(--focus-blue);
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 0;
      }
    }
  }

 ::v-deep #patient, ::v-deep #doctor {
  width: 200px;
}

::v-deep .time-input-group {
  display: flex;
  input.vdatetime-input {
    // background: transparent;
    // border: none;
    // outline: none;
    width: 6rem;
    // font-size: 1.125rem;
    // padding: 2px 0px;
    // color: var(--input-text-color);
    margin-top: 5px;
  }
  .vdatetime {
    &:first-of-type {
      margin-right: 0.5rem;
    }
    &:last-of-type {
      margin-left: 0.5rem;
    }
  }
}

.button-group {
  display: flex;
  margin-top: 30px;
  .submit-button, .cancel-button {
    padding: 0.325rem 0.625rem;
    display: flex;
    justify-content: center;
    border: none;
    outline: none;
    width: 100px;
    font-size: 0.75rem;
    border-radius: 5px;
    background: var(--button-blue);
    color: white;
    // position: sticky;
    // top: 20px;
    // right: 0;
  }

  .cancel-button {
    margin-left: auto;
    margin-right: 0.625rem;
    background-color: var(--light-gray);
    color: var(--primary);
    border: 1px solid #ccc;
  }
}

::v-deep svg {
  width: 20px;
  height: 20px;
  * {
    fill: black;
  }
}
</style>
