<template>
  <div class="wrapper">
    <notifications></notifications>
    <side-bar>
      <template slot="links">

        <div class="d-flex flex-row justify-content-center">
          <div class="profile mt-3 mb-3 ">
            <h5 id="profile_name" class="my-1 font-weight-bold"> Jane S.</h5>
            <h5 id="profile_ID" class="my-1"> ID 1234567</h5>
            <h5 id="role" class="my-1"> Role: Business Owner</h5>
          </div>
          <img id="profile-icon" class="mt-3 ml-2 mr-2 w-25 h-25" :src="user" alt="" aspect-ratio="1"/>

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
          }"
        >
        </sidebar-item>
        <sidebar-item
          :link="{
            name: 'Manage Transactions',
            icon: ['fas', 'receipt'],
            path: '/manage-transaction',
          }"
        >
        </sidebar-item>
        <sidebar-item

          :link="{
            name: 'Products',
            icon: ['fas', 'plus'],
            path: '',
          }"
        >

          <sidebar-item
            opened
            :link="{
              name: 'All Products',
              icon: ['fas', 'plus'],
              path: '/manageproducts/list',
            }"
          >
          </sidebar-item>
          <sidebar-item
            opened
            :link="{
              name: 'Add Products',
              icon: ['fas', 'plus'],
              path: '/manageproducts/add',
            }"
          >
          </sidebar-item>
          <sidebar-item
            opened
            :link="{
              name: 'Product Analytics',
              icon: ['fas', 'plus'],
              path: '/manageproducts/analytics',
            }"
          >
          </sidebar-item>
        </sidebar-item>
        <sidebar-item

          :link="{
            name: 'Inventory',
            icon: ['fas', 'plus'],
            path: '',
          }"
        >

          <sidebar-item
            opened
            :link="{
              name: 'All Inventories',
              icon: ['fas', 'plus'],
              path: '/inventory/list',
            }"
          >
          </sidebar-item>
        </sidebar-item>
        <sidebar-item

          :link="{
            name: 'Manage Sales',
            icon: ['fas', 'plus'],
            path: '/managesales',
          }"
        >
          <sidebar-item
            opened
            :link="{
              name: 'Orders',
              icon: ['fas', 'plus'],
              path: '/allproducts',
            }"
          >
          </sidebar-item>

        </sidebar-item>
        <sidebar-item
          :link="{
              name: 'Invoices',
              icon: ['fas', 'plus'],
              path: '/invoice/',
            }"
        >
          <sidebar-item
            :link="{
                name: 'Create Invoice',
                icon: ['fas', 'plus'],
                path: '/invoice/create',
              }"
          >
          </sidebar-item>
          <sidebar-item
            :link="{
                name: 'All Invoices',
                icon: ['fas', 'plus'],
                path: '/invoice/list',
              }"
          >
          </sidebar-item>
        </sidebar-item>
        <sidebar-item
          :link="{
              name: 'Financials',
              icon: ['fas', 'plus'],
              path: '/financialstmts/',
            }"
        >
          <sidebar-item
            :link="{
              name: 'Balance Sheet',
              icon: ['fas', 'plus'],
              path: '/financialstmts/balance-sheet/_slug',
            }"
          >
          </sidebar-item>
          <sidebar-item
            :link="{
              name: 'Income Statement',
              icon: ['fas', 'plus'],
              path: '/financialstmts/profit-loss/_slug',
            }"
          >
          </sidebar-item>
        </sidebar-item>
        <sidebar-item
          :link="{
              name: 'Reports',
              icon: ['fas', 'chart-bar'],
              path: '/reports/',
            }"
        >
          <sidebar-item
            :link="{
              name: 'Report Generation',
              icon: ['fas', 'plus'],
              path: '/reports/charts',
            }"
          >
          </sidebar-item>
        </sidebar-item>
        <sidebar-item
          :link="{
              name: 'Onboarding',
              icon: ['fas', 'plus'],
              path: '/onboarding',
            }"
        >
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

      <div class="" @click="$sidebar.displaySidebar(true)"
      >
        <nuxt class="flex-grow-1"></nuxt>
      </div>
      <content-footer class="flex-shrink-0" v-if="!$route.meta.hideFooter"></content-footer>
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
        data() {
            return {
                user: require('/assets/uploads/user-icon.svg'),

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
