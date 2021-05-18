<template>
  <client-only>
    <div class="mx-3">
      <!-- Side Bar Component -->

      <div class="dashboard-main">
        <!-- Overview -->
        <b-row class="justify-content-between mx-0 flex-nowrap">
          <back-button class="mt-4 ml-2"></back-button>
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
              <h5 class="card-title">Popular Products
                <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="These are the items that have generated the most revenue this week"/>
              </h5>
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
              <h5 class="card-title">Inventory Items- Need Restock
                <font-awesome-icon icon="info-circle" 
                  v-b-tooltip.hover title="These are the items in your inventory that has fallen below the minimum quantity value. 
                  Restock immediately."/>
              </h5>
              <b-card>
                <!--<h6 class="card-title">These items have fallen below threshhold</h6>-->
                <b-table striped hover :items="tableItems"></b-table>
              </b-card>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-card>
                <b-card-title>Break-even
                  <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                        "Breakeven refers to the point at which cost and income are equal.
                         There is neither a profit nor a loss"/>
                </b-card-title>
                <b-card-text>
                  <line-chart :data="chartData" :options="chartOption" :height="250"/>
                </b-card-text>
              </b-card>
              
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
    import LineChart from "../../components/charts/LineChart";
    import BackButton from '../../components/argon-core/BackButton.vue';
    export default {
        name: "Reports",
        layout: 'DashboardLayout',
        components: {LineChart, BackButton},
        mixins: [commonChartDetails],
        head(){
          return{
              title: 'Product Analytics'
          }
        },
        data() {
            return {
                tableItems: tableItems,
                chartData: {
                    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                    datasets: [
                        {
                            label: 'Income',
                            data: [10000, 15000, 20000, 30000, 40000, 50000, 60000, 70000, 34000, 45000, 11000, 78000, 45000],
                            borderColor: 'green',
                            fill: false,
                        },
                        {
                            label: 'Last year Income',
                            data: [30000, 24000, 57000, 23000, 68000, 72000, 20005, 64000, 13300, 143000, 16500, 33000, 56000],
                            borderColor: '#B3C4D4',
                            fill: false
                        }
                    ]
                },
                chartOption: {
                    responsive: true,
                    legend: {
                        display: true
                    },
                    title: {
                        display: true,
                        fontSize: 24,
                        fontColor: '#6b7280'
                    },
                    tooltips: {
                        backgroundColor: '#17BF62'
                    },
                    scales: {
                        xAxes: [
                            {
                                gridLines: {
                                    display: false
                                }
                            }
                        ],
                        yAxes: [
                            {
                                ticks: {
                                    beginAtZero: true,
                                    callback: function (value, index, values) {
                                        return '$' + value;
                                    }
                                },
                                gridLines: {
                                    display: true
                                }
                            }
                        ]
                    }
                },
               
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
