<template>
  <div class="container report-main" :class="[editForm && 'read-only']">
    <div class="row d-flex align-items-center">
      <div class="col-12 col-md-7">
        <PatientSmall :name="patient.first_name + ' ' + patient.last_name" :id="patient.id" :age="patient.age" :gender="patient.sex" :mobile="patient.Phone_Number" :bloodType="patient.blood_type" :photo="getProfilePic(patient)" />
      </div>
      <div class="col-12 col-md-4">
        <button class="download-button" v-if="editForm">
          <img src="../../assets/download.png" class="download-icon" alt="download-icon" />
          <a :href="`../../../assets/pdf/${patient.id}/Generated/${patient.fullname} - Report ${visitNumber}.pdf`">Download PDF Report</a>
        </button>
      </div>
    </div>
    <form method="post" v-on:submit.prevent="submitForm" id="appt-entry-form" class="pb-3">
      <div class="row">
        <div class="col">
          <div class="accordion" id="accordionPanelsStayOpenExample">
            <div class="accordion-item">
              <h2 class="accordion-header" id="complaints-accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#complaints-accordion" aria-expanded="false" aria-controls="complaints-accordion">
                  Chief Complaints
                </button>
              </h2>
              <div id="complaints-accordion" class="accordion-collapse collapse" aria-labelledby="complaints-accordion-header">
                <div class="accordion-body">
                  <textarea name="complaints" id="complaints" rows="4" v-model="report.examination.complaints" :readonly="editForm"></textarea>
                </div>
              </div>
            </div>
            <!-- <div class="accordion-item">
              <h2 class="accordion-header" id="pastHistory-accordion-header">
                <button
                  class="accordion-button collapsed"
                  type="button"
                  data-bs-toggle="collapse"
                  data-bs-target="#pastHistory-accordion"
                  aria-expanded="false"
                  aria-controls="pastHistory-accordion"
                >
                  Past History
                </button>
              </h2>
              <div id="pastHistory-accordion" class="accordion-collapse collapse" aria-labelledby="pastHistory-accordion-header">
                <div class="accordion-body">
                  <div class="past-history-checklist">
                    <div class="form-group past-history-checklist-item">
                      <input type="checkbox" name="t2dm" id="t2dm">
                      <label for="t2dm">T<span>2</span>DM</label>
                    </div>
                    <div class="form-group past-history-checklist-item">
                      <input type="checkbox" name="htn" id="htn">
                      <label for="htn">Hypertension</label>
                    </div>
                    <div class="form-group past-history-checklist-item">
                      <input type="checkbox" name="kidney" id="kidney">
                      <label for="kidney">Kidney Disease</label>
                    </div>
                    <div class="form-group past-history-checklist-item">
                      <input type="checkbox" name="thyroid" id="thyroid">
                      <label for="thyroid">Hyperthyroidism</label>
                    </div>
                    <div class="form-group past-history-checklist-item">
                      <input type="checkbox" name="artery" id="artery" class="past-history-checklist-item">
                      <label for="artery">Coronary Artery Disease</label>
                    </div>
                    <div class="form-group past-history-checklist-item">
                      <input type="checkbox" name="cerebero" id="cerebero" class="past-history-checklist-item">
                      <label for="cerebero">Cereberovascular Disease</label>
                    </div>
                  </div>
                  <div class="past-history-extra">
                    <label for="when">When:</label>
                    <textarea name="when" id="when" rows="4" :readonly="editForm" ></textarea>
                  </div>
                </div>
              </div>
            </div> -->
            <div class="accordion-item" v-if="patient.sex === 'F'">
              <h2 class="accordion-header" id="gynecs-accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#gynecs-accordion" aria-expanded="false" aria-controls="gynecs-accordion">
                  Gynecs/Obs History
                </button>
              </h2>
              <div id="gynecs-accordion" class="accordion-collapse collapse" aria-labelledby="gynecs-accordion-header">
                <div class="accordion-body">
                  <div class="gynecs-form">
                    <div class="form-group gynecs-input">
                      <label for="gplad" class="gynecs-label">GPLAD</label>
                      <input type="text" name="gplad" id="gplad" />
                    </div>
                    <div class="form-group gynecs-input">
                      <label for="edd" class="gynecs-label">EDD</label>
                      <input type="text" name="edd" id="edd" />
                    </div>
                    <div class="form-group gynecs-input">
                      <label for="lmp" class="gynecs-label">LMP</label>
                      <input type="text" name="lmp" id="lmp" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="accordion-item">
              <h2 class="accordion-header" id="examination-accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#examination-accordion" aria-expanded="false" aria-controls="examination-accordion">
                  Examination
                </button>
              </h2>
              <div id="examination-accordion" class="accordion-collapse collapse" aria-labelledby="examination-accordion-header">
                <div class="accordion-body">
                  <div class="examination-container">
                    <div class="examination-input">
                      <label for="respiratory">Respiratory:</label>
                      <textarea name="respiratory" id="respiratory" rows="4" v-model="report.examination.respiratory" :readonly="editForm"></textarea>
                    </div>
                    <div class="examination-input">
                      <label for="cardiovascular">Cardiovascular:</label>
                      <textarea name="cardio" id="cardiovascular" rows="4" v-model="report.examination.cardiovascular" :readonly="editForm"></textarea>
                    </div>
                    <div class="examination-input">
                      <label for="abdominal">Per Abdominal:</label>
                      <textarea name="abdominal" id="abdominal" rows="4" v-model="report.examination.per_abdominal" :readonly="editForm"></textarea>
                    </div>
                    <div class="examination-input">
                      <label for="cereberovascular">Cereberovascular:</label>
                      <textarea name="cereberovascular" id="cereberovascular" rows="4" v-model="report.examination.cereberovascular" :readonly="editForm"></textarea>
                    </div>
                    <div class="examination-input">
                      <label for="localExam">Local Examination:</label>
                      <textarea name="localExam" id="localExam" rows="4" v-model="report.examination.local_examination" :readonly="editForm"></textarea>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="accordion-item">
              <h2 class="accordion-header" id="vitals-accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#vitals-accordion" aria-expanded="false" aria-controls="vitals-accordion">
                  Vitals
                </button>
              </h2>
              <div id="vitals-accordion" class="accordion-collapse collapse" aria-labelledby="vitals-accordion-header">
                <div class="accordion-body">
                  <div class="vitals-form">
                    <div class="form-group vitals-input">
                      <label for="blood-pressure" class="vitals-label">BP</label>
                      <input type="text" name="blood-pressure" id="blood-pressure" v-model="report.examination.blood_pressure" />
                    </div>
                    <div class="form-group vitals-input">
                      <label for="spo2" class="vitals-label">SpO<span>2</span></label>
                      <input type="text" name="spo2" id="spo2" v-model="report.examination.SpO2" />
                    </div>
                    <div class="form-group vitals-input">
                      <label for="pulse" class="vitals-label">Pulse</label>
                      <input type="text" name="pulse" id="pulse" v-model="report.examination.pulse_rate" />
                    </div>
                    <div class="form-group vitals-input">
                      <label for="temp" class="vitals-label">Temp</label>
                      <input type="text" name="temp" id="temp" v-model="report.examination.temperature" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="accordion-item">
              <h2 class="accordion-header" id="general-accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#general-accordion" aria-expanded="false" aria-controls="general-accordion">
                  General
                </button>
              </h2>
              <div id="general-accordion" class="accordion-collapse collapse" aria-labelledby="general-accordion-header">
                <div class="accordion-body">
                  <div class="general-checklist">
                    <div class="form-group general-checklist-item">
                      <input type="checkbox" name="pallor" id="pallor" :disabled="editForm" v-model="report.examination.pallor" />
                      <label for="pallor">Pallor</label>
                    </div>
                    <div class="form-group general-checklist-item">
                      <input type="checkbox" name="icterus" id="icterus" :disabled="editForm" v-model="report.examination.icterus" />
                      <label for="icterus">Icterus</label>
                    </div>
                    <div class="form-group general-checklist-item">
                      <input type="checkbox" name="clubbing" id="clubbing" :disabled="editForm" v-model="report.examination.clubbing" />
                      <label for="clubbing">Clubbing</label>
                    </div>
                    <div class="form-group general-checklist-item">
                      <input type="checkbox" name="koilonychia" id="koilonychia" :disabled="editForm" v-model="report.examination.koilonychia" />
                      <label for="koilonychia">Koilonychia</label>
                    </div>
                    <div class="form-group general-checklist-item">
                      <input type="checkbox" name="lymphadenopathy" id="lymphadenopathy" class="general-checklist-item" :disabled="editForm" v-model="report.examination.lymphadenopathy" />
                      <label for="lymphadenopathy">Lymphadenopathy</label>
                    </div>
                    <div class="form-group general-checklist-item">
                      <input type="checkbox" name="oedema" id="oedema" class="general-checklist-item" :disabled="editForm" v-model="report.examination.oedema" />
                      <label for="oedema">Oedema</label>
                    </div>
                  </div>
                  <div class="general-extra">
                    <label for="others">Others:</label>
                    <textarea name="others" id="others" rows="4" v-model="report.examination.others" :readonly="editForm"></textarea>
                  </div>
                </div>
              </div>
            </div>
            <div class="accordion-item">
              <h2 class="accordion-header" id="result-accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#result-accordion" aria-expanded="false" aria-controls="result-accordion">
                  Result
                </button>
              </h2>
              <div id="result-accordion" class="accordion-collapse collapse" aria-labelledby="result-accordion-header">
                <div class="accordion-body">
                  <div class="result">
                    <label for="diagnonsis">Probable Diagnosis:</label>
                    <textarea name="diagnosis" id="diagnosis" rows="4" v-model="report.examination.diagnosis" :readonly="editForm"></textarea>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button type="submit" class="save-button" form="appt-entry-form">Save</button>
    </form>
  </div>
