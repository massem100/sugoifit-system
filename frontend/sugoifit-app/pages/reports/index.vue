<template>
  <client-only>
    <div class="d-flex flex-row ">
      
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
          report home page
        </b-container>
      </div>


    </div>

  </client-only>

</template>

<script>
  
    import {
        barChartData,
        barChartOptions,
        lineChartData,
        lineChartOptions,
        pieChartData, pieChartOptions
    } from "../../assets/data/chartData";

    export default {
        name: "Reports",
        layout: 'dashboard',
        data() {
            return {}
        },
        components: {

        },
        head() {
            return {
                title: 'Reports',
            }
        }
    }
</script>

<style scoped>
  /*.row {*/
  /*  display: flex;*/
  /*  flex-direction: row;*/
  /*}*/
  /*  .col {*/
  /*    display: flex;*/
  /*    flex-direction: column;*/
  /*  }*/
  #chartDiv {
    width: 50%;
    height: 30%;
    position: absolute;
    top: 300px;
    right: 80px;
  }

  .side-bar {
    position: fixed;
  }

  .dashboard-main {
    margin-left: 20rem;
  }
</style>
