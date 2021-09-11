<template>
  <div class="new-appointment-main mb-4">
    <div class="page-title">Appointment</div>
    <div class="add-appointment-main">
      <div class="container-fluid">
        <form action="" method="post">
        <div class="row new-section">
          <div class="col">
            <div class="section-header">Chief Complaints</div>
            <div class="section-input">
              <textarea name="complaints" id="complaints"></textarea>
            </div>
          </div>
        </div>
        <div class="row new-section">
          <div class="col">
            <div class="section-header">Vitals</div>
            <div class="section-input input-group">
              <div class="input-group-item">
                <label for="blood-pressure">BP:</label>
                <input type="text" name="blood-pressure" id="blood-pressure" />
              </div>
              <div class="input-group-item">
                <label for="blood-pressure">SpO2:</label>
                <input type="text" name="spo2" id="spo2" />
              </div>
              <div class="input-group-item">
                <label for="blood-pressure">Pulse:</label>
                <input type="text" name="pulse" id="pulse" />
              </div>
              <div class="input-group-item">
                <label for="blood-pressure">Temp:</label>
                <input type="text" name="temp" id="temp" />
              </div>
            </div>
          </div>
        </div>
        <div class="row new-section">
          <div class="col">
            <div class="section-header">Examination</div>
            <div class="row">
              <div class="col-6">
                <div class="section-input">
                  <label for="respiratory">Respiratory:</label>
                  <textarea name="respriatory" id="respriatory"></textarea>
                </div>
              </div>
              <div class="col-6">
                <div class="section-input">
                  <label for="cereberovascular">Cereberovascular:</label>
                  <textarea name="cereberovascular" id="cereberovascular"></textarea>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-6">
                <div class="section-input">
                  <label for="cardiovascular">Cardiovascular:</label>
                  <textarea name="cardiovascular" id="cardiovascular"></textarea>
                </div>
              </div>
              <div class="col-6">
                <div class="section-input">
                  <label for="localExam">Local Examination:</label>
                  <textarea name="localExam" id="localExam"></textarea>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-6">
                <div class="section-input">
                  <label for="abdominal">Per Abdominal:</label>
                  <textarea name="abdominal" id="abdominal"></textarea>
                </div>
              </div>
              <div class="col-6">
                <div class="section-input">
                  <label for="localExam">Local Examination:</label>
                  <textarea name="localExam" id="localExam"></textarea>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row new-section">
          <div class="col">
            <div class="section-header">General</div>
            <div class="section-input general-checklist">
              <div class="row mb-2">
                <div class="form-group general-checklist-item">
                <input type="checkbox" name="pallor" id="pallor" />
                <label for="pallor">Pallor</label>
              </div>
              <div class="form-group general-checklist-item">
                <input type="checkbox" name="clubbing" id="clubbing" />
                <label for="clubbing">Clubbing</label>
              </div>
              <div class="form-group general-checklist-item">
                <input type="checkbox" name="lymphadenopathy" id="lymphadenopathy" class="general-checklist-item" />
                <label for="lymphadenopathy">Lymphadenopathy</label>
              </div>
              </div>
              <div class="row">
              <div class="form-group general-checklist-item">
                <input type="checkbox" name="icterus" id="icterus" />
                <label for="icterus">Icterus</label>
              </div>
                <div class="form-group general-checklist-item">
                <input type="checkbox" name="koilonychia" id="koilonychia" />
                <label for="koilonychia">Koilonychia</label>
              </div>
              <div class="form-group general-checklist-item">
                <input type="checkbox" name="oedema" id="oedema" class="general-checklist-item" />
                <label for="oedema">Oedema</label>
              </div>
              </div>
            </div>
            <div class="section-input my-3">
              <div class="input-group-item">
                <label for="others">Others:</label>
                <textarea name="others" id="others"></textarea>
              </div>
            </div>
          </div>
        </div>
        <div class="row new-section">
          <div class="col">
            <div class="section-header">Probable Diagnosis</div>
            <div class="section-input">
              <textarea name="diagnosis" id="diagnosis"></textarea>
            </div>
          </div>
        </div>
        <input type="submit" value="Save" @click.prevent="submitForm" class="save-button">
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style lang="scss" scoped>
.page-title {
  margin-top: 15px;
}
.add-appointment-main {
  background-color: var(--background-primary);
  padding: 1rem;
  margin-top: 15px;
  border-radius: 0.75rem;
}

.new-section {
  margin-bottom: 30px;
  .section-header {
    margin-bottom: 15px;
  }
  .section-input {
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
  .input-group {
    // justify-content: space-evenly;
    .input-group-item {
      margin-right: 25px;
      label {
        font-size: 0.875rem;
        margin-right: 15px;
      }
      input {
        border-radius: 0.375rem;
        width: 150px;
      }
    }
  }
   .general-checklist-item {
     display: flex;
     align-items: center;
     width: 20%;
      label {
      font-size: 0.875rem;
        margin-left: 0.625rem;
      }
      input[type="checkbox"] {
      font-size: 0.875rem;
        width: fit-content;
      }
    }
}

.save-button {
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
  margin-left: auto;
  // position: sticky;
  // top: 20px;
  // right: 0;
}
</style>