</template>

<script>
import PatientSmall from '../../components/PatientSmall.vue'
import axios from 'axios'
import { Snackbar, defaultPic } from '../../util/util'

export default {
  name: 'ReportMobile',
  components: {
    PatientSmall
  },
  data() {
    return {
      patient: {},
      report: {},
      editForm: false,
      visitNumber: null
    }
  },
  mounted() {
    this.getPatientInfo()
    this.getReport()
  },
  methods: {
    getProfilePic (user) {
      if (!user.profilePic) {
        return defaultPic(user)
      } else {
        return 'http://localhost:8080/assets' + user.profilePic
      }
    },
    async getPatientInfo() {
      const id = this.$route.params.id
      console.log(process.env.VUE_APP_API_URL + `/p/${id}`)
      const response = await axios.get(process.env.VUE_APP_API_URL + `/p/${id}`)
      this.patient = response.data.patientInfo
    },
    async getReport() {
      const id = this.$route.params.id
      const reportNum = this.$route.params.visitNumber
      this.visitNumber = reportNum
      console.log(process.env.VUE_APP_API_URL + `/p/${id}/v/${reportNum}`)
      const response = await axios.get(process.env.VUE_APP_API_URL + `/p/${id}/v/${reportNum}`)
      this.report = response.data
      console.log(this.report.examination)
      console.log('Visit Status', this.report.visit_completed)
      this.editForm = this.report.visit_completed
    },
    async submitForm() {
      const route = this.$route.path
      const patientID = route.split('/')[2]
      const visitNumber = route.split('/')[4]
      const data = {
        respiratory: this.report.examination.respiratory || null,
        cardio: this.report.examination.cardiovascular || null,
        cerebero: this.report.examination.cereberovascular || null,
        per_abdominal: this.report.examination.per_abdominal || null,
        localExam: this.report.examination.local_examination || null,
        others: this.report.examination.others || null,
        pallor: this.report.examination.pallor || false,
        icterus: this.report.examination.icterus || false,
        lymphadenopathy: this.report.examination.lymphadenopathy || false,
        koilonychia: this.report.examination.koilonychia || false,
        oedema: this.report.examination.oedema || false,
        clubbing: this.report.examination.clubbing || false,
        bloodPressure: this.report.examination.blood_pressure || null,
        temp: this.report.examination.temperature || null,
        spo2: this.report.examination.SpO2 || null,
        complaints: this.report.examination.complaints || null,
        diagnosis: this.report.examination.diagnosis || null,
        pulse: this.report.examination.pulse_rate || null
      }
      axios
        .post(process.env.VUE_APP_API_URL + '/createReport/' + patientID + '/visit/' + visitNumber, data)
        .then((response) => {
          if (response.status === 200) {
            Snackbar('Report Generated!', 'var(--success)')
            // this.editForm = false
          } else {
            console.log('This is weird')
            Snackbar('Report Generation Unsuccessful', 'var(--error-text)')
          }
        })
        .catch(() => {
          Snackbar('Report Generation Unsuccessful', 'var(--error-text)')
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.report-main {
  padding: 30px 20px 0;
}

.accordion {
  border-radius: 0;
  .accordion-item {
    border-radius: 0;
    margin-bottom: 15px;
    border: none;
    .accordion-header {
      button {
        box-shadow: none;
        background-color: var(--light-gray);
        padding: 12px 8px;
        border-radius: 0;
        &::after {
          background-image: url('../../assets/accordion-arrow.svg');
          width: 10px;
          height: 8px;
          background-size: contain;
          margin-right: 10px;
          color: green;
        }
      }
      .accordion-button:not(.collapsed) {
        color: var(--primary-accent-dark);
      }
    }
  }
}

:where(.past-history-checklist-item, .general-checklist-item) {
  margin-bottom: 5px;
  label {
    font-size: 1.125rem;
    margin-left: 10px;
    span {
      font-size: 10px;
    }
  }
}
:where(.past-history-extra, .general-extra) {
  margin-top: 20px;
}

:where(.examination-input, .past-history-extra, .general-extra, .result, .accordion-body) {
  label {
    margin-bottom: 15px;
  }
  textarea {
    width: 100%;
    margin-bottom: 16px;
    border-radius: 5px;
    padding: 10px 15px;
    border-radius: 0.625rem;
    // border: 1px solid var(--input-border-color);
  }
}

:where(.gynecs-input, .vitals-input) {
  margin-bottom: 12px;
  label {
    width: 30%;
  }
  input {
    width: 70%;
    border-radius: 5px;
    border: none;
    padding: 8px 10px;
    border: 1px solid var(--input-border-color);
  }
}

.read-only > * {
  input,
  textarea {
    background: var(--light-gray);
  }
}

.download-button,
.save-button {
  // border: 1px solid black;
  border-radius: 5px;
  padding: 8px 12px;
  display: flex;
  align-items: center;
  margin: 10px auto 25px;
  background: var(--primary-accent-light);
  .download-icon {
    object-fit: contain;
    filter: invert(100);
    width: 20px;
    margin-right: 10px;
  }
  a {
    color: white;
  }
}

.save-button {
  // padding: 0.325rem 0.625rem;
  display: flex;
  justify-content: center;
  border: none;
  // width: 100px;
  text-transform: uppercase;
  width: 100%;
  font-size: 1rem;
  border-radius: 5px;
  color: white;
  border-radius: 5px;
  padding: 5px 12px;
  align-items: center;
  margin: 10px auto 25px;
  background: var(--primary-accent-light);
}
</style>
