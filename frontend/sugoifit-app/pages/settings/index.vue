<template>
  <div class="mx-3">
    <client-only>
      <h5 class="mb-0">Settings</h5>
      <v-container fluid>

        <v-tabs
          v-model="level2Tab"
          align-with-title
        >
          <v-tabs-slider color="yellow"></v-tabs-slider>
          <v-tab
            v-for="item in level2TabItems"
            :key="item"
          >
            {{ item }}
          </v-tab>
        </v-tabs>
        <v-tabs-items v-model="level2Tab">
          <v-tab-item
            key="0"
          >
            <v-card class="shadow-none">
              <v-card-text>
                <profile-create/>
              </v-card-text>
            </v-card>
          </v-tab-item>
          <v-tab-item
            key="1"
          >
            <v-card class="shadow-none">
              <v-card-text>
                <company-create/>
              </v-card-text>
            </v-card>
          </v-tab-item>
          <v-tab-item
            key="2"
          >
            <v-card class="shadow-none">
              <v-card-text>
                <template v-for="(singleItem, ind2) in formList">
                  <div :key="ind2">
                    <h6 class="text-info card-subtitle ">{{singleItem.heading}}</h6>
                    <div class="d-flex w-50 offset-lg-1" v-for="(singleSubItem, ind3) in singleItem.subItems"
                         :key="ind3">
                      <span class="align-self-center">{{singleSubItem.title}}:</span>
                      <v-text-field
                      ></v-text-field>
                    </div>
                  </div>

                </template>

              </v-card-text>
              <v-card-text>
                <h6 class="text-info card-subtitle ">Positions:</h6>
                <div class="d-flex w-75 offset-lg-1">
                  <span class="align-self-center">Drag Section to change:</span>
                  <div>
                    <v-data-table
                      :headers="headers1"
                      :items="desserts1"
                      loading
                      loading-text="Loading... Please wait"
                      :items-per-page="3"
                      class="elevation-1"
                    >
                      <template v-slot:items="props">

                        <td>{{ props.item.position }}</td>
                        <td>{{ props.item.section_name }}</td>
                        <td>
                          <b-button
                            variant="link"
                            class="text-danger"
                          >
                            delete
                          </b-button>
                        </td>
                      </template>

                    </v-data-table>
                  </div>
                </div>
              </v-card-text>
            </v-card>

          </v-tab-item>
          <v-tab-item
            key="3"
          >
            <v-card class="shadow-none">
              <div>
                <v-data-table
                  :headers="headers2"
                  :items="desserts2"
                  loading
                  loading-text="Loading... Please wait"
                  :items-per-page="3"
                  class="elevation-1"
                >
                  <template v-slot:items="props">

                    <td>
                      <v-avatar>
                        <v-img
                          class="elevation-6"
                          alt=""

                          :src="require('../../assets/uploads/Profile_icon.png')"
                        ></v-img>
                        <span class="ml-2">{{props.item.user_name}}</span>
                      </v-avatar>
                    </td>
                    <td>{{ props.item.role }}</td>
                    <td class="d-flex justify-content-around">
                      <b-button
                        variant="link"
                        class="text-danger"
                      >
                        edit
                      </b-button>
                      <b-button
                        variant="link"
                        class="text-danger"
                      >
                        delete
                      </b-button>
                    </td>
                  </template>

                </v-data-table>
                <v-card class="d-flex justify-end shadow-none p-4">
                  <div align="end">
                    <b-button pill variant="info">add user</b-button>
                    <b-button pill variant="info">Save</b-button>
                  </div>
                </v-card>
              </div>
            </v-card>
          </v-tab-item>
        </v-tabs-items>
        <!--        <v-card class="d-flex justify-end shadow-none">-->
        <!--          <div align="end">-->
        <!--            <b-button pill variant="info" size="lg">Save Changes</b-button>-->
        <!--          </div>-->
        <!--        </v-card>-->
      </v-container>
    </client-only>
  </div>
</template>

<script>
    export default {
        name: "index",
        layout: 'dashboard',
        data() {
            return {
                level2Tab: null,
                level2TabItems: [
                    'Your Profile', 'Your Company', 'Your Website', 'Your Managemnet',
                ],
                text: 'test',
                formList: [
                    {
                        heading: 'Welcome Section',
                        subItems: [
                            {title: 'Welcome Heading'},
                            {title: 'Welcome Message'},
                            {title: 'Welcome Image'},
                        ]
                    },
                    {
                        heading: 'Product Section',
                        subItems: [
                            {title: 'Product Heading'},
                        ]
                    },
                    {
                        heading: 'Receipt Section',
                        subItems: [
                            {title: 'Receipt Heading'},
                            {title: 'Receipt Message'},
                        ]
                    },
                    {
                        heading: 'Contact Section',
                        subItems: [
                            {title: 'Contact Heading'},
                        ]
                    },
                ],
                headers1: [
                    {
                        text: 'Position',
                        value: 'position',
                        align: 'start'
                    },
                    {
                        text: 'Section Name',
                        value: 'section_name',
                        align: 'start'
                    },
                    {text: 'Method', value: 'actions', align: 'center', sortable: false}
                ],
                desserts1: [
                    {
                        position: '1',
                        section_name: 'Welcome'
                    },
                    {
                        position: '2',
                        section_name: 'Receipt'
                    },
                    {
                        position: '3',
                        section_name: 'Contact'
                    },
                    {
                        position: '4',
                        section_name: 'Welcome'
                    },
                    {
                        position: '5',
                        section_name: 'Receipt'
                    },
                    {
                        position: '6',
                        section_name: 'Contact'
                    },
                    {
                        position: '7',
                        section_name: 'Welcome'
                    },
                    {
                        position: '8',
                        section_name: 'Receipt'
                    },
                    {
                        position: '9',
                        section_name: 'Contact'
                    },

                ],
                headers2: [
                    {
                        text: 'User Name',
                        value: 'user_name',
                        align: 'start'
                    },
                    {
                        text: 'Role',
                        value: 'role',
                        align: 'start'
                    },
                    {text: 'Method', value: 'actions', align: 'center', sortable: false}
                ],
                desserts2: [
                    {
                        user_name: '1',
                        role: 'Business Owner'
                    },
                    {
                        user_name: '2',
                        role: 'Employee'
                    },
                    {
                        user_name: '3',
                        role: 'Finanace Manage',
                    },


                ],
            }
        },
        mounted() {
            // console.log(this.desserts1)
        }
    }
</script>

<style scoped>

</style>
