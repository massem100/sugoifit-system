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
          <b-row>

            <b-col>
              <b-row class="justify-content-around">
                <b-form-select v-model="selectedTitle" class="col-lg-3" :options="titleOptions"></b-form-select>
                <b-form-select v-model="selectedYear" class="col-lg-3" :options="yearOptions"></b-form-select>
              </b-row>
              <line-chart :data="lineChartData" :options="lineChartOptions" :height="200"/>
            </b-col>
            <b-col>
              <pie-chart :data="pieChartData" :options="pieChartOptions" :height="200"/>
            </b-col>
          </b-row>
          <!--          <b-row>-->
          <!--            <b-col v-for="(item , ind1) in 3" :key="ind1">-->
          <!--              <trend-->
          <!--                :data="[0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0]"-->
          <!--                :gradient="['#6fa8dc', '#42b983', '#2c3e50']"-->
          <!--                auto-draw-->
          <!--                smooth-->
          <!--              >-->
          <!--              </trend>-->
          <!--              <p>Trends to show</p>-->
          <!--            </b-col>-->
          <!--          </b-row>-->
          <b-row>
            <b-col v-for="(item, ind) in trendItems" :key="ind">
              <vue-ellipse-progress :progress="item.value">
                <span slot="legend-value">%</span>
              </vue-ellipse-progress>
              Progress
            </b-col>
          </b-row>
        </b-container>
      </div>


    </div>

  </client-only>

</template>

<script>

    import commonChartDetails from "@/mixins/commonChartDetails";

    export default {
        name: "Reports",
        layout: 'dashboard',
        mixins: [commonChartDetails],
        mounted() {
            this.selectedTitle = this.titleOptions[0]
            this.selectedYear = this.yearOptions[0]
        },
        head() {
            return {
                title: 'Reports',
            }
        }
    }
</script>

<style scoped>

</style>
