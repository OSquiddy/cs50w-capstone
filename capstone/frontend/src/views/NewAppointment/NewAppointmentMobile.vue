<template>
  <div class="add-appointment-main">
    <header>
      <div class="container">
        <div class="row">
          <div class="col header px-4 py-3">
            <img src="../../assets/cancel.svg" class="cancel" alt="cross/cancel-icon" />
            <div class="page-header">New Appointment</div>
            <img src="../../assets/tick.svg" class="accept" alt="accept-icon" />
          </div>
        </div>
      </div>
    </header>
    <div class="add-appointment-container">
      <form action="" method="post">
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
                      <input type="text" name="patient" id="patient" placeholder="Patient Name" autocomplete="off" />
                      <SearchableDropdown :placeholder="'Patient Name'" />
                      <!-- <vSelect :options="patients" v-model="fullname" label="fullname">
                        <template v-slot:option="option">
                          <div class="dropdown-row-container">
                          <div class="img"></div>
            <div class="dropdown-content-text patient-group">
              <div class="patient-name"> {{option.fullname}} </div>
              <div class="patient-id"> ID: {{option.id}} </div>
            </div>
                          </div>
                        </template>
                      </vSelect> -->
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
                      <datetime v-model="date" type="date" :format="'ccc, MMM dd, yyyy'"></datetime>
                    </div>
                    <div class="section-input-group">
                      <label for="last-name">Time:</label>
                      <div class="time-input-group">
                        <datetime type="time" v-model="time1" use12-hour :format="'hh:mm a'"></datetime>
                        <img src="../../assets/right-arrow.svg" alt="right-arrow" />
                        <datetime type="time" v-model="time2" use12-hour :format="'hh:mm a'"></datetime>
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
                      <input type="text" name="doctor" id="doctor" placeholder="Doctor Name" autocomplete="off" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <hr class="section-divider" />
      </form>
    </div>
  </div>
</template>

<script>
import { Datetime } from 'vue-datetime'
import { DateTime } from 'luxon'
import SearchableDropdown from '../../components/SearchableDropdown.vue'
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
      patients: [
        { id: 12, fullname: 'Harry Potter' },
        { id: 14, fullname: 'Hermione Granger' },
        { id: 13, fullname: 'Ron Weasley' }
      ],
      fullname: null,
      date: DateTime.now().toFormat('yyyy-MM-dd')
    }
  },
  // computed: {
  //   date() {
  //     return
  //   }
  // },
  mounted () {
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
  margin-top: 1.5rem;
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
