<template>
  <div class="appointment-main h-100">
    <div class="calendar-wrapper">
      <div class="text-center section">
        <!-- <h2 class="h2">Custom Calendars</h2>
        <p class="text-lg font-medium text-gray-600 mb-6">
          Roll your own calendars using scoped slots
        </p> -->
        <Calendar class="custom-calendar max-w-full" :masks="masks" :attributes="appointmentsList" disable-page-swipe is-expanded>
          <template v-slot:day-content="{ day, attributes }">
            <div class="d-flex flex-column h-100">
              <span class="day-label">{{ day.day }}</span>
              <div class="flex-grow-1 cal-appt-container">
                <template v-for="attr in attributes">
                  <div v-if="attr.customData.patientsList.length" :key="attr.key" class="text-xs p-1 mt-0 mb-1 text-white">
                  <div v-for="patient in attr.customData.patientsList" :key="patient.id" class="appointment" :style="'background:' + patient.background">
                    <div class="name">{{ patient.name }} </div>
                    <div class="time"> {{ patient.time }} </div>
                  </div>
                  </div>
                </template>
              </div>
            </div>
          </template>
        </Calendar>
      </div>
    </div>
  </div>
</template>

<script>
import Calendar from 'v-calendar/lib/components/calendar.umd'
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'Appointments',
  components: {
    Calendar
  },
  data () {
    return {
      masks: {
        weekdays: 'WWW'
      },
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
    }
  }
}
</script>

<style lang="scss" scoped>
.appointment-main {
  margin-top: 30px;
}

.appointment {
  padding: 4px;
  border-radius: 5px;
  margin-bottom: 8px;
  cursor: pointer;
  .name {
    color: white;
    font-size: 0.75rem;
  }
  .time {
    color: white;
    font-size: 0.625rem;
  }
}

.calendar-wrapper {
  padding: 1rem;
  border-radius: 0.75rem;
  background: var(--background-primary);
  // height: inherit;
  margin-bottom: 20px;
}

::-webkit-scrollbar {
  width: 0px;
}
::-webkit-scrollbar-track {
  display: none;
}

.cal-appt-container {
  overflow: scroll;
}

::v-deep .custom-calendar.vc-container {
  --day-border: 1px solid #b8c2cc;
  --day-border-highlight: 1px solid #b8c2cc;
  --day-width: 90px;
  --day-height: 90px;
  --weekday-bg: #f8fafc;
  --weekday-border: 1px solid #eaeaea;
  border-radius: 0;
  width: 100%;
  & .vc-nav-header {
    .vc-svg-icon path {
      fill: #ebf8ff;
    }
  }
  & .vc-nav-item {
    color: #ebf8ff;
  }
  & .is-active {
    color: #2a4365 ;
  }
  & .vc-header {
    background-color: #f1f5f8;
    padding: 10px 0;
  }
  & .vc-weeks {
    padding: 0;
  }
  & .vc-weekday {
    background-color: var(--weekday-bg);
    border-bottom: var(--weekday-border);
    border-top: var(--weekday-border);
    padding: 5px 0;
  }
  & .vc-day {
    padding: 0 5px 3px 5px;
    text-align: left;
    height: calc((100vh - 100px) / 7);
    min-height: var(--day-height);
    min-width: var(--day-width);
    background-color: white;
    &.weekday-1,
    &.weekday-7 {
      background-color: #eff8ff;
    }
    &:not(.on-bottom) {
      border-bottom: var(--day-border);
      &.weekday-1 {
        border-bottom: var(--day-border-highlight);
      }
    }
    &:not(.on-right) {
      border-right: var(--day-border);
    }
  }
  & .vc-day-dots {
    overflow: auto;
    margin-bottom: 5px;
  }
}
</style>
