<template>
  <div class="container patient-small-container">
    <div class="row patient-name-container">
        <h3 class="patient-name">{{name}}</h3>
    </div>
    <div class="row patient-info-container">
    <div class="col-3">
      <div class="patient-photo"></div>
    </div>
    <div class="col-9 patient-info">
      <div class="row patient-details-row">
        <div class="col patient-details">ID: {{id}}</div>
        <div class="col patient-details">Age: {{age}}yrs</div>
      </div>
      <div class="row patient-details-row">
        <div class="col patient-details">Blood Type: {{bloodType}}</div>
        <div class="col patient-details">Gender: {{gender}}</div>
      </div>
      <div class="row patient-details-row">
        <div class="col patient-details">Mobile: {{mobile}}</div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'PatientSmall',
  props: {
    name: {
      type: String
    },
    id: {
      type: Number
    },
    age: {
      type: Number
    },
    bloodType: {
      type: String
    },
    gender: {
      type: String
    },
    mobile: {
      type: String
    }
  }
}
</script>

<style lang="scss" scoped>
.patient-small-container {
  // display: flex;
  background: #f4f4f4;
  border-radius: 20px;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.2);
  // padding: 0 5px;
  margin-bottom: 20px;
  overflow: hidden;
  .patient-name-container {
    margin: 0 -1.5rem 0.25rem;
    .patient-name {
      font-size: 1.125rem;
      text-align: center;
      background-color: var(--primary-accent-light);
      padding: 7px 0;
      color: white;
    }
  }
  .patient-info-container {
    padding-bottom: 10px;
    .patient-photo {
    background-color: #c4c4c4;
    border-radius: 50%;
    // width: 22%;
    aspect-ratio: 1;
    // margin-left: auto;
    align-self: flex-start;
  }
  .patient-info {
    // padding-bottom: 20px;
    // padding-left: 1rem;
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
</style>
