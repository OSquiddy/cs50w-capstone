<template>
  <div class="history-main">
    <form action="" method="post">
      <section class="past-history">
        <h2 class="section-header">Past History</h2>
        <h5 class="minor-heading">Allergies</h5>
        <div class="allergies-group section-input-group" v-if="edit">
          <div class="allergy-input">
            <label for="allergy1">Allergies: </label>
            <textarea name="allergy" id="allergy"></textarea>
          </div>
        </div>
        <ul class="allergies" v-else>
          <li class="allergy" v-for="allergy in allergies" :key="allergy">
            {{allergy}}
          </li>
        </ul>
          <h5 class="minor-heading" for="general">General</h5>
        <div class="section-input-group" v-if="edit">
          <textarea name="general" id="general" cols="90" rows="4"></textarea>
        </div>
        <div class="common-illnesses">
          <input type="checkbox" name="t2dm" id="t2dm" :disabled="!edit" :checked="history.t2dm">
          <label for="t2dm">T2DM</label>
        </div>
        <div class="common-illnesses">
          <input type="checkbox" name="heart_disease" id="heart_disease" :disabled="!edit" :checked="history.heart_disease">
          <label for="heart_disease">Heart Disease</label>
        </div>
        <div class="common-illnesses">
          <input type="checkbox" name="hypothyroidism" id="hypothyroidism" :disabled="!edit" :checked="history.hypothyroidism">
          <label for="hypothyroidism">Hypothyroidism</label>
        </div>
        <div class="common-illnesses">
          <input type="checkbox" name="kidney_disease" id="kidney_disease" :disabled="!edit" :checked="history.kidney_disease">
          <label for="kidney_disease">Chronic Kidney Disease</label>
        </div>
        <div class="common-illnesses">
          <input type="checkbox" name="cardiovascular_disease" id="cardiovascular_disease" :disabled="!edit" :checked="history.cardiovascular_disease">
          <label for="cardiovascular_disease">Cardiovascular Disease</label>
        </div>
        <div class="general" v-if="!edit">
          {{history.general}} There was no general info
        </div>
        <div class="section-input-group" v-if="edit">
          <h5 for="surgical" class="minor-heading">Surgical History</h5>
          <textarea name="surgical" id="surgical" cols="90" rows="4"></textarea>
        </div>
        <div class="surgeries" v-if="!edit && history.surgeries">
          {{history.surgeries}} are not present
        </div>
      </section>
      <section class="family-history">
        <h2 class="section-header">Family History</h2>
        <div class="famIllness-group section-input-group" v-if="edit">
          <div class="famIllness-input">
            <label for="famIllness">Illnesses: </label>
            <textarea name="famIllness" id="famIllness"></textarea>
          </div>
        </div>
        <ul class="allergies" v-else>
          <li class="allergy" v-for="allergy in allergies" :key="allergy">
            {{allergy}}
          </li>
        </ul>
      </section>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
export default {
  name: 'History',
  data() {
    return {
      history: {
        general: null,
        surgeries: null
      },
      allergies: [],
      familyIllnesses: [],
      edit: false
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
      this.history = response.data.history
      this.history.allergies.split(/\r?\n/).map((line) => { this.allergies.push(line) })
    }
  }
}
</script>

<style lang="scss" scoped>
.history-main {
  background-color: var(--background-primary);
  padding: 1rem;
  margin-top: 30px;
  border-radius: 0.75rem;
  border: 1px transparent;
}

section {
  margin-bottom: 25px;
  .section-header {
    font-size: 1.25rem;
    font-weight: 400;
  }
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
  .section-input-group {
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
      margin-bottom: 15px;
      label {
        width: 100px;
      }
    }
  }
}
</style>
