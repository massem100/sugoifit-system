<template>
  <client-only>
    <v-container
      fill-height
      fluid
      grid-list-xl>
      <v-layout
        justify-center
        wrap
      >
        <v-flex
          xs12
          md8
        >
          <v-tabs v-model="level1Tab">
            <v-tab v-for="(mainItem, ind1) in level1TabItems" :key="ind1">
              {{mainItem}}
            </v-tab>
          </v-tabs>
          <v-tabs-items v-model="level1Tab">
            <v-tab-item v-for="(mainItem, ind1) in level1TabItems" :key="ind1">
              <!--            edit profile section-->
              <v-card class="shadow-none" v-if="ind1 == 0">
                <material-card
                  color="green"
                  title="Edit Profile"
                  text="Complete your profile"
                >
                  <v-form>
                    <v-container py-0>
                      <v-layout wrap>
                        <v-flex
                          xs12
                          md4
                        >
                          <v-text-field
                            label="Company (disabled)"
                            disabled/>
                        </v-flex>
                        <v-flex
                          xs12
                          md4
                        >
                          <v-text-field
                            class="purple-input"
                            label="User Name"
                          />
                        </v-flex>
                        <v-flex
                          xs12
                          md4
                        >
                          <v-text-field
                            label="Email Address"
                            class="purple-input"/>
                        </v-flex>
                        <v-flex
                          xs12
                          md6
                        >
                          <v-text-field
                            label="First Name"
                            class="purple-input"/>
                        </v-flex>
                        <v-flex
                          xs12
                          md6
                        >
                          <v-text-field
                            label="Last Name"
                            class="purple-input"/>
                        </v-flex>
                        <v-flex
                          xs12
                          md12
                        >
                          <v-text-field
                            label="Adress"
                            class="purple-input"/>
                        </v-flex>
                        <v-flex
                          xs12
                          md4>
                          <v-text-field
                            label="City"
                            class="purple-input"/>
                        </v-flex>
                        <v-flex
                          xs12
                          md4>
                          <v-text-field
                            label="Country"
                            class="purple-input"/>
                        </v-flex>
                        <v-flex
                          xs12
                          md4>
                          <v-text-field
                            class="purple-input"
                            label="Postal Code"
                            type="number"/>
                        </v-flex>
                        <v-flex xs12>
                          <v-textarea
                            class="purple-input"
                            label="About Me"
                            value="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                          />
                        </v-flex>
                        <v-flex
                          xs12
                          text-xs-right
                        >
                          <v-btn
                            class="mx-0 font-weight-light"
                            color="success"
                          >
                            Update Profile
                          </v-btn>
                        </v-flex>
                      </v-layout>
                    </v-container>
                  </v-form>
                </material-card>
              </v-card>
              <!--            settings section-->
              <v-card class="shadow-none" v-if="ind1 == 1">
                <SettingsComponent />
              </v-card>
            </v-tab-item>
          </v-tabs-items>

        </v-flex>
        <v-flex
          xs12
          md4
        >
          <material-card class="v-card-profile">
            <v-avatar
              slot="offset"
              class="mx-auto d-block"
              size="130"
            >
              <img
                src="https://demos.creative-tim.com/vue-material-dashboard/img/marc.aba54d65.jpg"
              >
            </v-avatar>
            <v-card-text class="text-xs-center">
              <h6 class="category text-gray font-weight-thin mb-3">{{ user.function }}</h6>
              <h4 class="card-title font-weight-light">{{ fullname }}</h4>
              <p class="card-description font-weight-light">{{ user.description }}</p>
              <blockquote class="blockquote">{{ user.citation }}</blockquote>
              <v-btn
                color="success"
                round
                class="font-weight-light"
              >Follow</v-btn>
            </v-card-text>
          </material-card>
        </v-flex>
      </v-layout>
    </v-container>
  </client-only>
</template>

<script>
  import { mapGetters } from 'vuex'
  import materialCard from '~/components/material/AppCard'
  import SettingsComponent from "../components/SettingsComponent";

  export default {
    layout: 'dashboard',
    data() {
      return {
        level1Tab: null,
        level1TabItems: ['Edit Profile', 'Settings'],

      }
    },
    components: {
      materialCard,
      SettingsComponent
    },
    computed: {
      ...mapGetters({
        user: 'user/getUser',
        fullname: 'user/getFullname',
      })
    }
  }
</script>
