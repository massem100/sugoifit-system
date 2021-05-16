<template>
  <div class="d-flex flex-column ">
    <b-row class="justify-content-center mx-0 flex-nowrap">
      <card class="col-lg-12">
        <b-row>
          <div class=" welcome-heading mt-4 mb-2 ml-5">
            <h3 class="font-weight-bold"> Welcome Back, <span> Jane</span></h3>

            <p contenteditable 
                class="editme" 
                v-text="txt"
                @blur="onEdit"
                @keydown.enter="endEdit"
                   >Lorem ipsum dolor sit amet consectetur adi</p>
          </div>

          <div class="d-flex font-weight-bold  ml-lg-auto m-2 mr-4">
            <div class="m-3 text-center">
              <p>7:00 PM</p>
              <p class="font-weight-bold">EST</p>
            </div>
            <div class="m-3 text-center">
              <p>12:00 AM</p>
              <p class="font-weight-bold">LONDON</p>
            </div>

          </div>
        </b-row>


        <b-row class="quick_actions_div mb-3 text-center">
          <nuxt-link class="quick_actions " :to="{name:'manage-transaction'}">
            <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon>
            <span>Add Transaction</span>
          </nuxt-link>

          <nuxt-link class="quick_actions" :to="{name:'add-invoice'}">
            <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon>
            <span> Place Order</span>
          </nuxt-link>

          <nuxt-link class="quick_actions " :to="{name:'add-invoice'}">
            <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon>
            <span> Create Invoice</span>
          </nuxt-link>

          <div class="quick_actions ">
            <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon>
            <span> Create Invoice</span>
          </div>

        </b-row>

      </card>
    </b-row>

    <b-row class="mx-0">
      <b-col class="col-lg-6 ml-4 ">
        <card type="white" header-classes="bg-transparent" class="h-100">
          <div slot="header" class="row align-items-center">
            <b-col>
              <h6 class="text-light text-uppercase ls-1 mb-1">Overview</h6>
              <h5 class="h3 mb-0">Cash Flow</h5>
            </b-col>
            <b-col>
              <ul class="nav nav-pills justify-content-end">
                <li class="nav-item mr-2 mr-md-0">
                  <a class="nav-link py-2 px-3" href="#">
                    <!-- :class="{ active: bigLineChart.activeIndex === 0 }" -->
                    <span class="d-none d-md-block">Month</span>
                    <span class="d-md-none">M</span>
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link py-2 px-3" href="#"
                  >
                    <!-- :class="{ active: bigLineChart.activeIndex === 1 }"
                    @click.prevent="initBigChart(1)" -->
                    <span class="d-none d-md-block">Week</span>
                    <span class="d-md-none">W</span>
                  </a>
                </li>
              </ul>
            </b-col>
          </div>
          <line-chart :data="chartData" :options="chartOption" :height="250"></line-chart>
        </card>
      </b-col>
      <b-col class="col-lg-5 p-2 ">
        <card type="white" header-classes="bg-transparent" class="h-100">
          <div slot="header" class="row align-items-center">
            <div class="col">
              <h6 class="text-light text-uppercase ls-1 mb-1">Overview</h6>
              <h5 class="h3 mb-0">Profits</h5>
            </div>
            <div class="col">
              <ul class="nav nav-pills justify-content-end">
                <li class="nav-item mr-2 mr-md-0">
                  <a class="nav-link py-2 px-3" href="#">
                    <!-- :class="{ active: bigLineChart.activeIndex === 0 }" -->
                    <span class="d-none d-md-block">Month</span>
                    <span class="d-md-none">M</span>
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link py-2 px-3" href="#"
                  >
                    <!-- :class="{ active: bigLineChart.activeIndex === 1 }"
                    @click.prevent="initBigChart(1)" -->
                    <span class="d-none d-md-block">Week</span>
                    <span class="d-md-none">W</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
                    <bar-chart
                      :data="barChartData" :options="barChartOption" :height="250"
                    >
                    </bar-chart>
        </card>
      </b-col>
    </b-row>
    <b-row class="d-flex flex-row m-4">
      <b-col>
        <h4> Fillable Orders</h4>
        <b-table class="m-2 bg-white" striped hover :items="items"></b-table>
      </b-col>
      <card class="w-25 mt-4 m-2">
        <h5>Inventory Items <span> Restock</span></h5>
        <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero accusamus se </p>
      </card>

    </b-row>

    <div id ="check" class="d-flex flex-row m-4">
      <b-col>
        <h4> Popular Products</h4>
        <div class="w-75 bg-white" v-for="item in items" :key="item.age">
          <img src="" alt="">
          <h5>{{item.age}}</h5>
          <!-- <h5>{{item.first_name}}</h5> -->
        </div>
      </b-col>
      <card class="w-25 m-2">
        <h5>Inventory Items <span> Restock</span></h5>
        <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero accusamus se </p>
      </card>


    </div>
  </div>

</template>

<script>
    import Card from '../components/argon-core/Cards/Card.vue';

    // Charts
    import * as chartConfigs from "@/components/argon-core/Charts/config";
    import LineChart from "@/components/charts/LineChart";
    import BarChart from "@/components/charts/BarChart";


    export default {
        components: {
            Card,
            LineChart,
            BarChart
        },
        layout: 'DashboardLayout',
        name: 'dashboard',
        data() {
            return {
                txt: localStorage.getItem('text_change'), 
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
                barChartData: {
                    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                    datasets: [{
                        data: [10000, 15000, 20000, 30000, 40000, 50000, 60000, 70000, 34000, 45000, 11000, 78000, 45000],
                        fillColor: "rgba(14,72,100,1)",
                        backgroundColor: "#33AEEF",
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
                barChartOption: {
                    responsive: true,
                    legend: {
                        display: false
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

                            }
                        ]
                    }
                },
                items: [
                    {age: 40, first_name: 'Dickerson', last_name: 'Macdonald'},
                    {age: 21, first_name: 'Larsen', last_name: 'Shaw'},
                    {age: 89, first_name: 'Geneva', last_name: 'Wilson'},
                    {age: 38, first_name: 'Jami', last_name: 'Carney'}
                ]
            }
        },

        head: {
            
                title: "SugoiFit Dashboard",
                meta: [
                    {
                        hid: "description",
                        name: "dashboard",
                        content: "SugoiFit Business Management System Dashboard"
                    }
                ],

        },
        watch:{
            txt(){
              this.txt = localStorage.getItem('text_change');
              
            }
        },
        methods: { 
          onEdit(evt){
             var src = evt.target.innerText
             this.txt = src
         },
         endEdit(){
            this.$el.querySelector('.editme').blur()
            let te = this.$el.querySelector('.editme').innerText;
            let elemt = this.$el.querySelector('#check').children;
            console.log(te);
            console.log(elemt);
            localStorage.setItem('text_change', te );
         },
        }
    }
</script>

<style lang="scss">


  a {
    color: #065863;
  }

  a:visited {
    color: #065863 !important;
  }

</style>
