<template>
  <v-navigation-drawer id="app-drawer"
    v-model= "drawer"
    app
    flat
    clipped
    mobile-break-point="991"
    width="280"
    style="background: #A7E4EC;"
    
    @input="navChanged"
  >
    <v-layout
      class="fill-height"
      tag="v-list"
      column
    >
      <v-list dense>
        <v-list-tile avatar to="/">
          <v-list-tile-avatar>
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

      <div class="d-flex flex-row align-items-center mx-3">
        <div class="profile mt-3 mb-2 ">
          <h6 id="profile_name" class="my-1 font-weight-bold"> Jane S.</h6>
          <h6 id="profile_ID" class="my-1"> ID 1234567</h6>
          <h6 id="role" class="my-1"> Role: Business Owner</h6>
        </div>
        <v-img id="profile-icon" :src="user" alt="" aspect-ratio="1" class="mr-2"/>

      </div>


      <v-list>
        <v-list-tile
          v-if="responsive"
          class="my-3"
        >
          <v-text-field
            class="purple-input search-input"
            label="Search..."
            color="purple"
          />
        </v-list-tile>
        <div v-for="(link, i) in links"
             :key="i">
          <v-list-tile
            v-if="link.to"
            :to="link.to"
            active-class="secondary white--text"
            class="v-list-item"
          >
            <v-list-tile-action>
              <v-icon>{{ link.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-title
              v-text="link.text"
            />
          </v-list-tile>
          <v-list-group
            v-else
            class="v-list-item"
            active-class="secondary"
          >
            <template v-slot:activator>
              <v-list-tile>
                <v-list-tile-action>
                  <v-icon>{{ link.icon }}</v-icon>
                </v-list-tile-action>
                <v-list-tile-title>{{ link.text }}</v-list-tile-title>
              </v-list-tile>
            </template>
            <v-list-tile
              v-for="subItem in link.subItems"
              :key="subItem.text"
              :to="subItem.to"
              class="v-list-item"
              active-class="secondary white--text"
            >
              <v-list-tile-content>
                <v-list-tile-title>{{ subItem.text }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list-group>
        </div>


      </v-list>
    </v-layout>
  </v-navigation-drawer>
</template>

<script>
    // Utilities
    import {mapActions, mapGetters} from 'vuex'

    export default {
        data() {
            return {
                logo: require('~/assets/uploads/align-left.png'),
                user: require('~/assets/uploads/Profile_icon.png'),
                links: [
                    {
                        to: '/',
                        icon: 'mdi-view-dashboard',
                        text: 'Dashboard'
                    },
                    {
                        to: null,
                        icon: 'mdi-account',
                        text: 'Manage Products',
                        subItems: [
                            {
                                to: '/manageProducts/list',
                                icon: 'mdi-view-dashboard',
                                text: 'All Products'
                            },
                            {
                                to: '/manageProducts/add',
                                icon: 'mdi-plus',
                                text: 'Add Product'
                            },
                            {
                                to: '/manageProducts/analytics',
                                icon: 'mdi-view-dashboard',
                                text: 'Analytics'
                            }
                        ]
                    },
                    {
                        to: '',
                        icon: 'mdi-clipboard-outline',
                        text: 'Manage Sales',
                         subItems: [
                            {
                                to: '/transaction/sales/create',
                                icon: 'mdi-view-dashboard',
                                text: 'Create Sales'
                            },
                            {
                                to: '/transaction/sales/list',
                                icon: 'mdi-view-dashboard',
                                text: 'All sales'
                            }
                        ]
                    },
                    {
                        to: '/typography',
                        icon: 'mdi-format-font',
                        text: 'Financial Statements'
                    },
                    {
                        to: null,
                        icon: 'mdi-chart-bubble',
                        text: 'View Reports',
                        subItems: [
                            {
                                to: '/reports/charts',
                                icon: 'mdi-view-dashboard',
                                text: 'Charts'
                            },
                            {
                                to: '/projectionsRecommendations',
                                icon: 'mdi-view-dashboard',
                                text: 'Projections & recommendations'
                            }
                        ]
                    },

                ],
                responsive: true
            }
        },
        computed: {
            ...mapGetters({
                drawer: 'app/getDrawer'
            })
        },

        mounted() {
            this.onResponsiveInverted()
            window.addEventListener('resize', this.onResponsiveInverted)
        },
        beforeDestroy() {
            window.removeEventListener('resize', this.onResponsiveInverted)
        },
        methods: {
            ...mapActions({
                setUsername: 'user/setUsername',
                setDrawer: 'app/setDrawer'
            }),
            onResponsiveInverted() {
                this.responsive = window.innerWidth < 991;
            },
            navChanged(e) {
                this.setDrawer(e)
                
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
    .v-list__tile--active{
      .v-list__tile__title {
        color: white!important;
      }
      .title{
        color: #292929!important;
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
</style>
