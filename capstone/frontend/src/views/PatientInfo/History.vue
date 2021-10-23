<template>
  <div class="history-main">
    <form action="" method="post" @submit.prevent="submitForm">
      <h5 class="section-header">
        Past History
        <img src="../../assets/edit.svg" alt="edit-icon" class="edit-icon" @click="toggleGeneralEdit" />
      </h5>
      <section class="past-history container-fluid">
        <div class="row">
          <div class="col-2 history-type">General :</div>
          <div class="col-10">
            <div class="row section-info-row">
              <div class="col-4">
                <div class="common-illnesses">
                  <input type="checkbox" name="t2dm" id="t2dm" v-if="generalEdit" v-model="history.t2dm" />
                  <label for="t2dm">
                    T2DM
                    <span class="icon" v-if="!generalEdit">
                      :
                      <template v-if="history.t2dm">&#x2714;</template>
                      <template v-else>&#x2716;</template>
                    </span>
                  </label>
                </div>
                <div class="common-illnesses">
                  <input type="checkbox" name="heart_disease" id="heart_disease" v-if="generalEdit" v-model="history.heart_disease" />
                  <label for="heart_disease">
                    Heart Disease
                    <span class="icon" v-if="!generalEdit">
                      :
                      <template v-if="history.heart_disease">&#x2714;</template>
                      <template v-else>&#x2716;</template>
                    </span>
                  </label>
                </div>
              </div>
              <div class="col-4">
                <div class="common-illnesses">
                  <input type="checkbox" name="hypothyroidism" id="hypothyroidism" v-if="generalEdit" v-model="history.hypothyroidism" />
                  <label for="hypothyroidism">
                    Hypothyroidism
                    <span class="icon" v-if="!generalEdit">
                      :
                      <template v-if="history.hypothyroidism">&#x2714;</template>
                      <template v-else>&#x2716;</template>
                    </span>
                  </label>
                </div>
                <div class="common-illnesses">
                  <input type="checkbox" name="kidney_disease" id="kidney_disease" v-if="generalEdit" v-model="history.chronic_kidney_disease" />
                  <label for="kidney_disease">
                    Chronic Kidney Disease
                    <span class="icon" v-if="!generalEdit">
                      :
                      <template v-if="history.chronic_kidney_disease">&#x2714;</template>
                      <template v-else>&#x2716;</template>
                    </span>
                  </label>
                </div>
              </div>
              <div class="col-4">
                <div class="common-illnesses">
                  <input type="checkbox" name="cardiovascular_disease" id="cardiovascular_disease" v-if="generalEdit" v-model="history.cardiovascular_disease" />
                  <label for="cardiovascular_disease">
                    Cardiovascular Disease
                    <span class="icon" v-if="!generalEdit">
                      :
                      <template v-if="history.cardiovascular_disease">&#x2714;</template>
                      <template v-else>&#x2716;</template>
                    </span>
                  </label>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-2 history-type">Allergies :</div>
          <div class="col-10">
            <div class="row section-info-row" v-if="generalEdit">
              <div class="col">
                <textarea name="allergies" id="allergies" class="section-input-group" v-model="history.allergies"></textarea>
              </div>
            </div>
            <div class="row" v-else>
              <div class="col">
                <ul class="allergies">
                  <li class="allergy" v-for="allergy in allergies" :key="allergy">
                    {{ allergy }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-2 history-type">Surgical History :</div>
          <div class="col-10">
            <div class="row section-info-row" v-if="generalEdit">
              <div class="col">
                <textarea name="surgeries" id="surgeries" class="section-input-group" v-model="history.surgeries"></textarea>
              </div>
            </div>
            <div class="row" v-else>
              <div class="col">
                <ul class="surgeries">
                  <li class="surgery" v-for="surgery in surgicalHistory" :key="surgery">
                    {{ surgery }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-2 history-type">Drug History :</div>
          <div class="col-10">
            <div class="row section-info-row" v-if="generalEdit">
              <div class="col">
                <textarea name="drugHistory" id="drugHistory" class="section-input-group" v-model="history.drugs"></textarea>
              </div>
            </div>
            <div class="row" v-else>
              <div class="col">
                <ul class="drug-history">
                  <li class="drug" v-for="drug in drugHistory" :key="drug">
                    {{ drug }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-2 history-type">Other :</div>
          <div class="col-10">
            <div class="row section-info-row" v-if="generalEdit">
              <div class="col">
                <textarea name="general" id="general" class="section-input-group" v-model="history.general"></textarea>
              </div>
            </div>
            <div class="row" v-else>
              <div class="col">
                <ul class="general-history">
                  <li class="general-item" v-for="item in generalHistory" :key="item">
                    {{ item }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div class="container-fluid">
          <div class="row">
            <div class="col d-flex">
              <input type="button" value="Cancel" @click="toggleGeneralEdit" class="cancel-button" v-if="generalEdit" />
              <input type="submit" value="Save" class="save-button" v-if="generalEdit" />
            </div>
          </div>
        </div>
      </section>
      <h5 class="section-header">
        Family History
        <img src="../../assets/edit.svg" alt="edit-icon" class="edit-icon" @click="toggleFamilyEdit" />
      </h5>
      <section class="family-history container-fluid">
        <div class="row">
          <div class="col-2 history-type">Familial Tendencies :</div>
          <div class="col-10">
            <div class="row section-info-row" v-if="familyEdit">
              <div class="col">
                <textarea name="famIllness" id="famIllness" class="section-input-group" v-model="history.family"></textarea>
              </div>
            </div>
            <div class="row" v-else>
              <div class="col">
                <ul class="allergies">
                  <li class="famIllness" v-for="famIllness in familyHistory" :key="famIllness">
                    {{ famIllness }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div class="container-fluid">
          <div class="row">
            <div class="col d-flex">
              <input type="button" value="Cancel" @click="toggleFamilyEdit" class="cancel-button" v-if="familyEdit" />
              <input type="submit" value="Save" class="save-button" v-if="familyEdit" />
            </div>
          </div>
        </div>
      </section>
    </form>
  </div>
</template>

<script>
/* eslint-disable dot-notation */
import axios from 'axios'
import { mapState } from 'vuex'
import { Snackbar } from '../../util/util'

export default {
  name: 'History',
  data() {
    return {
      history: {
        general: null,
        surgeries: null,
        allergies: null,
        drugs: null,
        family: null,
        t2dm: false,
        chronic_kidney_disease: false,
        cardiovascular_disease: false,
        heart_disease: false,
        hypothyroidism: false
      },
      allergies: [],
      familyHistory: [],
      surgicalHistory: [],
      drugHistory: [],
      generalHistory: [],
      generalEdit: false,
      familyEdit: false
    }
  },
  computed: {
    ...mapState(['patient'])
  },
  mounted() {
    this.getPatientHistory()
  },
  methods: {
    async getPatientHistory() {
      const response = await axios.get(process.env.VUE_APP_API_URL + '/history/' + this.patient.id)
      if (response.data) {
        this.history = response.data.history
      }
      try {
        this.generateListFromText()
      } catch (error) {
        console.log('Inner Error')
      }
    },
    generateListFromText () {
      this.allergies = []
      this.surgicalHistory = []
      this.drugHistory = []
      this.familyHistory = []
      this.generalHistory = []
      if (this.history.allergies) {
        this.history.allergies.split(/\r?\n/).map((line) => {
          this.allergies.push(line)
        })
      } else {
        this.allergies.push('N/A')
      }
      if (this.history.surgeries) {
        this.history.surgeries.split(/\r?\n/).map((line) => {
          this.surgicalHistory.push(line)
        })
      } else {
        this.surgicalHistory.push('N/A')
      }
      if (this.history.general) {
        this.history.general.split(/\r?\n/).map((line) => {
          this.generalHistory.push(line)
        })
      } else {
        this.generalHistory.push('N/A')
      }
      if (this.history.family) {
        this.history.family.split(/\r?\n/).map((line) => {
          this.familyHistory.push(line)
        })
      } else {
        this.familyHistory.push('N/A')
      }
      if (this.history.drugs) {
        this.history.drugs.split(/\r?\n/).map((line) => {
          this.drugHistory.push(line)
        })
      } else {
        this.drugHistory.push('N/A')
      }
    },
    toggleGeneralEdit() {
      this.generalEdit = !this.generalEdit
    },
    toggleFamilyEdit() {
      this.familyEdit = !this.familyEdit
    },
    async submitForm() {
      const formData = {
        t2dm: this.history.t2dm,
        kidney_disease: this.history.chronic_kidney_disease,
        cardiovascular_disease: this.history.cardiovascular_disease,
        heart_disease: this.history.heart_disease,
        hypothyroidism: this.history.hypothyroidism,
        general: this.history.general,
        surgeries: this.history.surgeries,
        allergies: this.history.allergies,
        drugs: this.history.drugs,
        family: this.history.family
      }
      // console.log(formData)
      try {
        const response = await axios.post(process.env.VUE_APP_API_URL + '/history/' + this.patient.id, formData)
        if (response.status === 200) {
          Snackbar('Settings Updated', 'var(--success)')
          this.history = response.data.history
          this.generateListFromText()
          this.generalEdit = false
          this.familyEdit = false
        }
      } catch (error) {
        console.log(error)
        Snackbar('Update Unsuccessful', 'var(--error-text')
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.history-main {
}

.section-header {
  font-size: 1rem;
  text-transform: uppercase;
  font-weight: 400;
  display: flex;
  margin-top: 30px;
  opacity: 0.8;
  // border: 1px solid purple;
}

section {
  margin-bottom: 25px;
  background-color: var(--background-primary);
  padding: 1rem;
  // margin-top: 30px;
  border-radius: 0.75rem;
  border: 1px transparent;
  .minor-heading {
    font-size: 1.125rem;
    font-weight: 400;
  }
  // .section-input-group {
  //   margin-bottom: 12px;
  //   label {
  //     // width: 100%;
  //     font-size: 0.875rem;
  //   }
  //   input {
  //     background: var(--light-gray);
  //     border: none;
  //     outline: none;
  //     width: 50%;
  //     padding: 5px 10px;
  //     color: var(--input-text-color);
  //     border-radius: 5px;
  //     margin-top: 5px;
  //     &:focus {
  //       border-bottom: 1px solid var(--focus-blue);
  //       border-bottom-left-radius: 0;
  //       border-bottom-right-radius: 0;
  //     }
  //   }
  // }
  input,
  textarea {
    border-radius: 0.625rem;
    padding: 5px 10px;
    border: 1px solid var(--input-border-color);
    font-size: 0.875rem;
  }
  textarea {
    width: 100%;
    height: 120px;
  }
  label {
    font-size: 0.875rem;
  }
}

.past-history,
.family-history {
  .allergies-group,
  .famIllness-group {
    // display: flex;
    // flex-direction: column;
    .allergy-input,
    .famIllness-input {
      // width: fit-content;
      justify-content: space-between;
      // border: 1px solid;
      // margin-bottom: 15px;
      label {
        width: 100px;
      }
    }
  }
}

.section-info-row {
  margin-bottom: 15px;
  .common-illnesses {
    margin-bottom: 10px;
    label {
      margin-left: 5px;
    }
  }
}

.history-type {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 15px;
}

.edit-icon {
  cursor: pointer;
  display: flex;
  margin-left: auto;
}

.save-button,
.cancel-button {
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
</style>
