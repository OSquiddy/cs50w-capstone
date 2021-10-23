<template>
  <div class="overview-main">
    <form action="" class="settings-form" method="POST">
      <div class="container-fluid">
        <div class="row">
          <div class="col p-0">
            <div class="new-section upcoming">
              <div class="section-text">
                <h6>Upcoming Appointment: </h6>
                <div class="next-appt-date">Fri, <span class="date">24th</span> September, 2021</div>
              </div>
              <img src="../../assets/undraw_medical_research.svg" class="upcoming-appt-icon" alt="upcoming-appt-icon">
            </div>
            <div class="new-section mt-3">
              <h5 class="section-title mb-3">Additional Information</h5>
              <div class="additional-details-grid">
                <div class="additional-details">
                  <div class="wrapper">
                    <img src="../../assets/id-card.svg" svg-inline class="id-icon" alt="id-icon" id="id-card">
                  </div>
                  <div class="detail-title">ID</div>
                  <div class="patient-details">{{patient.id}}</div>
                </div>
                <div class="additional-details">
                  <div class="wrapper">
                    <img src="../../assets/toolbox.svg" svg-inline class="toolbox-icon" alt="toolbox-icon">
                  </div>
                  <div class="detail-title">Occupation</div>
                  <div class="patient-details">{{patient.occupation}}</div>
                </div>
                <div class="additional-details">
                  <div class="wrapper">
                    <img src="../../assets/blood.svg" svg-inline class="blood-icon" alt="blood-icon">
                  </div>
                  <div class="detail-title">Blood Type</div>
                  <div class="patient-details">{{patient.blood_type}}</div>
                </div>
                <div class="additional-details">
                  <div class="wrapper">
                    <img src="../../assets/father.svg" svg-inline class="father-icon" alt="father-icon">
                  </div>
                  <div class="detail-title">Father's Name</div>
                  <div class="patient-details">{{patient.fathers_name}}</div>
                </div>
                <div class="additional-details">
                  <div class="wrapper">
                    <img src="../../assets/mother.svg" svg-inline class="mother-icon" alt="id-icon">
                  </div>
                  <div class="detail-title">Mother's Name</div>
                  <div class="patient-details">{{patient.mothers_name}}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </form>
  <router-view name="default" />
  </div>
</template>

<script>
// import { VueTelInput } from 'vue-tel-input'
import { mapState } from 'vuex'
export default {
  name: 'PatientOverview',
  components: {
    // VueTelInput
  },
  data () {
    return {
      edit: false
    }
  },
  computed: {
    ...mapState(['patient'])
  },
  methods: {
    toggleEdit () {
      this.edit = !this.edit
    }
  }
}
</script>

<style lang="scss" scoped>
.overview-main {
  background-color: var(--background-primary);
  padding: 1rem;
  margin-top: 30px;
  border-radius: 0.75rem;
  border: 1px transparent;
}

::v-deep svg {
  width: 20px;
  height: 20px;
}

.new-section {
  margin-bottom: 25px;
}

.settings-form {
  position: relative;
}
.save-button, .cancel-button {
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

::v-deep .upcoming {
  // border: 1px solid;
  min-height: 150px;
  background-color: #fafafa;
  box-shadow: 0 3px 3px 0px rgba(0, 0, 0, 0.2);
  border-radius: 12px;
  padding: 15px;
  overflow: hidden;
  width: 55%;
  position: relative;
  display: flex;
  h6 {
    color: black;
  }
  .next-appt-date {
    font-size: 2rem;
    // margin-top: 10px;
    .date {
      font-size: 2rem;
      color: var(--primary-accent-dark);
    }
  }
  .upcoming-appt-icon {
    width: 200px;
    object-fit: contain;
    margin-left: auto;
    // display: flex;
    // position: absolute;
    // bottom: 4px;
    // right: 15px;
  }
}

::v-deep .additional-details-grid {
  display: grid;
  justify-content: flex-start;
  grid-template-columns: repeat(auto-fill, 160px);
  grid-gap: 18px;
  .additional-details {
    box-shadow: 0 3px 3px 0px rgba(0, 0, 0, 0.2);
    background-color: white;
    // padding: 10px;
    border-radius: 5px;
    // aspect-ratio: 1 / 1;
    min-height: 170px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
    .wrapper {
      // border: 1px solid;
      position: absolute;
      width: 100%;
      height: 80%;
      top: 20%;
      border-bottom-right-radius: 5px;
      border-bottom-left-radius: 5px;
      display: flex;
    }
    svg {
      // position: absolute;
      // right: 5px;
      // bottom: 5px;
      margin: auto auto;
      display: flex;
      width: 100%;
      height: 50%;
      z-index: 0;
      * {
        fill: var(--primary-accent-dark);
        opacity: 0.15;
      }
    }
    #id-card {
      height: 30%;
    }
    .detail-title {
      font-size: 0.875rem;
      background-color: var(--primary-accent-dark);
      color: white;
      padding: 3px 6px;
      text-align: center;
      height: 20%;
    }
    .patient-details {
      display: flex;
      margin: auto auto;
      font-size: 1.25rem;
      font-weight: 500;
      line-height: 1.2;
      z-index: 3;
      // border: 1px solid;
      width: fit-content;
      align-self: flex-end;
      text-align: center;
    }
  }
}
</style>
