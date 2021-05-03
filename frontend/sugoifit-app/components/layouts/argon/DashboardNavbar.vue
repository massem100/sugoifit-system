<template>
  <base-nav container-classes="container-fluid" class="navbar-top border-bottom navbar-expand "
            :class="{ 'bg-primary navbar-light': type === 'default' }">  
            <!-- <i @click = "toggleSidebar" class = "ni ni-lg ni-align-left-2 text-white mt-2 mb-2 mr-4 "></i> -->
          <h4  class = " font-weight-bold mt-2 mr-3 h3 text-white "> SugoiFit Financials</h4>
         
    <!-- Search form -->
    <form id="navbar-search-main" class="navbar-search ml-lg-auto form-inline mr-sm-3"
          :class="{
                    'navbar-search-light': type === 'default',
                    'navbar-search-dark': type === 'light',
                  }">
      <div class="form-group mb-0">
        <div class="input-group input-group-alternative input-group-merge">
          <div class="input-group-prepend">
            <span class="input-group-text"><i class="fas fa-search"></i></span>
          </div>
          <input class="form-control" placeholder="Search" type="text" />
        </div>
      </div>
      <button type="button" class="close" data-action="search-close" data-target="#navbar-search-main"
              aria-label="Close" > <span aria-hidden="true">×</span>
      </button>
    </form>

    <!-- Navbar links -->
    <i class="ni ni-lg ni-bell-55 m-2 text-white"></i>
    <i class="ni ni-lg ni-circle-08 m-2 text-white"></i>
    <b-link class="m-0" :to = "{name: 'settings-main'}">
      <b-nav-item-dropdown toggle-class="text-decoration-none"  no-caret>
          <!-- Using 'button-content' slot -->
          <template #button-content>
            <i class="ni ni-lg ni-settings-gear-65 m-2 text-white"></i>
          </template>
          <b-dropdown-item ><b-link :to="{name: 'settings-business-create'}">Business Profile</b-link></b-dropdown-item>
          <b-dropdown-item ><b-link :to="{name: 'settings-profile-create'}">User Profile</b-link></b-dropdown-item>
          <b-dropdown-item ><b-link :to="{name: 'settings-website-create'}"> Edit Website</b-link></b-dropdown-item>
        </b-nav-item-dropdown>
        </b-link>
    <i @click="Logout" class="ni ni-lg ni-button-power m-2 text-white"></i>
    
  </base-nav>
</template>
<script>
import { CollapseTransition } from "vue2-transitions";
import BaseNav from "@/components/argon-core/Navbar/BaseNav.vue";
import Modal from "@/components/argon-core/Modal.vue";
import { pick, merge } from "lodash";

export default {
  components: {
    CollapseTransition,
    BaseNav,
    Modal,
  },
  props: {
    type: {
      type: String,
      default: "default", // default|light
      description:
        "Look of the dashboard navbar. Default (Green) or light (gray)",
    },
  },
 
  data() {
    return {
      activeNotifications: false,
      showMenu: false,
      searchModalVisible: false,
      searchQuery: "",
    };
  },
  methods: {
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    toggleNotificationDropDown() {
      this.activeNotifications = !this.activeNotifications;
    },
    closeDropDown() {
      this.activeNotifications = false;
    },
    toggleSidebar() {
      this.$sidebar.displaySidebar(!this.$sidebar.showSidebar);
    },
    hideSidebar() {
      this.$sidebar.displaySidebar(false);
    },
    Logout: function() {
        let PATH_API = 'auth/logout';
        this.$axios.get(`/api/${PATH_API}`, {
          headers: {
          'contentType': 'application/json',
          }
        })
        .then(function (jsonResponse) {
          return jsonResponse.data;
        })
        .then(function (jsonResponse) {
          // this.setUsername(null);
          $nuxt.$router.push({ name:'auth-Login'});
        }).catch( err =>{
            console.log(err);
         });
    }, 
    
  },
};
</script>
