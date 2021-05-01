<template>
  <div class="d-flex flex-column ">
    <b-row class="justify-content-center mx-0 flex-nowrap">
    <card class="col-lg-12">
        <b-row>
        <div class=" welcome-heading mt-4 mb-2 ml-5">
            <h3 class="font-weight-bold"> Welcome Back, <span> Jane</span></h3>
    
            <p class="">Lorem ipsum dolor sit amet consectetur adi</p>
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
      <nuxt-link class="quick_actions " :to="{name:'add-transaction'}">
        <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon><span>Add Transaction</span>
      </nuxt-link>

      <nuxt-link class="quick_actions" :to="{name:'add-invoice'}">
        <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon><span> Place Order</span>
      </nuxt-link>

      <nuxt-link class="quick_actions " :to="{name:'add-invoice'}">
        <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon><span> Create Invoice</span>
      </nuxt-link>

      <div class="quick_actions ">
        <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon><span> Create Invoice</span>
      </div>

    </b-row>

    </card>
    </b-row>
   
      <b-row>
        <b-col class="col-lg-6 ml-4 ">
            <card type="white" header-classes="bg-transparent">
                <div slot="header" class="row align-items-center">
                <b-col>
                    <h6 class="text-light text-uppercase ls-1 mb-1">Overview</h6>
                    <h5 class="h3 mb-0">Cash Flow</h5>
                </b-col>
                <b-col >
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
                <line-chart
                :height="200"
                ref="bigChart"
                
                >
                <!-- :chart-data="bigLineChart.chartData"
                :extra-options="bigLineChart.extraOptions" -->
                </line-chart>
            </card>
            </b-col>
        <b-col class="col-lg-5 p-2 ">
            <card type="white" header-classes="bg-transparent">
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
                :height="200"
                    ref="bigChart"
                >
                </bar-chart>
            
                <!-- :chart-data="bigLineChart.chartData"
                :extra-options="bigLineChart.extraOptions" -->
    
            </card>
            </b-col>
      </b-row>
    <b-row class = "d-flex flex-row m-4"> 
          <b-col>
            <h4> Fillable Orders</h4>
            <b-table class= "m-2 bg-white" striped hover :items="items"></b-table>
          </b-col>
          <card class="w-25 mt-4 m-2"> 
            <h5>Inventory Items <span> Restock</span></h5>
            <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero accusamus se </p>
          </card>

    </b-row>
    
    <div class = "d-flex flex-row m-4"> 
          <b-col>
            <h4>  Popular Products</h4>
            <div class = "w-75 bg-white" v-for =  "item in items" :key = "item.age"> 
              <img src="" alt="">
              <h5>{{item.age}}</h5>
              <!-- <h5>{{item.first_name}}</h5> -->
            </div>
          </b-col>
          <card class = "w-25 m-2"> 
            <h5>Inventory Items <span> Restock</span></h5>
            <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero accusamus se </p>
          </card>
  

    </div>
  </div>

</template>

<script>
import Card from '../components/argon-core/Cards/Card.vue';
import ImageSlider from '../components/ImageSlider.vue';

// Charts
import * as chartConfigs from "@/components/argon-core/Charts/config";
import LineChart from "@/components/argon-core/Charts/LineChart";
import BarChart from "@/components/argon-core/Charts/BarChart";


export default {
  components: { 
        Card,
        ImageSlider, 
        LineChart, 
        BarChart 
   },
        layout: 'DashboardLayout',
        name:'dashboard',
        data(){
          return {
            items: [
                      { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
                      { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
                      { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
                      { age: 38, first_name: 'Jami', last_name: 'Carney' }
                    ]
            }
        }, 

        head() {
            return {
                title: "Dashboard",
                meta: [
                    {
                        hid: "description",
                        name: "dashboard",
                        content: "SugoiFit Business Management System Dashboard"
                    }
                ], 
                
            };
        },
    }
</script>

<style lang="scss">


a{
  color: #065863;
}
a:visited{
  color: #065863  !important;
}

</style>
