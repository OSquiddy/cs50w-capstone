<template>
  <div class="patient-directory-main">
    <div class="container patients-list">
      <!-- <div v-for="item in items" :key="item.id">
        {{ item }}
      </div> -->
      <!-- This entire row will be one component or it will be repeated in v-for as is -->
      <div class="row patient-small-container">
        <div class="col-3 patient-photo"></div>
        <div class="col-9 patient-info">
          <h3 class="patient-name">Ronald Weasley</h3>
          <div class="row patient-details-row">
            <div class="col patient-details">ID: 2453</div>
            <div class="col patient-details">Age: 17yrs</div>
          </div>
          <div class="row patient-details-row">
            <div class="col patient-details">Blood Type: O+</div>
            <div class="col patient-details">Gender: Male</div>
          </div>
          <div class="row patient-details-row">
            <div class="col patient-details">Mobile: +1 2092001356</div>
          </div>
        </div>
      </div>
      <!-- This entire row will be one component or it will be repeated in v-for as is -->
      <div class="row patient-small-container">
        <div class="col-3 patient-photo"></div>
        <div class="col-9 patient-info">
          <h3 class="patient-name">Harry Potter</h3>
          <div class="row patient-details-row">
            <div class="col patient-details">ID: 2453</div>
            <div class="col patient-details">Age: 17yrs</div>
          </div>
          <div class="row patient-details-row">
            <div class="col patient-details">Blood Type: O+</div>
            <div class="col patient-details">Gender: Male</div>
          </div>
          <div class="row patient-details-row">
            <div class="col patient-details">Mobile: +1 2092001356</div>
          </div>
        </div>
      </div>
      <!-- This entire row will be one component or it will be repeated in v-for as is -->
      <div class="row patient-small-container">
        <div class="col-3 patient-photo"></div>
        <div class="col-9 patient-info">
          <h3 class="patient-name">Hermione Granger</h3>
          <div class="row patient-details-row">
            <div class="col patient-details">ID: 2453</div>
            <div class="col patient-details">Age: 17yrs</div>
          </div>
          <div class="row patient-details-row">
            <div class="col patient-details">Blood Type: O+</div>
            <div class="col patient-details">Gender: Male</div>
          </div>
          <div class="row patient-details-row">
            <div class="col patient-details">Mobile: +1 2092001356</div>
          </div>
        </div>
      </div>
    </div>
    <button class="new-appointment">
      <img src="../../assets/plus.svg" alt="add-symbol">
    </button>
  </div>
</template>

<script>
export default {
  name: 'PatientDirectory',
  data() {
    return {}
  }
}
</script>

<style lang="scss" scoped>
.patient-directory-main {
  padding: 20px 20px 55px;
  height: calc(100vh - 197px);
  overflow-y: scroll;
  .patients-list {
    .patient-small-container {
      display: flex;
      background: #f4f4f4;
      border-radius: 20px;
      box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.2);
      padding: 15px 5px;
      margin-bottom: 20px;
      // margin: 0 20px;
      // &:first-of-type {
      //   margin-top: 20px;
      // }
      .patient-photo {
        background-color: #c4c4c4;
        border-radius: 50%;
        width: 22%;
        aspect-ratio: 1;
        margin-left: auto;
        align-self: flex-start;
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
