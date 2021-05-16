<template>
  <div class="wrapper">
    <notifications></notifications>
    <b-col>
      
      <b-row>
       <div class="side-nav-on"> 
        <!-- The inner divs will be triggered by a v-if to toggle active class/display -->
        <div class="w-100">
            <!-- I want to make the sidebar dynamic so when its time to change
             the company type instead of the list its illustration or words -->
            <div class="sugoifit-name">
                <img class = "logo" src="~assets/uploads/logo.png" alt="">
                <h5 class = ""> SugoiFIt App</h5>
            </div>

            <ul class = "list-nav d-flex flex-column"> 
                    <!-- <img class = "checked" src="~assets/uploads/checked.svg" alt=""> -->
                <li><span>1</span>Email Details</li>
                <li><span>2</span>Company Type </li>
                <!-- <li class = ""><span>3</span>Business Details </li> -->
                <div class = "d-flex flex-row"> 

               
               <li><span>3</span></li>
                <b-nav-item-dropdown  text="Business Details" right>
                    
                    <b-dropdown-item class = "list-style-none" href="#">Corporation</b-dropdown-item>
                    <b-dropdown-item href="#">About your business</b-dropdown-item>
                   
                </b-nav-item-dropdown>
                 </div>
                <li><span>4</span> Team </li>
                <li><span>5</span> Personal Details</li>
            </ul>

            <div class = "onboard-footer">

            </div>
              
        </div>
        
    </div>
    
    <div class="main-content">
      <!-- <dashboard-navbar
        :type="$route.name === 'alternative' ? 'light' : 'default'"
      ></dashboard-navbar> -->

      <div>
      <base-alert v-if="alert.message"
                    :class="`alert ${alert.type}`"
                    style="
                           height: 3.5rem; 
                           width:100%;
                           z-index:1;" 
                    dismissible
                     ><strong>Success:</strong> {{alert.message}}
      </base-alert>
        <nuxt></nuxt>
      </div>
      <content-footer class = "" v-if="!$route.meta.hideFooter"></content-footer>
    </div>
      </b-row>
    </b-col>
    
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
import BaseAlert from '../components/argon-core/BaseAlert.vue';

export default {
  components: {
    DashboardNavbar,
    ContentFooter,
    DashboardContent,
    BaseAlert,
  },
  data(){
    return{
      user: require('/assets/uploads/user-icon.svg'),
      
    }
  },
  computed: {
        alert () {
            return this.$store.state.alert
        }
    },
  watch: {
        $route (to, from){
            // clear alert on location change
            this.$store.dispatch('alert/clear');
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
