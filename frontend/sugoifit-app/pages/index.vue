<template>
<div class="d-flex flex-column"> 
      <nav-header class = "nav-bar"></nav-header>
  <div class="d-flex flex-row ">
    <!-- Side Bar Component -->
        <side-bar class = "side-bar"></side-bar>

        <div class="dashboard-main ">
  
              <div class="d-flex flex-row w-100 align-items-center">
                  <div class="d-flex flex-column welcome-heading ">
                    <h5 class=""> Welcome Back, <span> Jane</span></h5>
                    <p class="">Lorem ipsum dolor sit amet consectetur adi</p>
                  </div>   
                   <div class="d-flex flex-row m-2 ml-auto mr-2 ">
                     <div class="d-flex flex-column m-2 ">
                        <p>7:00 PM</p>
                        <p>EST</p>
                     </div>
                     
                      <div class="d-flex flex-column m-2 ">
                          <p>12:00 AM</p>
                          <p>LONDON</p>
                      </div>
                     
                  </div> 
              </div>

             
        
            <!-- Quick Actions -->
            <div class=" ml-3 d-flex justify-content-center">
              <div class="quick_actions_div d-flex flex-row justify-content-center  bg-danger p-2  text-center">
                  <nuxt-link class="d-flex flex-column quick_actions " :to="{name:'add-transaction'}">
                    <img src="" alt=""><i class="fas fa-plus"></i><span>Add Transaction</span>
                  </nuxt-link>

                  <div class="d-flex flex-column quick_actions "><img src="" alt=""><i
                    class="fas fa-plus"></i><span> Place Order</span>
                  </div>

                  <nuxt-link class="d-flex flex-column quick_actions " :to="{name:'add-invoice'}">
                    <img src="" alt=""><i class="fas fa-plus"></i><span> Create Invoice</span>
                  </nuxt-link>
                  
                  <div class="d-flex flex-column quick_actions"><img src="" alt=""><i class="fas fa-plus"></i><span> Create Invoice</span>
                </div>

              </div>
            </div>
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
        </div>

 </div>
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
      credentials: "same-origin",
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (jsonResponse) {
       console.log(jsonResponse);
      })
      .catch(function (error) {
        // console.log(error);
      });    
  }

};


</script>

<style scoped>
  .quick_actions_div{
    
  }
  .quick_actions{
    margin: 0px 20px 10px 0px;
    background-color: #DFFBFF;
    justify-content: center;
    width: 20rem; 
    height: 4rem;
    font: 400 1rem "Poppins";
  }
  .side-bar{
    
    display: none;
  }

 
  .nav-bar{
    margin-bottom: 2rem;
    position: fixed; 
    top:0; 
    left:0;
    width: 100%;
    height: 2rem;
    z-index: 2;
  }

  .dashboard-main{
    margin: 2rem;
  }
  /*
  
  .time_box{
    display:none;
  }

  .quick_actions_div {
  display: grid;
  grid-template-columns: 1fr 1fr ;
  justify-content: center;
}

.quick_actions {
  margin: 10px 15px 10px 0px;
  background-color: #DFFBFF;
  width: 14rem;
  height: 3rem;
  padding: 20px;
  display: flex;
  justify-content: center;
  border-radius: 5px;
  text-decoration: none;
  font: 400 1rem "Poppins";
  color: #222222;

}
.quick_actions span {
    font-size: 16px;
    align-items: center;
    justify-content: center;
  }

  .fillable-order{
    margin: 1rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .order_table{
    margin: 2rem;
    width: 10rem; 
    height: 10rem;
    font: 400 0.8rem "Poppins";
  }

  
  .welcome-heading {
    text-align: start;

    margin: 5rem 1rem 1rem 1.2rem;
  
  }

 .welcome-heading p{
    font-weight: 200;
    font-family: 'Poppins';
  }
  @media only screen and (max-width: 600px) {
    
  }

  @media only screen and (min-width: 600px) {
    
  }
  @media only screen and (min-width: 768px) {
   
  }
  */

  @media only screen and (min-width: 992px) {
     .side-bar{
      display:block;
      /* position: fixed; */
      /* top: 3.6rem; */
    }

    .dashboard-main{
    /* margin-left: 22rem; */
    z-index: 1;
  }
/*
  .order_notes{
    margin: 2rem;
    width: 95%;
    justify-content: flex-start;
  }
  .order_table{
    width: 32rem;
  }
  
.quick_actions_div {
  display: flex;
  justify-content:flex-start;
  margin-top: 140px;
  margin-left: 2rem;
  width: 20rem;
  height: 6rem;
  background-color: burlywood;
}

.quick_actions {
  margin: 10px 15px 10px 0px;
  background-color: #DFFBFF;
  width: 14rem;
  height: 5rem;
  padding: 20px;
  display: flex;
  justify-content: center;
  border-radius: 5px;
  text-decoration: none;
  color: #222222;

}
.quick_actions span {
    font-size: 16px;
    align-items: center;
    justify-content: center;
  }
  .fillable-order{
    font: 400 0.8rem "Poppins";
    margin: 1rem;
    width: 30rem;
    height: 25rem;
    background: blueviolet;
  }
  .notes{
    margin-top: 1rem;
    width:25rem;
    height: 25rem;
    background-color: #FFFCE2;
  } */
  }
  @media only screen and (min-width: 1200px) {
    
  } 
</style>
