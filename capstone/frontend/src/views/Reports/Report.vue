<template>
  <div class="reports-main container-fluid" v-if="numVisits">
    <div class="row minH">
      <div class="col-8 p-0 report-preview-container">
        <!-- <div class="report-preview"></div> -->
        <!-- <embed width="100%" height="100%" src="../../assets/Omar CV.pdf" type="application/pdf" /> -->
        <object width="100%" height="100%" type="application/pdf" :data="`../../assets/pdf/${patientID}/Generated/${patient.fullname} - Report ${visitNumber ? visitNumber : numVisits}.pdf#zoom=43%`">
          <p class="d-flex pdf-error">The PDF link is corrupted</p>
        </object>
      </div>
      <div class="col-4 report-sidepanel">
        <div class="generated-reports-section">
          <div class="generated-reports-header">Generated Reports</div>
          <ol>
            <!-- <li class="generated-report report" v-for="visit, index in visitList" :key="visit.visit_number" @click="selectGenerated($event, index, visit.visit_number)">
              Report for Visit {{visit.visit_number}} <span class="report-date">{{visit.date}}</span>
            </li> -->
            <li class="report" v-for="visit, index in visitList" :key="visit.visit_number" :class="index === generatedSelected  && 'active'" @click="selectGenerated($event, index, visit.visit_number)">
              Report for Visit {{visit.visit_number}} <span class="report-date">{{visit.date}}</span>
            </li>
          </ol>
        </div>
        <!-- <div class="uploaded-reports-section">
          <div class="uploaded-reports-header">Uploaded Reports</div>
          <ol>
            <li class="uploaded-report report">Report for Visit 5 <span class="report-date">05-09-2021</span></li>
            <li class="uploaded-report report">Report for Visit 4 <span class="report-date">05-09-2021</span></li>
            <li class="uploaded-report report">Report for Visit 3 <span class="report-date">05-09-2021</span></li>
            <li class="uploaded-report report">Report for Visit 2 <span class="report-date">05-09-2021</span></li>
            <li class="uploaded-report report">Report for Visit 1 <span class="report-date">05-09-2021</span></li>
          </ol>
        </div> -->
      </div>
    </div>
  </div>
  <div v-else>
      <NoDataContainer :displayText="noDataMsg" />
  </div>
</template>

<script>
import axios from 'axios'
import NoDataContainer from '../../components/NoDataContainer.vue'
export default {
  name: 'Reports',
  components: {
    NoDataContainer
  },
  data () {
    return {
      visitList: [],
      patient: {},
      visitNumber: null,
      generatedSelected: 0,
      counter: 0,
      noDataMsg: 'There are no reports for this patient at the moment.'
    }
  },
  computed: {
    patientID () {
      return this.$route.path.split('/')[2]
    },
    numVisits () {
      return this.visitList.length
    }
  },
  watch: {
    generatedSelected(newValue, oldValue) {
      // document.querySelectorAll('.generated-report')[oldValue].classList.remove('active')
    }
  },
  mounted () {
    this.getReports()
    if (this.visitList.length) {
      // document.querySelectorAll('.generated-report')[0].classList.add('active')
    }
  },
  methods: {
    async getReports () {
      const response = await axios.get(process.env.VUE_APP_API_URL + '/getNumReports/' + this.patientID)
      this.visitList = response.data.completedVisits
      this.patient = response.data.patient
    },
    selectGenerated (event, index, visitNumber) {
      // console.log(event.target, index)
      this.generatedSelected = index
      // event.target.classList.add('active')
      this.visitNumber = visitNumber
    }
  }
}
</script>

<style lang="scss" scoped>
.reports-main {
  background-color: var(--background-primary);
  margin-top: 30px;
  border-radius: 0.75rem;
  min-height: calc(100vh - 270px);
  margin-bottom: 30px;
}

.minH {
  min-height: inherit;
  height: inherit;
}

.report-preview-container {
  background-color: #525659;
  height: inherit;
  justify-content: center;
  display: flex;
  align-items: center;
  // padding: 2rem 0;
  border-top-left-radius: 0.75rem;
  border-bottom-left-radius: 0.75rem;
  object, embed {
    border-top-left-radius: 0.75rem;
    border-bottom-left-radius: 0.75rem;
    .pdf-error {
      align-items: center;
      justify-content: center;
      height: 100%;
      margin: auto;
      color: white;
      font-size: 1.25rem;
      font-family: 'Roboto', sans-serif;
    }
  }
}

.report-sidepanel {
  height: max-content;
}

.generated-reports-section, .uploaded-reports-section {
  margin-top: 10px;
  .generated-reports-header, .uploaded-reports-header {
    font-size: 1.125rem;
    font-weight: 500;
  }
  ol {
    list-style: decimal inside;
    margin-top: 20px;
    margin-bottom: 30px;
    padding-left: 0;
    .report {
      padding: 0.5rem 1rem;
      cursor: pointer;
      margin-bottom: 10px;
      border-radius: 5px;
      border: 1px solid transparent;
      &:hover {
        // transform: scale(1.03);
        transition: 0.3s ease-out;
         &, .report-date {
          color: var(--button-blue);
        }
      }
      .report-date {
        float: right;
        display: inline-flex;
      }
    }
    .active {
      border-color: var(--button-blue);
      &, .report-date {
        color: var(--button-blue);
      }
    }
  }
}
</style>
