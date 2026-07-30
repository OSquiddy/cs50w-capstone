<template>
  <div class="reports-main container-fluid" v-if="numVisits">
    <div class="row minH">
      <div class="col-8 p-0 report-preview-container">
        <object width="100%" height="100%" type="application/pdf" :data="pdfObjectUrl">
          <p class="d-flex pdf-error">The PDF link is corrupted</p>
        </object>
      </div>
      <div class="col-4 report-sidepanel">
        <div class="generated-reports-section">
          <div class="generated-reports-header">Generated Reports</div>
          <ol>
            <li class="report" v-for="visit, index in visitList" :key="visit.visit_number" :class="index === generatedSelected && 'active'" @click="selectGenerated($event, index, visit.visit_number)">
              Report for Visit {{ visit.visit_number }} <span class="report-date">{{ visit.date }}</span>
            </li>
          </ol>
        </div>
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
      pdfObjectUrl: null,
      pdfCache: {},
      noDataMsg: 'There are no reports for this patient at the moment.'
    }
  },
  computed: {
    patientID () {
      return this.$route.path.split('/')[2]
    },
    numVisits () {
      return this.visitList.length
    },
    activeVisitNumber () {
      return this.visitNumber ?? this.visitList[0]?.visit_number
    }
  },
  mounted () {
    this.getReports()
  },
  beforeUnmount () {
    Object.values(this.pdfCache).forEach(url => URL.revokeObjectURL(url))
    this.pdfCache = {}
    this.pdfObjectUrl = null
  },
  methods: {
    pdfDisplayUrl (blobUrl) {
      return `${blobUrl}#zoom=FitH`
    },
    async loadPdf () {
      const visitNum = this.activeVisitNumber
      if (!visitNum) return
      if (this.pdfCache[visitNum]) {
        this.pdfObjectUrl = this.pdfDisplayUrl(this.pdfCache[visitNum])
        return
      }
      const url = `${process.env.VUE_APP_API_URL}/p/${this.patientID}/v/${visitNum}/pdf`
      try {
        const response = await axios.get(url, { responseType: 'blob' })
        const blobUrl = URL.createObjectURL(response.data)
        this.$set(this.pdfCache, visitNum, blobUrl)
        this.pdfObjectUrl = this.pdfDisplayUrl(blobUrl)
      } catch (e) {
        this.pdfObjectUrl = null
      }
    },
    async getReports () {
      const response = await axios.get(process.env.VUE_APP_API_URL + '/getNumReports/' + this.patientID)
      this.visitList = response.data.completedVisits
      this.patient = response.data.patient
      await this.loadPdf()
    },
    selectGenerated (event, index, visitNumber) {
      this.generatedSelected = index
      if (this.visitNumber === visitNumber) return
      this.visitNumber = visitNumber
      this.loadPdf()
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
