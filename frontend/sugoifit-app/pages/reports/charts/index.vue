<template>
  <client-only>
    <b-container fluid="" class="py-4">
      <b-row>
        <!-- <back-button class="mt-4 ml-2"></back-button> -->
        <b-col sm="3" cols="12">
          <b-card no-body>
            <b-card-text class="d-flex justify-content-between align-items-center p-3">
              <div>
                <h3 class="mb-0">
                  <font-awesome-icon :icon="['fas','dollar-sign']"></font-awesome-icon>
                  {{kFormatter(report.expense)}}
                </h3>
                <small>Total Expense</small>
              </div>
              <div>
                <b-avatar>
                  <font-awesome-icon :icon="['fas','dollar-sign']" class="text-info"></font-awesome-icon>
                </b-avatar>

              </div>
            </b-card-text>
          </b-card>
        </b-col>
        <b-col sm="3" cols="12">
          <b-card no-body>
            <b-card-text class="d-flex justify-content-between align-items-center p-3">
              <div>
                <h3 class="mb-0">
                  <font-awesome-icon :icon="['fas','dollar-sign']"></font-awesome-icon>
                  {{kFormatter(report.income)}}
                </h3>
                <small>Total Income</small>
              </div>
              <div>
                <b-avatar>
                  <font-awesome-icon :icon="['fas','money-bill']" class="text-info"></font-awesome-icon>
                </b-avatar>

              </div>
            </b-card-text>
          </b-card>
        </b-col>
        <b-col sm="3" cols="12">
          <b-card no-body>
            <b-card-text class="d-flex justify-content-between align-items-center p-3">
              <div>
                <h3 class="mb-0">
                  <font-awesome-icon :icon="['fas','dollar-sign']"></font-awesome-icon>
                  {{kFormatter(report.profit)}}
                </h3>
                <small>Total Profit</small>
              </div>
              <div>
                <b-avatar>
                  <font-awesome-icon :icon="['fas','hand-holding-usd']" class="text-info"></font-awesome-icon>
                </b-avatar>

              </div>
            </b-card-text>
          </b-card>
        </b-col>
        <b-col sm="3" cols="12">
          <b-card no-body>
            <b-card-text class="d-flex justify-content-between align-items-center p-3">
              <div>
                <h3 class="mb-0">
                  <font-awesome-icon :icon="['fas','dollar-sign']"></font-awesome-icon>
                  {{kFormatter(report.revenue)}}
                </h3>
                <small>Total Revenue</small>
              </div>
              <div>
                <b-avatar>
                  <font-awesome-icon :icon="['fas','funnel-dollar']" class="text-info"></font-awesome-icon>
                </b-avatar>

              </div>
            </b-card-text>
          </b-card>
        </b-col>
        <b-col lg="7" cols="12" class="py-3">
          <b-card class="h-100">
            <b-card-title class="d-flex justify-content-between flex-wrap align-items-center">
              <h3 class="col-lg-5 col-md-12">Revenue</h3>
              <div class="d-flex  col-lg-7 col-md-12">
                <b-form-select v-model="selectedTitle" class="mx-2" :options="titleOptions" size="sm"></b-form-select>
                <b-form-select v-model="selectedYear" class="mx-2" :options="yearOptions" size="sm"></b-form-select>
              </div>
            </b-card-title>
            <b-card-text>
              <line-chart :data="chartData" :options="chartOption" :height="250"></line-chart>
            </b-card-text>
          </b-card>
        </b-col>
        <b-col lg="5" cols="12" class="py-3">
          <b-card class="h-100">
            <b-card-title>
              <h3>Expenses</h3>
            </b-card-title>
            <b-card-text class="d-flex align-items-center justify-content-center" style="height: calc( 100% - 50px)">
              <doughnut-chart :data="pieData" :options="pieOp" :height="200"></doughnut-chart>
            </b-card-text>
          </b-card>
        </b-col>
        <b-col cols="12">
          <b-card>
            <b-card-title>Ratio Analysis</b-card-title>
            <b-card-title>Profitability Ratio</b-card-title>
            <b-card-text>
              <b-table-simple responsive>
                <b-thead>
                  <b-tr>
                    <b-th style="width: 100px">Ratio Name</b-th>
                    <b-th class="text-center">Ratio Result/Percentage</b-th>
                    <b-th style="width: 150px" class="text-right">Actions</b-th>
                  </b-tr>
                </b-thead>
                <b-tbody>
                   <!-- idx <= (maxRatio?ratios.length:4)  -->
                  <b-tr v-for="(ratio,idx) in ratios" :key="idx" >
                    <b-td class="text-capitalize">{{ratio.name}}</b-td>
                    <b-td>
                      <div class="d-flex align-items-center justify-content-center">
                        <b-progress :value="ratio.value" :max="100" class="mr-3" height="8px"
                                    style="min-width: 250px"></b-progress>
                        <span>{{ratio.ratio}}</span>
                      </div>

                    </b-td>
                    <b-td class="text-right">
                      <b-button size="sm" variant="info">See more</b-button>
                    </b-td>
                  </b-tr>
                  <b-tr>
                    <b-td colspan="3" class="text-right">
                      <b-button size="sm" variant="light" @click="maxRatio=!maxRatio">
                        {{maxRatio?'See Less':'See All'}}
                      </b-button>
                    </b-td>
                  </b-tr>
                </b-tbody>
              </b-table-simple>
            </b-card-text>
          </b-card>
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
      <!--      <b-row>-->
      <!--        <b-col v-for="(item, ind) in trendItems" :key="ind">-->
      <!--          <vue-ellipse-progress :progress="item.value">-->
      <!--            <span slot="legend-value">%</span>-->
      <!--          </vue-ellipse-progress>-->
      <!--          Progress-->
      <!--        </b-col>-->
      <!--      </b-row>-->
    </b-container>

  </client-only>

