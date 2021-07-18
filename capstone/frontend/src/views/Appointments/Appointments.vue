<template>
  <div class="appointment-main">
    <div class="container appointment-list">
      <!-- <div v-for="item in items" :key="item.id">
        {{ item }}
      </div> -->
      <!-- Each row will either be its own component or will go in the v-for as is. -->
      <div class="row">
        <div class="col appointment-day">
          <div class="appointment-title">
            <div>
              <span class="appointment-date">July 3rd</span>
              <span class="appointment-meta">Today</span>
            </div>
          </div>
          <div class="appointment-patient-list">
            <div class="patient-appt-container">
              <div class="vertical-accent"></div>
              <div class="patient-appt-details">
                <div class="patient-appt-name">Ronald Weasley</div>
                <div class="patient-appt-time">11:00 AM - 11:30 AM</div>
              </div>
              <button class="patient-appt-join">Join</button>
            </div>
            <div class="patient-appt-container">
              <div class="vertical-accent"></div>
              <div class="patient-appt-details">
                <div class="patient-appt-name">Harry Potter</div>
                <div class="patient-appt-time">11:30 AM - 12:0 PM</div>
              </div>
              <button class="patient-appt-join">Join</button>
            </div>
          </div>
        </div>
      </div>
      <!-- Each row will either be its own component or will go in the v-for as is. -->
      <div class="row">
        <div class="col appointment-day">
          <div class="appointment-title">
            <div>
              <span class="appointment-date">July 4th</span>
              <span class="appointment-meta">Tomorrow</span>
            </div>
          </div>
          <div class="appointment-patient-list">
            <div class="patient-appt-container">
              <div class="vertical-accent"></div>
              <div class="patient-appt-details">
                <div class="patient-appt-name">Fred Weasley</div>
                <div class="patient-appt-time">11:00 AM - 11:30 AM</div>
              </div>
              <button class="patient-appt-join">Join</button>
            </div>
            <div class="patient-appt-container">
              <div class="vertical-accent"></div>
              <div class="patient-appt-details">
                <div class="patient-appt-name">Sirius Black</div>
                <div class="patient-appt-time">11:30 AM - 12:0 PM</div>
              </div>
              <button class="patient-appt-join">Join</button>
            </div>
          </div>
        </div>
      </div>
      <!-- Each row will either be its own component or will go in the v-for as is. -->
      <div class="row">
        <div class="col appointment-day">
          <div class="appointment-title">
            <span class="appointment-date">July 5th</span>
            <!-- <span v-if="item.meta" class="appointment-meta"></span> -->
          </div>
          <div class="appointment-patient-list">
            <div class="patient-appt-container">
              <div class="vertical-accent"></div>
              <div class="patient-appt-details">
                <span class="no-patient">No meetings</span>
              </div>
              <button class="patient-appt-join">Join</button>
            </div>
          </div>
        </div>
      </div>
      <!-- Each row will either be its own component or will go in the v-for as is. -->
      <div class="row">
        <div class="col appointment-day">
          <div class="appointment-title">
            <span class="appointment-date">July 6th</span>
            <!-- <span v-if="item.meta" class="appointment-meta"></span> -->
          </div>
          <div class="appointment-patient-list">
            <div class="patient-appt-container">
              <div class="vertical-accent"></div>
              <div class="patient-appt-details">
                <span class="no-patient">No meetings</span>
              </div>
              <button class="patient-appt-join">Join</button>
            </div>
          </div>
        </div>
      </div>
      <!-- Each row will either be its own component or will go in the v-for as is. -->
      <div class="row">
        <div class="col appointment-day">
          <div class="appointment-title">
            <span class="appointment-date">July 7th</span>
            <!-- <span v-if="item.meta" class="appointment-meta"></span> -->
          </div>
          <div class="appointment-patient-list">
            <div class="patient-appt-container">
              <div class="vertical-accent"></div>
              <div class="patient-appt-details">
                <span class="no-patient">No meetings</span>
              </div>
              <button class="patient-appt-join">Join</button>
            </div>
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

export default {
  name: 'Appointments',
  // components: {
  //   SearchContainer
  // },
  data() {
    return {}
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
        &:hover {
          background: yellow;
        }
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
