<template>
  <div>
    <div class="grid-container">
      <div class="grid-item">Duty Schedule</div>
      <router-link to="/appointments">
        <div class="grid-item">Appointments</div>
      </router-link>
      <router-link to="/directory">
      <div class="grid-item">Patient Directory</div>
      </router-link>
      <div class="grid-item">Settings</div>
      <div class="grid-item">Dev Support</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainContainer',
  data() {
    return {
    }
  }
}
</script>

<style lang="scss" scoped>
.grid-container {
  display: grid;
  justify-content: center;
  grid-template-columns: repeat(auto-fill, 145px);
  grid-gap: 18px;
  a {
    text-decoration: none;
    color: var(--primary-text-color);
  }
  .grid-item {
    background: #c4c4c4;
    height: 145px;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
</style>
