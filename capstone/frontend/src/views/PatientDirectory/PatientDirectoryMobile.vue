<template>
  <div class="patient-directory-main">
    <div class="container-fluid patients-list">
      <div class="row">
        <div class="col-lg-11 mx-auto">
          <template v-for="patient in patientsList">
            <router-link :to="'/p/' + patient.id" :key="patient.id">
            <div class="row patient-small-container">
              <!-- <button class="delete-icon" @click="showModal(patient.id)">
                <img src="../../assets/cancel.svg" alt="delete-icon" />
              </button> -->
              <div class="col-3 col-sm-2 mx-sm-auto patient-photo px-0">
                <img :src="patient.profilePic ? patient.profilePic : getDefaultPic(patient)" alt="" />
              </div>
              <div class="col-9 col-sm-10 patient-info">
                <h3 class="patient-name">{{patient.first_name}} {{patient.last_name}}</h3>
                <div class="row patient-details-row">
                  <div class="col col-md-3 patient-details">ID: {{patient.id}}</div>
                  <div class="col col-md-3 patient-details">Age: {{patient.age}}yrs</div>
                </div>
                <div class="row patient-details-row">
                  <div class="col col-md-3 patient-details">Blood Type: {{patient.age}}</div>
                  <div class="col col-md-3 patient-details">Gender: {{patient.sex}}</div>
                </div>
                <div class="row patient-details-row">
                  <div class="col patient-details">Mobile: {{patient.Phone_Number}}</div>
                </div>
              </div>
            </div>
            </router-link>
          </template>
        </div>
      </div>
    </div>
    <router-link :to="'add/p'">
      <button class="new-appointment">
        <img src="../../assets/plus.svg" alt="add-symbol">
      </button>
    </router-link>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
import { defaultPic } from '../../util/util'

export default {
  name: 'PatientDirectoryMobile',
  data() {
    return {
      patientsList: []
    }
  },
  computed: {
    ...mapState('search', ['searchKeyword'])
  },
  watch: {
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
    async getPatientsList () {
      const list = await axios.get(process.env.VUE_APP_API_URL + '/patientList/name')
      this.patientsList = list.data.patientList
    },
    async getFilteredPatientsList () {
      const list = await axios.get(process.env.VUE_APP_API_URL + '/patientList/name/' + this.searchKeyword)
      this.patientsList = list.data.patientList
    },
    getDefaultPic (user) {
      return defaultPic(user)
    }
  }
}
</script>

<style lang="scss" scoped>
.patient-directory-main {
  background: var(--lightest-gray);
  padding: 20px 20px 55px;
  // height: calc(100vh - 197px);
  height: calc(100vh - 165px);
  overflow-y: scroll;
  .patients-list {
    .patient-small-container {
      display: flex;
      background: #fff;
      border-radius: 20px;
      box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.2);
      padding: 15px 5px;
      margin-bottom: 20px;
      // position: relative;
      // .delete-icon {
      //   position: absolute;
      //   top: 0;
      //   right: 0;
      //   width: fit-content;
      //   img {
      //     width: 10px;
      //   }
      // }
      .patient-photo {
        background-color: #c4c4c4;
        border-radius: 50%;
        width: 22%;
        max-width: 80px;
        aspect-ratio: 1;
        margin-left: auto;
        align-self: flex-start;
        img {
          width: 100%;
        }
      }
      .patient-info {
        // padding-bottom: 20px;
        padding-left: 1rem;
        .patient-name {
          font-size: 1.125rem;
        }
        .patient-details-row {
          margin-bottom: 3px;
          &:last-of-type {
            margin-bottom: 0;
          }
          .patient-details {
            font-size: 0.625rem;
          }
        }
      }
    }
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
}
</style>
