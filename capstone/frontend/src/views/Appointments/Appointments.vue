<template>
  <div class="appointment-main">
    <div class="container appointment-list">
      <div v-for="appointment in appointmentsList" :key="appointment.date">
        <div class="row">
        <div class="col appointment-day">
          <div class="appointment-title">
            <div>
              <span class="appointment-date">{{ formatDate(appointment.date) }}</span>
              <span class="appointment-meta">{{ appointment.meta }}</span>
            </div>
          </div>
          <template v-if="appointment.patientsList.length">
          <div class="appointment-patient-list" v-for="patient in appointment.patientsList" :key="patient.id">
              <div class="patient-appt-container">
                <div class="vertical-accent"></div>
                <div class="patient-appt-details">
                  <div class="patient-appt-name">{{ patient.name }}</div>
                  <div class="patient-appt-time">{{ patient.time }}</div>
                </div>
                <button class="patient-appt-join">Join</button>
              </div>
            </div>
          </template>
          <template v-else>
            <div class="appointment-patient-list">
              <div class="patient-appt-container">
                <div class="vertical-accent"></div>
                <div class="patient-appt-details">
                  <span class="no-patient">No meetings</span>
                </div>
              </div>
            </div>
          </template>
          </div>
        </div>
      </div>
    </div>
    <button class="new-appointment">
      <img src="../../assets/plus.svg" alt="add-symbol">
    </button>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
import { DateTime } from 'luxon'

export default {
  name: 'Appointments',
  // components: {
  //   SearchContainer
  // },
  data() {
    return {
      appointmentsList: []
    }
  },
  computed: {
    ...mapState('search', ['searchKeyword'])
  },
  watch: {
    searchKeyword() {
      if (this.searchKeyword !== '') {
        this.getFilteredList()
      } else {
        this.getAppointmentsList()
      }
    }
  },
  mounted () {
    this.getAppointmentsList()
  },
  methods: {
    async getAppointmentsList () {
      const list = await axios.get(process.env.VUE_APP_API_URL + '/appointmentsList')
      this.appointmentsList = list.data.appointmentsList
    },
    async getFilteredList () {
      const list = await axios.get(process.env.VUE_APP_API_URL + '/appointmentsList/' + this.searchKeyword)
      this.appointmentsList = list.data.appointmentsList
    },
    formatDate (date) {
      const dt = DateTime.fromISO(date)
      return dt.toFormat('LLL dd')
    }
  }
}
</script>

<style lang="scss" scoped>
.appointment-list {
  height: calc(100vh - 197px);
  overflow-y: scroll;
  padding-bottom: 55px;
  margin-top: -1px;
  .appointment-day {
    .appointment-title {
      display: flex;
      margin:0 -12px 15px;
      background: white;
      position: sticky;
      padding: 15px 12px 0;
      top: 0px;
      .appointment-date {
        display: inline-flex;
        font-weight: 500;
        font-size: 0.95rem;
        margin-right: 12px;
      }
      .appointment-meta {
        display: inline-flex;
        font-size: 0.7rem;
        align-self: center;
      }
    }
    .patient-appt-container {
      display: flex;
      background: #f4f4f4;
      border-radius: 5px;
      box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.2);
      padding: 8px 10px;
      margin-bottom: 15px;
      .vertical-accent {
        width: 4px;
        border-radius: 3px;
        background: #c4c4c4;
        margin-right: 12px;
      }
      .patient-appt-join {
        border-radius: 5px;
        border: 1px solid #353535;
        align-self: center;
        padding: 3px 19px;
        font-size: 0.75rem;
        margin-left: auto;
        // &:hover {
        //   background: yellow;
        // }
      }
    }
  }
}

.appointment-main {
  position: relative;
}
.new-appointment {
  background-color: #353535;
  border-radius: 50%;
  aspect-ratio: 1;
  border: none;
  position: absolute;
  bottom: 30px;
  right: 35px;
  img {
    padding: 8px;
  }
}
</style>
