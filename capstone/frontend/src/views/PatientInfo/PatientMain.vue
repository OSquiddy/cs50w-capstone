<template>
  <div class="container patient-main">
    <div class="row">
      <div class="col">
        <h1 class="page-title">Patient Information</h1>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="patient-card">
          <div class="patient-card-name">{{patient.first_name}} {{patient.last_name}}</div>
          <div class="container patient-card-details-box">
            <div class="row">
              <div class="col-4 patient-card-photo"></div>
              <div class="col-8 patient-card-details">
                <div class="patient-card-item">ID: {{patient.id}}</div>
                <div class="patient-card-item">Age: {{patient.age}}yrs</div>
                <div class="patient-card-item">Blood Type: {{patient.blood_type}}</div>
                <div class="patient-card-item">Gender: {{patient.sex}}</div>
                <div class="patient-card-item">Mobile: {{patient.Phone_Number}}</div>
              </div>
            </div>
            <div class="row">
              <div class="col patiend-additional-details">
                <div class="patient-extra-item">Occupation: {{patient.occupation}}</div>
                <div class="patient-extra-item">Address: {{patient.address}}</div>
                <div class="patient-extra-item">DOB: {{patient.date_of_birth}}</div>
                <div class="patient-extra-item">Father's Name: {{patient.fathers_name}}</div>
                <div class="patient-extra-item">Mother's Name: {{patient.mothers_name}}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col report-section">
        <h2 class="report-section-title">Reports</h2>
        <div class="report-train">
          <router-link :to="'/p/' + patient.id + '/v/1'"><div class="report"></div></router-link>
          <router-link :to="'/p/' + patient.id + '/v/1'"><div class="report"></div></router-link>
          <router-link :to="'/p/' + patient.id + '/v/1'"><div class="report"></div></router-link>
          <router-link :to="'/p/' + patient.id + '/v/1'"><div class="report"></div></router-link>
          <router-link :to="'/p/' + patient.id + '/v/1'"><div class="report"></div></router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PatientMain',
  data() {
    return {
      patient: {}
    }
  },
  mounted () {
    this.getPatientInfo()
  },
  methods: {
    async getPatientInfo() {
      const id = this.$route.params.id
      console.log(id)
      const info = await axios.get(process.env.VUE_APP_API_URL + `/p/${id}`)
      this.patient = info.data.patientInfo
    }
  }
}
</script>

<style lang="scss" scoped>
.patient-main {
  padding: 0 20px;
}
.page-title {
  font-size: 1.125rem;
  margin-bottom: 20px;
  font-weight: 400;
}

.patient-card {
  border-radius: 20px;
  overflow: hidden;
  .patient-card-name {
    text-align: center;
    background-color: var(--primary-accent-light);
    padding: 7px 0;
    color: white;
  }
  .patient-card-details-box {
    padding-top: 20px;
    padding-bottom: 20px;
    background-color: var(--light-gray);
    .patient-card-photo {
      background-color: var(--medium-gray);
      border-radius: 50%;
      aspect-ratio: 1;
      align-self: flex-start;
    }
    .patient-card-details {
      padding-left: 20px;
    }
  }
}

:where(.patient-card-item, .patient-extra-item) {
        font-size: 0.75rem;
        margin-bottom: 5px;
      }

.report-section {
  padding-top: 20px;
  .report-section-title {
    font-size: 1.125rem;
    margin-bottom: 20px;
    font-weight: 400;
  }
  .report-train {
    display: flex;
    margin-right: -20px;
    overflow-x: auto;
    padding-bottom: 15px;
    .report {
      display: block;
      width: 102px;
      height: 102px;
      border-radius: 20px;
      margin-right: 20px;
      aspect-ratio: 1;
      background-color: var(--medium-gray);
    }
  }
}
</style>
