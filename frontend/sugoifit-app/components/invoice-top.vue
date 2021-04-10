<template>
  <div class="d-flex flex-row py-2 text-center flex-wrap">

    <b-link class="btnStyle pop-link" :to="{name:'invoice-create'}">
      <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon>
      <span> Product </span>
    </b-link>

    <b-link class="btnStyle pop-link" :to="{name:'invoice-create'}">
      <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon>
      <span> Service </span>
    </b-link>

  </div>
</template>

<script>
    export default {
        name: "invoice-top"
    }
</script>

<style scoped>
  .btnStyle {
    margin: 5px;
    background-color: #DFFBFF;
    width: 10rem;
    padding: 10px;
    display: flex;
    flex-direction: column;
    text-decoration: none !important;
    color: #222222;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    border: none;
  }
</style>
