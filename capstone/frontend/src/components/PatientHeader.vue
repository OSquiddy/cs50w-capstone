<template>
  <div class="patient-header container-fluid">
    <div class="patient-image">
      <div class="image"></div>
    </div>
    <div class="patient-info-container">
      <div class="patient-title">
        Ronald Weasley, 17, M
      </div>
      <div class="patient-address">
        The Burrow, St. Ottery Catchpole
        <br>
        UK
      </div>
      <div class="patient-meta">
        <div class="patient-dob">31/04/1980</div>
        <div class="patient-mobile">+1 324 (634) 4295</div>
        <div class="patient-email">roonil_wazlib@hogwarts.com</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PatientHeader',
  data () {
    return {}
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
