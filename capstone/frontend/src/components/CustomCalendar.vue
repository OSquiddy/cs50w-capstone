<template>
  <div class="custom-calendar-container">
    <div class="month-year-display">
      <span class="month">{{currentMonth.name}}</span> <span class="year">{{currentYear}}</span>
    </div>
    <div class="custom-carousel mt-2">
      <button class="left-arrow" @click="getPrevWeek"><img src="../assets/right-chevron.svg" alt="prev-dates" class="mirror"></button>
      <div class="date-slider">
          <div class="currWeek">
            <div class="day-date-box" v-for="day in currentWeek" :key="day.date.day" @click="selectDate(day, $event)" :class="[selectedDate.date.day == day.date.day ? 'active' : '']">
              <div class="day">{{day.day}}</div>
              <div class="date" v-if="day.date.month === currentMonth.index">{{day.date.day}}</div>
            </div>
          </div>
      </div>
      <button class="right-arrow" @click="getNextWeek"><img src="../assets/right-chevron.svg" alt="next-dates"></button>
    </div>
    <template v-if="appointmentsList.length">
    <div class="appointment-list mt-3" v-for="appointment in appointmentsList" :key="appointment.key">
        <div class="appointment-patient-list" v-for="patient in appointment.customData.patientsList" :key="patient.id">
          <div class="patient-appt-container">
            <div class="vertical-accent"></div>
            <div class="patient-appt-details">
              <div class="patient-appt-name">{{ patient.name }}</div>
              <div class="patient-appt-time">{{ patient.time }}</div>
            </div>
            <button class="patient-appt-join">Join</button>
          </div>
        </div>
    </div>
    </template>
    <template v-else>
      <div class="appointment-patient-list mt-3">
        <div class="patient-appt-container">
          <div class="vertical-accent"></div>
          <div class="patient-appt-details">
            <span class="no-patient">No meetings</span>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
import { DateTime } from 'luxon'
export default {
  name: 'CustomCalendar',
  data () {
    return {
      appointmentsList: [],
      currentWeek: null,
      currentWeekStart: null,
      currentWeekEnd: null,
      currentMonth: {
        name: null,
        index: null
      },
      currentYear: null,
      prevWeek: null,
      nextWeek: null,
      selectedDate: {
        name: null,
        date: null
      }
    }
  },
  mounted () {
    this.getWeek()
    this.getFilteredList()
  },
  watch: {
    selectedDate () {
      this.getFilteredList()
    }
  },
  methods: {
    async getFilteredList () {
      const list = await axios.get(process.env.VUE_APP_API_URL + '/appointmentsList/' + this.selectedDate.name)
      this.appointmentsList = list.data.appointmentsList
    },
    getWeek () {
      const today = DateTime.now()
      const weekYear = today.year
      const weekNumber = today.weekNumber
      const week = DateTime.fromObject({ weekYear: weekYear, weekNumber: weekNumber })
      let weekStart = week.startOf('week')
      let weekEnd = week.endOf('week')
      this.currentWeekStart = weekStart
      this.currentWeekEnd = weekEnd
      this.selectedDate = { name: today.toFormat('yyyy-MM-dd'), date: today }
      this.currentWeek = this.setWeek(weekStart, weekEnd)
      weekStart = weekStart.minus({ weeks: 1 })
      weekEnd = weekEnd.minus({ weeks: 1 })
      this.prevWeek = this.setWeek(weekStart, weekEnd)
      weekStart = weekStart.plus({ weeks: 2 })
      weekEnd = weekEnd.plus({ weeks: 2 })
      this.nextWeek = this.setWeek(weekStart, weekEnd)
      this.currentMonth = { name: today.toFormat('MMMM'), index: today.month }
      this.currentYear = today.toFormat('yyyy')
    },
    setWeek (weekStart, weekEnd) {
      const array = []
      for (let days = weekStart; days <= weekEnd; days = days.plus({ days: 1 })) {
        array.push({ date: days.toObject(), day: days.weekdayShort })
      }
      return array
    },
    selectDate (day, e) {
      const elem = e.target.parentElement
      if (elem.classList.contains('day-date-box')) {
        this.selectedDate = {
          name: `${day.date.year}-${day.date.month}-${day.date.day}`,
          date: DateTime.fromObject({ year: day.date.year, month: day.date.month, day: day.date.day })
        }
        const buttons = document.querySelectorAll('.day-date-box')
        buttons.forEach(button => button.classList.remove('active'))
        elem.classList.add('active')
      }
    },
    getNextWeek () {
      const today = DateTime.now()
      if (this.currentWeekEnd <= today.endOf('month')) {
        this.prevWeek = this.currentWeek
        this.currentWeek = this.nextWeek
        this.currentWeekStart = DateTime.fromObject(this.nextWeek[0].date)
        this.currentWeekEnd = DateTime.fromObject(this.nextWeek[6].date)
        const start = this.currentWeekStart.plus({ weeks: 1 })
        const end = this.currentWeekEnd.plus({ weeks: 1 })
        this.nextWeek = this.setWeek(start, end)
      }
    },
    getPrevWeek () {
      const today = DateTime.now()
      if (this.currentWeekStart >= today.startOf('month')) {
        this.nextWeek = this.currentWeek
        this.currentWeek = this.prevWeek
        this.currentWeekStart = DateTime.fromObject(this.prevWeek[0].date)
        this.currentWeekEnd = DateTime.fromObject(this.prevWeek[6].date)
        const start = this.currentWeekStart.minus({ weeks: 1 })
        const end = this.currentWeekEnd.minus({ weeks: 1 })
        this.prevWeek = this.setWeek(start, end)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.custom-carousel {
  display: flex;
  justify-content: center;
}
.date-slider {
  display: flex;
  width: 100%;
  overflow: hidden;
}

.prevWeek, .currWeek, .nextWeek {
  display: flex;
  width: 100%;
  justify-content: space-evenly;
}

.day {
  font-size: 12px;
  text-align: center;
}
.date {
  text-align: center;
  font-size: 14px;
  font-weight: 600;
}

.day-date-box {
  cursor: pointer;
  // border: 1px solid red;
  width: 2.5rem;
  padding: 2px 4px;
  border-radius: 5px;
  // min-width: 2.2rem;
}

.active {
  // background: var(--primary-accent-dark);
  background: #000;
  *{
    color: white;
  }
}

.left-arrow, .right-arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  align-self: center;
  width: 22px;
  height: 22px;
  border-radius: 5px;
  background-color: var(--primary-accent-light);
  outline: none;
  border: none;
  img {
    filter: invert(100)
  }
}

.month-year-display {
  .month, .year {
    font-size: 0.875rem;
  }
}

.appointment-list {
  overflow: scroll;
  height: 50vh;
  // &:hover {
  //   overflow: scroll;
  // }
}

.patient-appt-container {
  display: flex;
  background: #f4f4f4;
  border-radius: 5px;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.2);
  padding: 8px 10px;
  margin: 0 0 15px;
  width: 100%;
  .vertical-accent {
    width: 4px;
    border-radius: 3px;
    background: var(--primary-accent-light);
    margin-right: 12px;
  }
  .patient-appt-name {
    font-size: 0.875rem;
  }
  .patient-appt-time {
    font-size: 0.625rem;
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
</style>
