<template>

    <b-container class = "m-0 bg-success p-0 main-page">
          <!-- Nav Bar Component  -->
        <nav-header class = "nav-bar w-100"></nav-header>

        <b-container class=" bg-secondary w-100">
          <!-- Side Bar Component -->
              <side-bar class = "side-bar"></side-bar>
          <!-- Main Content -->
              <b-col align-h = "start" cols ="10" lg ="12" class="dashboard-main bg-danger ">
                    <!-- Full card welcome + Time -->
                      
                      <b-row class="">
                         
                        <!-- Welcome Back Section -->
                          
                          <b-col >
                              <b-card-text class=""> Welcome Back, <span> Jane</span></b-card-text>
                              <b-card-text class="">Lorem ipsum dolor sit amet consectetur adi</b-card-text>
                          </b-col>  
                          <!-- Time Section -->
                          <b-row class="mr-4 bg-light">
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
                    <b-row class="quick_actions_div justify-content-center m-3 text-center">
                        <b-link class="d-flex flex-column quick_actions " :to="{name:'add-transaction'}">
                         <font-awesome-icon :icon="['fas', 'fa-plus']"></font-awesome-icon><span>Add Transaction</span>
                        </b-link>

                        <b-link class="d-flex flex-column quick_actions "><i class="fas fa-plus"></i><span> Place Order</span></b-link>

                        <b-link class="d-flex flex-column quick_actions " :to="{name:'add-invoice'}">
                          <i class="fas fa-plus"></i><span> Create Invoice</span>
                        </b-link>
                        
                        <b-link class="d-flex flex-column quick_actions"><i class="fas fa-plus"></i><span> Create Invoice</span></b-link>
                     </b-row>
                  </b-col>

                  

                  <b-col class="fillable-order">
                      <h5> Orders to be filled</h5>
                      <b-table class = "order_table" :items = "orders"> </b-table>
                      
                  </b-col> 

            </b-col>
        </b-container>
    </b-container>

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
  /* .main-page{
    margin:0;
    width: 100%;
    height: 100vh;
  }

  .nav-bar{
    margin: 0;
    min-width: 100vw;
  }
 .dashboard-main{
   /* margin: 0;
   width: 100%;
   min-height: 100vh; */
   /* background-color: blueviolet; */
   /* box-sizing:initial; */
 /* }  */
</style>
