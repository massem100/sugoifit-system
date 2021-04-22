<template>
  <div class="d-flex flex-row">
    <div class="ml-5">
      <top-bar class="top-bar"/>
      <h3 class="m-2">Settings</h3>
      <settings-top/>
    </div>

  </div>
</template>

<script>
export default {
    name: "Settings",
    layout: 'dashboard'
};
</script>

<style scoped>

.box {
  width: 130px;
  height: 120px;
  text-align: center;
  font-size: 30px;
}
</style>