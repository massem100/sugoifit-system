<template>
  <div class="d-flex flex-row ">
    <!-- Side Bar Component -->
        <side-bar>Check</side-bar>

        <div>
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
                    <!-- Quick Actions -->
                <div class="quick_actions_div d-flex flex-row text-center">
                    <div class = "d-flex flex-column quick_actions"><img src="" alt=""><i class="fas fa-plus"></i><span>Add Transaction</span></div>
                    <div class = "d-flex flex-column quick_actions"><img src="" alt=""><i class="fas fa-plus"></i><span> Place Order</span></div>
                    <div class = "d-flex flex-column quick_actions"><img src="" alt=""><i class="fas fa-plus"></i><span> Create Invoice</span></div>
                    <div class = "d-flex flex-column quick_actions"><img src="" alt=""><i class="fas fa-plus"></i><span> Create Invoice</span></div>

                </div>
            </div>

            <div class="time_box ml-auto">
              <p>7:00 PM</p>
              <p>EST</p>
              <p>12:00 AM</p>
              <p>LONDON</p>
            </div>
        </div>
          <!-- Quick Actions -->
          <div class="quick_actions_div d-flex flex-row p-2 text-center">
              <nuxt-link class="d-flex flex-column quick_actions" :to="{name:'add-transaction'}">
                <img src="" alt=""><i class="fas fa-plus"></i><span>Add Transaction</span>
              </nuxt-link>
              <div class="d-flex flex-column quick_actions"><img src="" alt=""><i
                class="fas fa-plus"></i><span> Place Order</span></div>
              <div class="d-flex flex-column quick_actions"><img src="" alt=""><i class="fas fa-plus"></i><span> Create Invoice</span>
              </div>
              <div class="d-flex flex-column quick_actions"><img src="" alt=""><i class="fas fa-plus"></i><span> Create Invoice</span>
            </div>

          </div>
        </div>


 </div>

</template>

<script>
    
import SideBar from '/components/SideBar.vue'
export default {
    components: { SideBar },
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
        // console.log(error);
      });    
  }

    };

    
</script>

<style scoped>
  #chartDiv {
    width: 50%;
    height: 30%;
    position: absolute;
    top: 300px;
    right: 80px;
  }
</style>
