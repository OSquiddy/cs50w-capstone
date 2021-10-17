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
              <div class="col-4 col-md-4">
                <div class="patient-card-photo"></div>
              </div>
              <div class="col-8 col-md-4 patient-card-details">
                <div class="patient-card-item">ID: {{patient.id}}</div>
                <div class="patient-card-item">Age: {{patient.age}}yrs</div>
                <div class="patient-card-item">Blood Type: {{patient.blood_type}}</div>
                <div class="patient-card-item">Gender: {{patient.sex}}</div>
                <div class="patient-card-item">Mobile: {{patient.Phone_Number}}</div>
              </div>
              <div class="col-md-4 patiend-additional-details">
                <div class="patient-extra-item">Occupation: {{patient.occupation}}</div>
                <div class="patient-extra-item">DOB: {{patient.date_of_birth}}</div>
                <div class="patient-extra-item">Father's Name: {{patient.fathers_name}}</div>
                <div class="patient-extra-item">Mother's Name: {{patient.mothers_name}}</div>
                <div class="patient-extra-item">Address: {{patient.address}}</div>
              </div>
            </div>
            <!-- <div class="row">
              <div class="col patiend-additional-details">
                <div class="patient-extra-item">Occupation: {{patient.occupation}}</div>
                <div class="patient-extra-item">Address: {{patient.address}}</div>
                <div class="patient-extra-item">DOB: {{patient.date_of_birth}}</div>
                <div class="patient-extra-item">Father's Name: {{patient.fathers_name}}</div>
                <div class="patient-extra-item">Mother's Name: {{patient.mothers_name}}</div>
              </div>
            </div> -->
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col report-section">
        <h2 class="report-section-title">View Reports</h2>
        <div class="report-train" v-if="totalVisits">
          <template v-for="visit, index in visitList">
            <router-link :to="`/p/${patient.id}/v/${index + 1}`" :key="visit.visit_number">
              <div class="report">
                <img src="../../assets/undraw/undraw_report_red.svg" alt="report-icon" class="report-icon">
                <div class="report-title">Visit {{index + 1}}</div>
              </div>
            </router-link>
          </template>
        </div>
        <no-data-container v-else :displayText="noDataMsg" />
      </div>
    </div>
    <!-- <div class="row">
      <div class="col report-section">
        <h2 class="report-section-title">Download Reports</h2>
        <div class="report-train">
          <router-link :to="'/p/' + patient.id + '/v/1'"><div class="report"></div></router-link>
          <router-link :to="'/p/' + patient.id + '/v/1'"><div class="report"></div></router-link>
          <router-link :to="'/p/' + patient.id + '/v/1'"><div class="report"></div></router-link>
          <router-link :to="'/p/' + patient.id + '/v/1'"><div class="report"></div></router-link>
          <router-link :to="'/p/' + patient.id + '/v/1'"><div class="report"></div></router-link>
        </div>
      </div>
    </div> -->
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions, mapState } from 'vuex'
import NoDataContainer from '../../components/NoDataContainer.vue'

export default {
  name: 'PatientMainMobile',
  components: {
    NoDataContainer
  },
  data() {
    return {
      visitList: [],
      generatedSelected: 0,
      noDataMsg: 'There is no visit data for this patient.'
    }
  },
  computed: {
    ...mapState(['patient']),
    totalVisits () {
      return this.visitList.length
    }
  },
  mounted () {
    setTimeout(() => {
      this.getData()
    }, 0)
  },
  methods: {
    ...mapActions(['getPatientInfo']),
    async getData() {
      const id = this.$route.path.split('/')[2]
      const response = await this.getPatientInfo(id)

      if (response.status !== 200) {
        this.getData()
      } else {
        this.getReports()
      }
    },
    async getReports () {
      const response = await axios.get(process.env.VUE_APP_API_URL + '/getNumReports/' + this.patient.id)
      this.visitList = response.data.completedVisits
    }
  }
}
</script>

<style lang="scss" scoped>
.patient-main {
  margin-top: 30px;
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
    min-height: 38px;
  }
  .patient-card-details-box {
    padding-top: 20px;
    padding-bottom: 20px;
    background-color: var(--light-gray);
    // background-color: var(--background-primary);
    .patient-card-photo {
      background-color: var(--medium-gray);
      border-radius: 50%;
      // max-width: 120px;
      margin: 0 auto;
      max-height: 120px;
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
    margin-bottom: 15px;
    .report {
      display: flex;
      flex-direction: column;
      width: 102px;
      // height: 102px;
      border-radius: 20px;
      margin-right: 20px;
      aspect-ratio: 1;
      background-color: var(--light-gray);
      // background-image: url('../../assets/undraw/undraw_hiring_red.svg');
      // background-size: contain;
      // background-repeat: no-repeat;
      // background-position: center;
      // background-position-y: -9px;
      // background-color: var(--dark-gray);
      box-shadow: 0 3px 3px 0px rgba(0, 0, 0, 0.2);
      .report-icon {
        margin: auto 0;
        padding: 0 5px;
      }
      .report-title {
        // border: 1px solid red;
        display: flex;
        justify-content: center;
        width: 100%;
        background: var(--background-primary);
        border-bottom-right-radius: 20px;
        border-bottom-left-radius: 20px;
        padding: 2px 0;
        font-size: 0.75rem;
        font-weight: 500;
        align-self: flex-end;
      }
    }
  }
}

@media screen and (min-width:768px) {
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
      width: 175px;
      // height: 102px;
      border-radius: 20px;
      margin-right: 20px;
      aspect-ratio: 1 / 1.5;
      // background-image: url('../../assets/undraw/undraw_report_red.svg');
      // background-size: contain;
      // background-repeat: no-repeat;
      // background-position: center;
      // background-position-x: -5px;
      // background-color: var(--light-gray);
      box-shadow: 0 3px 3px 0px rgba(0, 0, 0, 0.2);
      .report-title {
        // border: 1px solid red;
        display: flex;
        justify-content: center;
        width: 100%;
        background: var(--background-primary);
        border-bottom-right-radius: 20px;
        border-bottom-left-radius: 20px;
        padding: 8px 0;
        align-self: flex-end;
      }
    }
  }
}
}
</style>
