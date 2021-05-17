<template>
  <div class="wrapper">
    <notifications></notifications>
    <side-bar class="bg-white text-black">
      <template slot="links">
           
          <div  class="d-flex  flex-row justify-content-start"> 
            <div  class="profile  ml-3 mt-3 mb-3 ">
                <h5 id="profile_name" class="my-1 font-weight-bold" :v-text="full_name">Jane S.</h5>
                <h5 id="profile_ID" class="my-1"> ID: {{userid}}</h5>
                <h5 id="role" class="my-1"> Role: {{role}}</h5>
              </div>
              <img id="profile-icon" class ="mt-3 ml-2 mr-2 w-25 h-25" :src="user" alt="" aspect-ratio="1" />
             
            </div>
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
        <sidebar-item
          :link="{
            name: 'Dashboard',
            icon: ['fas', 'plus'],
            path: '/',
            color: 'text-black',
          }"
        >
        </sidebar-item>
        <sidebar-item
          :link="{
            name: 'Manage Transactions',
            icon: ['fas', 'receipt'],
            path: '/manage-transaction',
            color: 'text-black',
          }"
        >
        </sidebar-item>
        <sidebar-item
          
          :link="{
            name: 'Products',
            icon: ['fas', 'plus'],
            path: '',
            color: 'text-black',
          }"
        >
        
          <sidebar-item
            opened
            :link="{
              name: 'All Products',
              icon: ['fas', 'plus'],
              path: '/manageproducts/list',
              color: 'text-black',
            }"
          >
          </sidebar-item>
          <sidebar-item
            opened
            :link="{
              name: 'Add Products',
              icon: ['fas', 'plus'],
              path: '/manageproducts/add',
              color: 'text-black',
            }"
          >
          </sidebar-item>
          <sidebar-item
            opened
            :link="{
              name: 'Product Analytics',
              icon: ['fas', 'plus'],
              path: '/manageproducts/analytics',
              color: 'text-black',
            }"
          >
          </sidebar-item>
        </sidebar-item>
       
         <sidebar-item
            :link="{
              name: 'Invoices',
              icon: ['fas', 'plus'],
              path: '/invoice/',
              color: 'text-black',
            }"
          >
            <sidebar-item
              :link="{
                name: 'Create Invoice',
                icon: ['fas', 'plus'],
                path: '/invoice/create',
                color: 'text-black',
              }"
            >
            </sidebar-item>
            <sidebar-item
              :link="{
                name: 'All Invoices',
                icon: ['fas', 'plus'],
                path: '/invoice/list',
                color: 'text-black',
              }"
            >
            </sidebar-item>
          </sidebar-item>
        <sidebar-item
            :link="{
              name: 'Financials',
              icon: ['fas', 'plus'],
              path: '/financialstmts/',
              color: 'text-black',
            }"
          >
          <sidebar-item
            :link="{
              name: 'Balance Sheet',
              icon: ['fas', 'plus'],
              path: '/financialstmts/balance-sheet/_slug',
              color: 'text-black',
            }"
          >
          </sidebar-item>
          <sidebar-item
            :link="{
              name: 'Income Statement',
              icon: ['fas', 'plus'],
              path: '/financialstmts/profit-loss/_slug',
              color: 'text-black',
            }"
          >
          </sidebar-item>
          </sidebar-item>
        <sidebar-item
            :link="{
              name: 'Reports',
              icon: ['fas', 'chart-bar'],
              path: '/reports/',
              color: 'text-black',
            }"
          >
          <sidebar-item
            :link="{
              name: 'Report Generation',
              icon: ['fas', 'plus'],
              path: '/reports/charts',
              color: 'text-black',
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
         <sidebar-item
            :link="{
              name: 'Start Onboarding Process',
              icon: ['fas', 'plus'],
              path: '/onboarding-main/',
              color: 'text-black',
            }"
          >
          </sidebar-item>
      </template>
    </side-bar>
    
    <div class="main-content">
      <dashboard-navbar
        :type="$route.name === 'alternative' ? 'light' : 'default'"
      ></dashboard-navbar>

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
      f_name:'', 
      l_name: ''

      
    }
  },
  created(){

  },
  computed: {
        alert () {
            return this.$store.state.alert
        }, 
        full_name(){
          return this.f_name + " " + this.l_name
        }, 
        role(){
          return localStorage.getItem('user_role');
        }, 
        userid(){
          return localStorage.getItem('userid');
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
