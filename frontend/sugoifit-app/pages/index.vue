<template>
  <div class="mx-3">
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
    <b-row class="quick_actions_div p-2  text-center mx-0">
      <nuxt-link class="quick_actions bg-primary" :to="{name:'add-transaction'}">
        <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon><span>Add Transaction</span>
      </nuxt-link>

      <div class="quick_actions bg-primary">
        <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon><span> Place Order</span>
      </div>

      <nuxt-link class="quick_actions bg-primary" :to="{name:'add-invoice'}">
        <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon><span> Create Invoice</span>
      </nuxt-link>

      <div class="quick_actions bg-primary">
        <font-awesome-icon :icon="['fas','plus']"></font-awesome-icon><span> Create Invoice</span>
      </div>

    </b-row>
    <card></card>
  </div>

</template>

<script>
import Card from '../components/argon-core/Cards/Card.vue';
    export default {
  components: { Card },
        layout: 'DashboardLayout',
        name:'dashboard',
        head() {
            return {
                title: "Dashboard",
                meta: [
                    {
                        hid: "description",
                        name: "dashboard",
                        content: "SugoiFit Business Management System Dashboard"
                    }
                ]
            };
        },
    }
</script>

<style lang="scss">

.quick_actions{
  text-decoration: none;
  
}
a{
  color: #065863;
}
a:visited{
  color: #065863  !important;
}

</style>
