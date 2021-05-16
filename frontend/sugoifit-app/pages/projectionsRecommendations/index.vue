<template>
  <client-only>
    <div class="mx-3">
      <!-- Side Bar Component -->

      <div class="dashboard-main">
        <!-- Overview -->
        <b-row class="justify-content-between mx-0 flex-nowrap">
          <div class="welcome-heading">
            <h5 class="font-weight-bold"> Welcome Back, <span> Jane</span></h5>
            <p class="">Lorem ipsum dolor sit amet consectetur adi</p>
          </div>
          <div class="d-flex font-weight-bold">
            <div class="m-3 text-center">
              <p>EST</p>
              <p>7:00 PM</p>
            </div>
            <div class="m-3 text-center">
              <p>LONDON</p>
              <p>12:00 AM</p>
            </div>
          </div>
        </b-row>
        <br>
        <b-container fluid>
          projections
        </b-container>
      </div>


    </div>

  </client-only>

</template>

<script>
    export default {
        layout: 'dashboard',
        head(){
          return{
              title: 'Projections'
          }
        },
    }
</script>

<style scoped>

</style>
