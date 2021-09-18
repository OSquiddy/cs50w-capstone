<template>
  <div class="add-appt-main">
    <form action="" method="post" @submit.prevent="createAppointment">
      <button>Cancel</button>
      <button type="submit">Submit</button>
      <label for="patient">Patient:</label>
      <SearchableDropdown :id="'patient'" :placeholder="'Patient Name'" :dataList="patientsList" :isPatient="true"/>
      <label for="date">Date</label>
      <datetime v-model="date" type="date" :format="'ccc, MMM dd, yyyy'"></datetime>
      <label for="patient">Time:</label>
      <datetime type="time" v-model="time1" use12-hour :format="'hh:mm a'"></datetime>
      <datetime type="time" v-model="time2" use12-hour :format="'hh:mm a'"></datetime>
      <label for="doctor">Doctor</label>
      <SearchableDropdown :id="'doctor'" :placeholder="'Doctor Name'" :dataList="doctorsList"/>
      <label for="payment">Payment:</label>
      <input type="number" name="payment" id="payment" v-model="payment">
    </form>
  </div>
</template>

<script>
import { Datetime } from 'vue-datetime'
import { DateTime } from 'luxon'
import SearchableDropdown from '../../components/SearchableDropdown.vue'
import axios from 'axios'
import { mapState } from 'vuex'

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
      date: DateTime.now().toFormat('yyyy-MM-dd'),
      payment: 0
    }
  },
  computed: {
    ...mapState(['patient', 'doctor'])
  },
  watch: {
    date(newValue, oldValue) {
      console.log(newValue, typeof (newValue))
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
      await axios.post(process.env.VUE_APP_API_URL + '/createAppointment/' + this.patient.id + '/' + this.doctor.id, data)
    }
  }
}
</script>

<style lang="scss" scoped></style>
