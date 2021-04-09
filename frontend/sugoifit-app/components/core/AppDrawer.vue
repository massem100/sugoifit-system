<template>
  <v-navigation-drawer
    id="app-drawer"
    app
    floating
    mobile-break-point="991"
    width="260"
  >
    <v-img
     style="background: #C7ECF2;"
      height="100%"
    >
      <v-layout
        class="fill-height"
        tag="v-list"
        column
      >
        <v-list dense>
          <v-list-tile avatar to="/">
          <v-list-tile-avatar
            color="white"
          >
              <v-img
                :src="logo"
                height="34"
                contain
              />
            </v-list-tile-avatar>
            <v-list-tile-title class="title">
              SugoiFit Financials
            </v-list-tile-title>
          </v-list-tile>
        </v-list>
        <v-divider/>

        <div class="d-flex flex-row">
          <div class="profile mt-3 mb-2 ">
                <h6 id = "profile_name"> Jane S.</h6>
                <h6  id= "profile_ID"> ID 1234567</h6>
                <h6 id ="role"> Role: Business Owner</h6>     
          </div>
          <img class ="" id = "profile-icon" src="~/assets/uploads/Profile_icon.png" alt="">
         
          </div>


        <v-list dense>
          <v-list-tile
            v-if="responsive"
          >
            <v-text-field
              class="purple-input search-input"
              label="Search..."
              color="purple"
            />
          </v-list-tile>
          <v-list-tile
            v-for="(link, i) in links"
            :key="i"
            :to="link.to"
            avatar
            class="v-list-item"
          >
            <v-list-tile-action>
              <v-icon>{{ link.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-title
              v-text="link.text"
            />
          </v-list-tile>
        </v-list>
      </v-layout>
    </v-img>
  </v-navigation-drawer>
</template>

<script>
  // Utilities
  import { mapActions, mapGetters } from 'vuex'

  export default {
    data() {
      return {
        logo: '/vuetifylogo.png',
        links: [
          {
            to: '/dashboard',
            icon: 'mdi-view-dashboard',
            text: 'Dashboard'
          },
          {
            to: '/user-profile',
            icon: 'mdi-account',
            text: 'Manage Products'
          },
          {
            to: '/table-list',
            icon: 'mdi-clipboard-outline',
            text: 'Manage Sales'
          },
          {
            to: '/typography',
            icon: 'mdi-format-font',
            text: 'Financial Statements'
          },
          {
            to: '/icons',
            icon: 'mdi-chart-bubble',
            text: 'View Reports'
          },
          
        ],
        responsive: true
      }
    },
 
    mounted () {
      this.onResponsiveInverted()
      window.addEventListener('resize', this.onResponsiveInverted)
    },
    beforeDestroy () {
      window.removeEventListener('resize', this.onResponsiveInverted)
    },
    methods: {
        onResponsiveInverted() {
        this.responsive = window.innerWidth < 991;
      }
    }
  }
</script>

<style lang="scss">
  #app-drawer {

    &.v-navigation-drawer .v-list {
      // background: rgba(27, 27, 27, 0.4);
      padding: 0;
    }

    .v-divider {
      margin: 0;
    }

    .v-list__tile {
      border-radius: 4px;

      &--buy {
        margin-top: auto;
        margin-bottom: 17px;
      }

      &__title {
        color: #292929;
      }
    }

    .v-image__image--contain {
      top: 9px;
      height: 60%;
    }

    .search-input {
      margin-bottom: 30px !important;
      padding-left: 15px;
      padding-right: 15px;
    }
  }

  html, body{
    font: 400 1rem "Poppins";
  }
</style>
