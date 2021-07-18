<template>
  <div class="container report-main">
    <div class="row">
      <div class="col">
        <PatientSmall :name="patient.first_name + ' ' + patient.last_name" :id="patient.id" :age="patient.age" :gender="patient.sex" :mobile="patient.Phone_Number" :bloodType="patient.blood_type" />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="accordion" id="accordionPanelsStayOpenExample">
          <div class="accordion-item">
            <h2 class="accordion-header" id="panelsStayOpen-headingOne">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="false" aria-controls="panelsStayOpen-collapseOne">
                Chief Complaints
              </button>
            </h2>
            <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingOne">
              <div class="accordion-body">
                <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These
                classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also
                worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="panelsStayOpen-headingTwo">
              <button
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#panelsStayOpen-collapseTwo"
                aria-expanded="false"
                aria-controls="panelsStayOpen-collapseTwo"
              >
                Past History
              </button>
            </h2>
            <div id="panelsStayOpen-collapseTwo" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingTwo">
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
                  <textarea name="when" id="when" rows="4"></textarea>
                </div>
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="panelsStayOpen-headingThree">
              <button
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#panelsStayOpen-collapseThree"
                aria-expanded="false"
                aria-controls="panelsStayOpen-collapseThree"
              >
                Gynecs/Obs History
              </button>
            </h2>
            <div id="panelsStayOpen-collapseThree" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingThree">
              <div class="accordion-body">
                <!-- <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These
                classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also
                worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow. -->
                <div class="gynecs-form">
                  <div class="form-group gynecs-input">
                    <label for="gplad" class="gynecs-label">GPLAD</label>
                    <input type="text" name="gplad" id="gplad">
                  </div>
                  <div class="form-group gynecs-input">
                    <label for="edd" class="gynecs-label">EDD</label>
                    <input type="text" name="edd" id="edd">
                  </div>
                  <div class="form-group gynecs-input">
                    <label for="lmp" class="gynecs-label">LMP</label>
                    <input type="text" name="lmp" id="lmp">
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="panelsStayOpen-headingFour">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseFour" aria-expanded="false" aria-controls="panelsStayOpen-collapseFour">
                Examination
              </button>
            </h2>
            <div id="panelsStayOpen-collapseFour" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingFour">
              <div class="accordion-body">
                <!-- <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These
                classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also
                worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow. -->
                <div class="examination-container">
                  <div class="examination-input">
                    <label for="respiratory">Respiratory:</label>
                    <textarea name="respiratory" id="respiratory" rows="4" :value="report.examination.respiratory" readonly></textarea>
                  </div>
                  <div class="examination-input">
                    <label for="cardiovascular">Cardiovascular:</label>
                    <textarea name="cardiovascular" id="cardiovascular" rows="4" :value="report.examination.cardiovascular"></textarea>
                  </div>
                  <div class="examination-input">
                    <label for="abdominal">Per Abdominal:</label>
                    <textarea name="abdominal" id="abdominal" rows="4"></textarea>
                  </div>
                  <div class="examination-input">
                    <label for="cereberovascular">Cereberovascular:</label>
                    <textarea name="cereberovascular" id="cereberovascular" rows="4" :value="report.examination.cereberovascular"></textarea>
                  </div>
                  <div class="examination-input">
                    <label for="localExam">Local Examination:</label>
                    <textarea name="localExam" id="localExam" rows="4"></textarea>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="panelsStayOpen-headingFive">
              <button
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#panelsStayOpen-collapseFive"
                aria-expanded="false"
                aria-controls="panelsStayOpen-collapseFive"
              >
                Vitals
              </button>
            </h2>
            <div id="panelsStayOpen-collapseFive" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingFive">
              <div class="accordion-body">
                <div class="vitals-form">
                  <div class="form-group vitals-input">
                    <label for="blood-pressure" class="vitals-label">BP</label>
                    <input type="text" name="blood-pressure" id="blood-pressure">
                  </div>
                  <div class="form-group vitals-input">
                    <label for="spo2" class="vitals-label">SpO<span>2</span></label>
                    <input type="text" name="spo2" id="spo2">
                  </div>
                  <div class="form-group vitals-input">
                    <label for="pulse" class="vitals-label">Pulse</label>
                    <input type="text" name="pulse" id="pulse">
                  </div>
                  <div class="form-group vitals-input">
                    <label for="temp" class="vitals-label">Temp</label>
                    <input type="text" name="temp" id="temp">
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="panelsStayOpen-headingSix">
              <button
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#panelsStayOpen-collapseSix"
                aria-expanded="false"
                aria-controls="panelsStayOpen-collapseSix"
              >
                General
              </button>
            </h2>
            <div id="panelsStayOpen-collapseSix" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingSix">
              <div class="accordion-body">
                <!-- <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These
                classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also
                worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow. -->
                <div class="general-checklist">
                  <div class="form-group general-checklist-item">
                    <input type="checkbox" name="pallor" id="pallor">
                    <label for="pallor">Pallor</label>
                  </div>
                  <div class="form-group general-checklist-item">
                    <input type="checkbox" name="icterus" id="icterus">
                    <label for="icterus">Icterus</label>
                  </div>
                  <div class="form-group general-checklist-item">
                    <input type="checkbox" name="clubbing" id="clubbing">
                    <label for="clubbing">Clubbing</label>
                  </div>
                  <div class="form-group general-checklist-item">
                    <input type="checkbox" name="koilonychia" id="koilonychia">
                    <label for="koilonychia">Koilonychia</label>
                  </div>
                  <div class="form-group general-checklist-item">
                    <input type="checkbox" name="lymphadenopathy" id="lymphadenopathy" class="general-checklist-item">
                    <label for="lymphadenopathy">Lymphadenopathy</label>
                  </div>
                  <div class="form-group general-checklist-item">
                    <input type="checkbox" name="oedema" id="oedema" class="general-checklist-item">
                    <label for="oedema">Oedema</label>
                  </div>
                </div>
                <div class="general-extra">
                  <label for="others">Others:</label>
                  <textarea name="others" id="others" rows="4"></textarea>
                </div>
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="panelsStayOpen-headingSeven">
              <button
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#panelsStayOpen-collapseSeven"
                aria-expanded="false"
                aria-controls="panelsStayOpen-collapseSeven"
              >
                Result
              </button>
            </h2>
            <div id="panelsStayOpen-collapseSeven" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingSeven">
              <div class="accordion-body">
                <!-- <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These
                classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also
                worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow. -->
                <div class="result">
                  <label for="diagnonsis">Probable Diagnosis:</label>
                  <textarea name="diagnosis" id="diagnosis" rows="4"></textarea>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PatientSmall from '../../components/PatientSmall.vue'
