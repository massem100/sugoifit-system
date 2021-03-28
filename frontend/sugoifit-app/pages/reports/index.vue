<template>
  <client-only>
    <div class="d-flex flex-row ">
      <!-- Side Bar Component -->
      <side-bar class = "side-bar">Check</side-bar>

      <div class="dashboard-main">
        <!-- Overview -->
        <div class="d-flex flex-column w-100">
          <div class="d-flex flex-row align-items-center settings_bar ml-auto ">
            <h6 class="d-flex ">Jane S.</h6>
            <img class="m-2" id="top-user-icon" src="~assets/uploads/Profile_icon.svg" alt="">
            <img class="m-2" src="~assets/uploads/settings.svg" alt="">
          </div>
          <div class="d-flex flex-row">
            <div class="welcome-heading">
              <h5 class=""> Welcome Back, <span> Jane</span></h5>
              <p class="">Lorem ipsum dolor sit amet consectetur adi</p>
            </div>

          </div>

          <div class="time_box ml-auto">
            <p>7:00 PM</p>
            <p>EST</p>
            <p>12:00 AM</p>
            <p>LONDON</p>
          </div>
        </div>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>


        <div class="container">

          <div class="row">
            <div class="col">
              <bar-chart :data="barChartData" :options="barChartOptions" :height="200"/>
            </div>
            <div class="col">
              <line-chart :data="barChartData" :options="barChartOptions" :height="200"/>
            </div>
            <div class="col">
              <pie-chart :data="barChartData" :options="barChartOptions" :height="200"/>
            </div>
            <div class="col" v-for="(item , ind1) in 3" :key="ind1">
              <trend
                :data="[0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0]"
                :gradient="['#6fa8dc', '#42b983', '#2c3e50']"
                auto-draw
                smooth
              >
              </trend>
              <p>Trends to show</p>
            </div>
          </div>
          <div class="row">
            <div class="col" v-for="(item, ind) in trendItems" :key="ind">
              <p>
                <vue-ellipse-progress :progress="item.value">
                  <span slot="legend-value">%</span>
                </vue-ellipse-progress>
                Progress
              </p>

            </div>
          </div>
        </div>
      </div>


    </div>

  </client-only>

</template>

<script>
  import SideBar from '../../components/SideBar.vue';
  import BarChart from '../../components/charts/BarChart'
  import LineChart from '../../components/charts/LineChart'
  import PieChart from '../../components/charts/PieChart'
  import {chartData, barChartOptions} from "../../assets/data/chartData";
  export default {
    name: "Reports",
    data() {
      return {
        barChartData: chartData,
        barChartOptions: barChartOptions,
        trendItems: [
          {value: 90},
          {value: 60},
          {value: 75},
          {value: 85},
          {value: 74},
          {value: 85},
        ]
      }
    },
    components: {
      BarChart,
      LineChart,
      PieChart,
      SideBar
    },
    head() {
      return {
        title: 'Reports',
      }
    }
  }
</script>

<style scoped>
.row {
  display: flex;
  flex-direction: row;
}
  .col {
    display: flex;
    flex-direction: column;
  }
#chartDiv {
  width: 50%;
  height: 30%;
  position: absolute;
  top: 300px;
  right: 80px;
}
.side-bar{
  position: fixed;
}

.dashboard-main{
  margin-left: 20rem;
}
</style>
