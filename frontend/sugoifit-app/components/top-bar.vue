<template>
  <div class="top-bar">
    <div class="d-flex align-items-center mr-3">
      <h6 class="m-2">Jane S.</h6>
      <img class="m-2" id="top-user-icon" src="~assets/uploads/Profile_icon.svg" alt="">
      <img class="m-2" src="~assets/uploads/settings.svg" alt="">
    </div>
  </div>
</template>

<script>
    export default {
        name: "top-bar",
    }
</script>

<style scoped>
  .top-bar {
    width: 100%;
    display: flex;
    justify-content: flex-end;
    align-items: center;
  }
</style>
