<template>
  <div class="d-flex flex-row py-2 text-center flex-wrap">

    <b-link class="btnStyle pop-link" :to="{name:'settings-profile-create'}">
        <span> Your Profile</span>
    </b-link>
    <b-link class="btnStyle pop-link" :to="{name:'settings-business-create'}">
        <span> Your Company</span>
    </b-link>
    <b-link class="btnStyle pop-link" :to="{name:'settings-website-create'}">
        <span> Your Website</span>
    </b-link>
    <b-link class="btnStyle pop-link" :to="{name:'settings-user-management'}">
        <span> User Management</span>
    </b-link>

  </div>
</template>

<script>
    export default {
        name: "settings-top"
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
