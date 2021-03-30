<template>
<div class = "m-0 w-100 h-100 bg-danger">
    <b-container class = "bg-success" fluid >
          <!-- Nav Bar Component  -->
        <nav-header class = "nav-bar w-100 "></nav-header>
        <b-row>
          <!-- Side Bar Component -->
              <side-bar class = "side-bar"></side-bar>
          <!-- Main Content -->
              <b-col class="dashboard-main m-5">
        
                    <b-row class="">
                        <b-col >
                          <h5 class=""> Welcome Back, <span> Jane</span></h5>
                          <p class="">Lorem ipsum dolor sit amet consectetur adi</p>
                        </b-col>   
                        <b-row >
                          <b-col>
                              <p>7:00 PM</p>
                              <p>EST</p>
                          </b-col>
                          
                            <b-col >
                                <p>12:00 AM</p>
                                <p>LONDON </p>
                            </b-col>
                          
                        </b-row> 
                    </b-row>

                  
              
                  <!-- Quick Actions -->
                  <b-col class=" d-flex justify-content-center">
                    <b-row class="quick_actions_div d-flex flex-row justify-content-center  bg-danger text-center">
                        <b-link class="d-flex flex-column quick_actions " :to="{name:'add-transaction'}">
                          <img src="" alt=""><i class="fas fa-plus"></i><span>Add Transaction</span>
                        </b-link>

                        <div class="d-flex flex-column quick_actions "><img src="" alt=""><i
                          class="fas fa-plus"></i><span> Place Order</span>
                        </div>

                        <b-link class="d-flex flex-column quick_actions " :to="{name:'add-invoice'}">
                          <img src="" alt=""><i class="fas fa-plus"></i><span> Create Invoice</span>
                        </b-link>
                        
                        <div class="d-flex flex-column quick_actions"><img src="" alt=""><i class="fas fa-plus"></i><span> Create Invoice</span>
                      </div>

                    </b-row>
                  </b-col>
                  <div class = "d-flex flex-row  order_notes">

                    <div class="d-flex flex-row">

                      <div class="fillable-order">
                        <h5> Orders to be filled</h5>
                        <b-table class = "order_table" :items = "orders"> </b-table>
                        
                      </div>

                      <div class="notes">

                      </div>
                      </div>
                    </div>
                
              
            </b-col>
        </b-row>
    </b-container>
</div>
</template>

<script>
    
import SideBar from '/components/SideBar.vue'
import NavHeader from '/components/nav-header.vue'

export default {
    components: { SideBar , NavHeader},
    name: 'Dashboard',
    head(){
        return{
            title:"Dashboard",
            meta: [
                {
                    hid:"description", 
                    name: "description",
                    content: "SugoiFit Business Management System Dashboard"
                }
            ]
        }; 
        
    },
    data(){
          return {
              orders: [
                {orderid: 1, 'order description': 'Slippers', cost: 20.00, 'Payment Due': 'Thursday'},
                {orderid: 1, 'order description': 'Slippers', cost: 20.00, 'Payment Due': 'Thursday'},
                {orderid: 1, 'order description': 'Slippers', cost: 20.00, 'Payment Due': 'Thursday'}
              
              ]
          }
        },
    methods: {

    }, 
    created: function () {
    let self = this;
    fetch("http://localhost:8080/api/test", {
      method: "GET",
      headers: {
        "accept": "application/json",
      },
      credentials: "cross-origin",
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (jsonResponse) {
       console.log(jsonResponse);
      })
      .catch(function (error) {
         console.log(error);
      });    
  }

};
</script>

<style scoped>
 
</style>
