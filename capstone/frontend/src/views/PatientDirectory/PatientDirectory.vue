<template>
  <div class="patient-directory-main">
    <input type="text" class="search" placeholder="Search by name or id" v-model="keyword" />
    <div class="page-title">Patients</div>
    <div class="directory-container">
      <table class="patients-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>EMAIL</th>
            <th>GENDER</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <template v-for="patient in patientsList">
            <tr :key="patient.id">
              <router-link :to="'/p/' + patient.id" class="patient-link">
                <td>{{ patient.id }}</td>
                <td>
                  <div class="patient-name">
                    <div class="patient-img"><img :src="patient.profilePic ? patient.profilePic : getDefaultPic(patient)" alt="" /></div>
                    {{ patient.fullname }}
                  </div>
                </td>
                <td>{{ patient.email }}</td>
                <td>{{ patient.sex }}</td>
              </router-link>
              <td>
                <button class="delete-icon" @click="showModal(patient.id)">
                  <img src="../../assets/cancel.svg" alt="delete-icon" />
                </button>
              </td>
            </tr>
          </template>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import axios from 'axios'
import { Modal } from 'bootstrap'
import { debounce, Snackbar, defaultPic } from '../../util/util'
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
    keyword() {
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
  mounted() {
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
    },
    async deleteUser (id) {
      try {
        const response = await axios.post(process.env.VUE_APP_API_URL + '/delete/p/' + id)
        if (response.status === 200) {
          Snackbar(`Deleted user: ${response.data.patient.fullname}`, 'var(--success)')
          this.getPatientsList()
        } else {
          Snackbar('Error: User not deleted', 'var(--error-text)')
        }
      } catch (error) {
        Snackbar('Error: User not deleted', 'var(--error-text)')
      }
    },
    showModal (id) {
      const myModal = new Modal(document.getElementById('myModal'))
      myModal.show()
      const modalBody = 'Are you sure you want to delete this user?'
      document.querySelector('.modal-body').innerText = modalBody
      document.querySelector('.modal-delete').onclick = () => {
        this.deleteUser(id)
        myModal.hide()
      }
    },
    getDefaultPic (user) {
      return defaultPic(user)
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
  border: 1px solid #99a1a6;
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
  .patient-link {
    display: contents;
  }
  th,
  td {
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
  thead tr {
    border-bottom: 1px solid #bbb;
  }
  tbody td {
    vertical-align: middle;
  }
  tbody tr:hover {
    background: var(--light-gray);
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
      img {
        width: 100%;
      }
    }
  }
}

.delete-icon {
  padding: 10px;
  img {
    width: 10px;
  }
  // padding: 10px;
}
</style>
