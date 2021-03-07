<template>
  <div class="d-flex flex-row ">
    <!-- Side Bar Component -->
    <side-bar>Check</side-bar>


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


    <!-- <div id="chartDiv" class ="" ></div> -->

  </div>

</template>

<script>
    import SideBar from '/components/SideBar.vue'

    export default {
        components: {SideBar},
        name: 'Dashboard',
        head() {
            return {
                title: "Dashboard",
                meta: [
                    {
                        hid: "description",
                        name: "description",
                        content: "SugoiFit Business Management System Dashboard"
                    }
                ]
            };
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
