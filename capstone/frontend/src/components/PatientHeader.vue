<template>
  <div class="patient-header container-fluid">
    <div class="patient-image">
      <div class="image"></div>
    </div>
    <div class="patient-info-container">
      <div class="patient-title">
        {{patient.fullname}}, {{patient.age}}, {{patient.sex}}
      </div>
      <div class="patient-address">
        {{patient.address}}
        <br>
        UK
      </div>
      <div class="patient-meta">
        <div class="patient-dob">{{patient.date_of_birth}}</div>
        <div class="patient-mobile">{{patient.Phone_Number}}</div>
        <div class="patient-email">{{patient.email}}</div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'PatientHeader',
  data () {
    return {}
  },
  computed: {
    ...mapState(['patient'])
  }
}
</script>

<style lang="scss" scoped>

.patient-image {
  margin-right: 1.5rem;
  .image {
    background: var(--medium-gray);
    width: 80px;
    height: 80px;
    border-radius: 50%;
  }
}

.patient-header {
  background: #FFF;
  border-top: 1px solid #eee;
  display: flex;
  align-items: center;
  padding: 20px;
}

.patient-title {
  font-size: 1.125rem;
}

.patient-address {
  font-size: 0.75rem;
  color: #515151;
}

.patient-meta, .patient-meta > * {
  display: flex;
  font-size: 0.75rem;
}

:where(.patient-mobile, .patient-dob) {
  margin-right: 1rem;
}
</style>