</template>

<script>

    import commonChartDetails from "@/mixins/commonChartDetails";
    import DoughnutChart from "../../../components/charts/DoughnutChart";
    import LineChart from "../../../components/charts/LineChart";
    import BackButton from '../../../components/argon-core/BackButton.vue';
    export default {
        name: "Reports",
        components: {DoughnutChart, LineChart, BackButton},
        layout: 'DashboardLayout',
        mixins: [commonChartDetails],
        head(){
          return{
              title: 'Report Charts'
          }
        },
        data() {
            return {
                report: {
                    expense: 124000,
                    profit: 134000,
                    revenue: 100000,
                    income: 5430000,
                },
                maxRatio: false,
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
                pieData: {
                    labels: [
                        'Maintenance',
                        'Labour Cost',
                        'Rent',
                        'Other',
                    ],
                    datasets: [
                        {
                            label: 'Visits',
                            data: [32, 25, 15, 3],
                            backgroundColor: ['#2f4b7c', '#7c327a', '#7c4f58', '#71707c'],
                        }
                    ]
                },
                pieOp: {
                    responsive: true,
                    legend: {
                        display: true,
                        position: 'right',
                        labels: {
                            fontSize: 16,
                        },
                    },
                    title: {
                        display: false,
                    },
                    tooltips: {
                        backgroundColor: '#17BF62'
                    },
                },
                ratios: [
                    {name: 'current ratio', value: '50', ratio: '1:0'},
                    {name: 'acid test ratio', value: '10', ratio: '7:0'},
                    {name: 'cash ratio', value: '75', ratio: '3:0'},
                    {name: 'debt ratio', value: '95', ratio: '1:0'},
                    {name: 'debt equity ratio', value: '25', ratio: '6:0'},
                    {name: 'interest coverage ratio', value: '45', ratio: '1:0'},
                    {name: 'asset turnover ratio', value: '80', ratio: '1:0'},
                    {name: 'inventory turnover ratio', value: '5', ratio: '2:0'},
                    {name: 'days inventory ratio', value: '65', ratio: '3:0'},
                ]
            }
        },
        methods: {
            kFormatter(num) {
                return Math.abs(num) > 999 ? Math.sign(num) * ((Math.abs(num) / 1000).toFixed(1)) + 'k' : Math.sign(num) * Math.abs(num)
            }
        },
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
