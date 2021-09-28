<template>
  <div class="history-main">
    <form action="" method="post">
      <section class="past-history">
        <h2 class="section-header">Past History</h2>
        <h5 class="minor-heading">Allergies</h5>
        <div class="allergies-group section-input-group">
          <div class="allergy-input">
            <label for="allergy1">Allergy 1: </label>
            <input type="text" name="allergy1" id="allergy1">
          </div>
          <div class="allergy-input">
            <label for="allergy2">Allergy 2:</label>
            <input type="text" name="allergy2" id="allergy2">
          </div>
          <div class="allergy-input">
            <label for="allergy3">Allergy 3:</label>
            <input type="text" name="allergy3" id="allergy3">
          </div>
        </div>
        <div class="section-input-group">
          <h5 class="minor-heading" for="general">General</h5>
          <textarea name="general" id="general" cols="90" rows="4"></textarea>
        </div>
        <div class="section-input-group">
          <h5 for="surgical" class="minor-heading">Surgical History</h5>
          <textarea name="surgical" id="surgical" cols="90" rows="4"></textarea>
        </div>
      </section>
      <section class="family-history">
        <h2 class="section-header">Family History</h2>
        <div class="famIllness-group section-input-group">
          <div class="famIllness-input">
            <label for="famIllness1">Illness 1: </label>
            <input type="text" name="famIllness1" id="famIllness1">
          </div>
          <div class="allergy-input">
            <label for="famIllness2">Illness 2:</label>
            <input type="text" name="famIllness2" id="famIllness2">
          </div>
          <div class="allergy-input">
            <label for="famIllness3">Illness 3:</label>
            <input type="text" name="famIllness3" id="famIllness3">
          </div>
        </div>
      </section>
    </form>
  </div>
</template>

<script>
export default {
  name: 'History'
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

.past-history, .family-history {
  .allergies-group, .famIllness-group {
    // display: flex;
    // flex-direction: column;
    .allergy-input, .famIllness-input {
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