import axios from 'axios'

export default {
  name: 'Report',
  components: {
    PatientSmall
  },
  data() {
    return {
      patient: {},
      report: {}
    }
  },
  mounted () {
    this.getPatientInfo()
    this.getReport()
  },
  methods: {
    async getPatientInfo () {
      const id = this.$route.params.id
      console.log(process.env.VUE_APP_API_URL + `/p/${id}`)
      const response = await axios.get(process.env.VUE_APP_API_URL + `/p/${id}`)
      this.patient = response.data.patientInfo
    },
    async getReport () {
      const id = this.$route.params.id
      const reportNum = this.$route.params.visitNumber
      console.log(process.env.VUE_APP_API_URL + `/p/${id}/v/${reportNum}`)
      const response = await axios.get(process.env.VUE_APP_API_URL + `/p/${id}/v/${reportNum}`)
      this.report = response.data
    }
  }
}
</script>

<style lang="scss" scoped>
.report-main {
  padding: 0 20px;
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
        background-color: var(--lightest-gray);
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

:where(.examination-input, .past-history-extra, .general-extra, .result) {
  label {
    margin-bottom: 15px;
  }
  textarea {
    width: 100%;
    margin-bottom: 16px;
  }
}

:where(.gynecs-input, .vitals-input) {
  margin-bottom: 12px;
  label {
    width: 30%;
  }
  input {
    width: 70%;
  }
}

</style>
