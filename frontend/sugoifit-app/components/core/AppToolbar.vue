<template>
  <v-toolbar
    id="core-toolbar"
    flat
    prominent
    style="background: #7CC3CD;"
  >
    <div class="v-toolbar-title">
      <v-toolbar-title
        class="white--text ml-4 font-weight-light"
      >
        <v-btn
          v-if="responsive"
          class="default v-btn--simple"
          light
          icon
          @click.stop="onClickBtn"
        >
          <v-icon>mdi-view-list</v-icon>
        </v-btn>
        {{ title }}
      </v-toolbar-title>
    </div>

    <v-spacer />
    <v-toolbar-items>
      <v-flex
        align-center
        layout
        py-2
      >
        <v-text-field
          v-if="responsiveInput"
          class="mr-4 mt-2 "
          label="Search..."
          hide-details
        />
        <nuxt-link
          v-ripple
          class="toolbar-items"
          to="/"
          title="Dashboard"
        >
          <v-icon color="white">mdi-view-dashboard</v-icon>
        </nuxt-link>
        <v-menu
          bottom
          left
          content-class="dropdown-menu"
          offset-y
          transition="slide-y-transition">
          <router-link
            v-ripple
            slot="activator"
            class="toolbar-items"
            to="/notifications"
          >
            <v-badge
              color="error"
              overlap
            >
              <template slot="badge">
                {{ notifications.length }}
              </template>
              <v-icon color="white">mdi-bell</v-icon>
            </v-badge>
          </router-link>
          <v-card>
            <v-list dense>
              <v-list-tile
                v-for="notification in notifications"
                :key="notification"
                @click="onClick"
              >
                <v-list-tile-title
                  v-text="notification"
                />
              </v-list-tile>
            </v-list>
          </v-card>
        </v-menu>
        <nuxt-link
          v-ripple
          class="toolbar-items"
          to="/user-profile"
          title="User profile"
        >
          <v-icon color="white">mdi-account</v-icon>
        </nuxt-link>
        <nuxt-link
          v-ripple
          class="toolbar-items"
          to="/"
          title="Logout"
          @click.native="logout"
        >
          <v-icon color="white">mdi-logout</v-icon>
        </nuxt-link>
      </v-flex>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    data: () => ({
      notifications: [
        
      ],
      title: 'Dashboard',
      responsive: true,
      responsiveInput: true
    }),
    watch: {
      '$route' (val) {
        this.title = val.name === 'index'?'Dashboard':val.name
      }
    },
    computed: {
      ...mapGetters({
        drawer: 'app/getDrawer'
      })
    },
    methods: {
      ...mapActions({
        setUsername: 'user/setUsername',
        setDrawer: 'app/setDrawer'
      }),

      onClickBtn () {
        this.setDrawer(!this.drawer)
      },
      onClick () {
        // Do something
      },
      onResponsiveInverted () {
        if (window.innerWidth < 991) {
          this.responsive = true
          this.responsiveInput = false
        } else {
          this.responsive = false
          this.responsiveInput = true
        }
      },
        logout: function() {
        let PATH_API = 'auth/logout';
        this.$axios.get(`/api/${PATH_API}`, {
          headers: {
          'contentType': 'application/json',
          }
        })
        .then(function (jsonResponse) {
          return jsonResponse.json();
        })
        .then(function (jsonResponse) {
          // this.setUsername(null);
          this.$router.push({ path: '/auth/login'});
        }), error =>{
            console.log(error);
          }},        
    },
    mounted () {
      this.onResponsiveInverted()
      window.addEventListener('resize', this.onResponsiveInverted)
    },
    beforeDestroy () {
      window.removeEventListener('resize', this.onResponsiveInverted)
    }
  }
</script>

<style>
  #core-toolbar a {
    text-decoration: none;
  }
</style>
