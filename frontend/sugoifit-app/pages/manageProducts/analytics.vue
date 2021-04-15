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
              <h5 class="card-title">Popular Products</h5>
              <b-card>

                <h6 class="card-title">Items of the week</h6>
                <b-row>

                  <b-col v-for="(singleItem, ind1) in 4" :key="ind1">
                    <b-card
                      img-src="https://picsum.photos/600/300/?image=25"
                      img-alt="Image"
                      img-top
                      tag="article"
                      style="max-width: 20rem;"
                      class="mb-2"
                    >
                      <b-card-text>
                        <h5>Product {{ind1 + 1}}</h5>
                        <p>Number Sold</p>
                      </b-card-text>
                    </b-card>
                  </b-col>
                </b-row>
              </b-card>
            </b-col>
            <b-col>
              <h5 class="card-title">Inventory Items- Need Restock</h5>
              <b-card>
                <h6 class="card-title">These items have fallen below threshhold</h6>
                <b-table striped hover :items="tableItems"></b-table>
              </b-card>
            </b-col>
          </b-row>
          <b-row>
            <b-col>

              <line-chart :data="barChartData" :options="barChartOptions"/>
            </b-col>
            <b-col></b-col>
          </b-row>
        </b-container>
      </div>


    </div>

  </client-only>

</template>

<script>
    import commonChartDetails from "@/mixins/commonChartDetails";
    import {tableItems} from "../../assets/data/tableData";


    export default {
        name: "Reports",
        layout: 'dashboard',
        mixins: [commonChartDetails],
        data() {
            return {
                tableItems: tableItems
            }
        },
        head() {
            return {
                title: 'Reports',
            }
        },
        mounted() {
            this.selectedTitle = this.titleOptions[0]
            this.selectedYear = this.yearOptions[0]
            this.barChartOptions.title.text = 'Break-Even'
        },
    }
</script>

<style scoped>

</style>
