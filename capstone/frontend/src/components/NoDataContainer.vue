<template>
  <div class="no-data-main">
    <div class="no-data-text">{{ displayText }}</div>
  </div>
</template>

<script>
export default {
  name: 'NoDataContainer',
  props: {
    displayText: String
  }
}
</script>

<style lang="scss" scoped>
.no-data-main {
  background: var(--light-gray);
  height: 250px;
  width: 100%;
  display: flex;
  justify-content: center;
  border-radius: 5px;
  .no-data-text {
    font-family: 'Roboto';
    color: var(--primary-text-color);
    opacity: 0.8;
    font-size: 1.125rem;
    display: flex;
    align-self: center;
  }
}

@media screen and (min-width: 1200px) {
  .no-data-main {
    margin-top: 30px;
    background: var(--background-primary);
  }
}
</style>
