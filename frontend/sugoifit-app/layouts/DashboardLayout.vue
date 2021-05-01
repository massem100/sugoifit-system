<template>
  <div class="wrapper">
    <notifications></notifications>
    <side-bar>
      <template slot="links">
           
          <div  class="d-flex flex-row"> 
            <div  class="profile mt-3 mb-2 ">
                <h6 id="profile_name" class="my-1 font-weight-bold"> Jane S.</h6>
                <h6 id="profile_ID" class="my-1"> ID 1234567</h6>
                <h6 id="role" class="my-1"> Role: Business Owner</h6>
              </div>
              <!-- <img id="profile-icon" class ="mr-2 w-25 h-25" :src="user" alt="" aspect-ratio="0.8" /> -->
            </div>
        <sidebar-item
          :link="{
            name: 'Dashboard',
            icon: 'ni ni-shop text-primary',
            path: '/',
          }"
        >
        </sidebar-item>
        <sidebar-item
          
          :link="{
            name: 'Products',
            icon: 'ni ni-bag-17 text-primary',
            path: '',
          }"
        >
        <sidebar-item
            opened
            :link="{
              name: 'Manage Products',
              icon: 'ni ni-bag-17 text-primary',
              path: '/manageproducts',
            }"
          >
          </sidebar-item>
          <sidebar-item
            opened
            :link="{
              name: 'All Products',
              icon: 'ni ni-bag-17 text-primary',
              path: '/manageproducts/list',
            }"
          >
          </sidebar-item>
          <sidebar-item
            opened
            :link="{
              name: 'Add Products',
              icon: 'ni ni-bag-17 text-primary',
              path: '/manageproducts/add',
            }"
          >
          </sidebar-item>
          <sidebar-item
            opened
            :link="{
              name: 'Product Analytics',
              icon: 'ni ni-bag-17 text-primary',
              path: '/manageproducts/analytics',
            }"
          >
          </sidebar-item>
        </sidebar-item>
        <sidebar-item
          
          :link="{
            name: 'Manage Sales',
            icon: 'ni ni-bag-17 text-primary',
            path: '/managesales',
          }"
        >
          <sidebar-item
            opened
            :link="{
              name: 'Orders',
              icon: 'ni ni-bag-17 text-primary',
              path: '/allproducts',
            }"
          >
          </sidebar-item>
        </sidebar-item>
        <sidebar-item
            :link="{
              name: 'Financials',
              icon: 'ni ni-bag-17 text-primary',
              path: '/financialstmts/income-stmt',
            }"
          >
          </sidebar-item>
        <sidebar-item
            :link="{
              name: 'Reports',
              icon: 'ni ni-bag-17 text-primary',
              path: '/reports/',
            }"
          >
          <sidebar-item
            :link="{
              name: 'Report Generation',
              icon: 'ni ni-bag-17 text-primary',
              path: '/reports/charts',
            }"
          >
          </sidebar-item>
          </sidebar-item>

        <hr
          class="my-3"
          style="
            border: 0;
            border-top: 1px solid rgba(0, 0, 0, 0.1);
            min-width: 80%;
            overflow: visible;
            box-sizing: content-box;
            height: 0;
          "
        />
      </template>
    </side-bar>
    <div class="main-content">
      <dashboard-navbar
        :type="$route.name === 'alternative' ? 'light' : 'default'"
      ></dashboard-navbar>

      <div class = "" @click="$sidebar.displaySidebar(true)"
      >
        <nuxt class = "flex-grow-1"></nuxt>
      </div>
      <content-footer class = "flex-shrink-0" v-if="!$route.meta.hideFooter"></content-footer>
    </div>
  </div>
</template>
<script>
/* eslint-disable no-new */
import PerfectScrollbar from "perfect-scrollbar";
import "perfect-scrollbar/css/perfect-scrollbar.css";

function hasElement(className) {
  return document.getElementsByClassName(className).length > 0;
}

function initScrollbar(className) {
  if (hasElement(className)) {
    new PerfectScrollbar(`.${className}`);
  } else {
    // try to init it later in case this component is loaded async
    setTimeout(() => {
      initScrollbar(className);
    }, 100);
  }
}

import DashboardNavbar from "~/components/layouts/argon/DashboardNavbar.vue";
import ContentFooter from "~/components/layouts/argon/ContentFooter.vue";
import DashboardContent from "~/components/layouts/argon/Content.vue";
import Vuex from "vuex";

export default {
  components: {
    DashboardNavbar,
    ContentFooter,
    DashboardContent,
  },
  data(){
    return{
      
    }
  },
  methods: {
    initScrollbar() {
      let isWindows = navigator.platform.startsWith("Win");
      if (isWindows) {
        initScrollbar("scrollbar-inner");
      }
    },
  },
  
};
</script>
<style lang="scss">
.wrapper {
    min-height: 100%;
    display: flex;
    flex-direction: column;
    
}
</style>
