<template>
  <div class="patient-directory-main">
    <input type="text" class="search" placeholder="Search by name or id" v-model="keyword">
    <div class="page-title">Patients</div>
    <div class="directory-container">
      <table class="patients-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>EMAIL</th>
            <th>LAST VISIT</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="patient in patientsList" :key="patient.id">
            <td>{{patient.id}}</td>
            <td>
              <div class="patient-name">
                <div class="patient-img"><img src="" alt=""></div>
                {{patient.fullname}}
              </div>
            </td>
            <td>{{patient.email}}</td>
            <td>04-06-2021</td>
          </tr>
          </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import axios from 'axios'
import { debounce } from '../../util/util'
export default {
  name: 'PatientDirectory',
  data() {
    return {
      keyword: null,
      patientsList: []
    }
  },
  computed: {
    ...mapState('search', ['searchKeyword'])
  },
  watch: {
    keyword () {
      this.debounceInput()
    },
    searchKeyword() {
      if (this.searchKeyword !== '') {
        this.getFilteredPatientsList()
      } else {
        this.getPatientsList()
      }
    }
  },
  mounted () {
    this.getPatientsList()
  },
  methods: {
    ...mapActions('search', ['updateSearchKeyWord']),
    debounceInput: debounce(function (e) {
      this.updateSearchKeyWord(this.keyword)
    }, 250),
    async getPatientsList () {
      const list = await axios.get(process.env.VUE_APP_API_URL + '/patientList/id')
      this.patientsList = list.data.patientList
    },
    async getFilteredPatientsList () {
      const list = await axios.get(process.env.VUE_APP_API_URL + '/patientList/id/' + this.searchKeyword)
      this.patientsList = list.data.patientList
    }
  }

}
</script>

<style lang="scss" scoped>
.directory-container {
  background-color: var(--background-primary);
  padding: 1rem;
  margin-top: 15px;
  border-radius: 0.75rem;
  min-height: calc(100vh - 200px);
  margin-bottom: 20px;
}

.search {
  border: 1px solid #99A1A6;
  background: transparent;
  border-radius: 0.375rem;
  padding: 5px 10px;
  width: 300px;
  margin-top: 30px;
}

.page-title {
  margin-top: 15px;
}

.patients-table {
  width: 100%;
  th, td {
    text-align: center;
    padding: 0.625rem 0;
    font-weight: 400;
  }
  th {
    font-size: 1.125rem;
  }
  td:nth-child(2) {
    text-align: left;
  }
  tr {
    border-bottom: 1px solid #BBB;
  }
  tbody tr:last-child {
    border-bottom: none;
  }
  .patient-name {
    display: flex;
    align-items: center;
    padding: 0.25rem 0.5rem;
    .patient-img {
      background: var(--medium-gray);
      width: 2rem;
      height: 2rem;
      border-radius: 50%;
      margin-right: 15px;
      margin-left: 20%;
    }
  }
}
</style>
