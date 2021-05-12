<template>
  <div class="m-3">
    <b-container fluid>
      <b-card>
        <h2 class="mb-4">Settings</h2>
        <b-tabs content-class="mt-3">
          <b-tab :title="item"
                 v-for="(item,idx) in level2TabItems"
                 :key="item"
                 :active="idx===0"
          >
            <div>
              <div v-if="idx===0">
                <profile-create></profile-create>
              </div>
              <div v-if="idx===1">
                <company-create></company-create>
              </div>
              <div v-if="idx===2">
                <website-create></website-create>
              </div>
              <div v-if="idx===3">
                <user-management></user-management>
              </div>
            </div>
          </b-tab>
        </b-tabs>
      </b-card>

    </b-container>
  </div>
</template>

<script>

    import ProfileCreate from "../../components/settings/profile-create";
    import CompanyCreate from "../../components/settings/company-create";
    import WebsiteCreate from "../../components/settings/website-create";
    import BusinessCreate from "../../components/settings/buisness-create";
    import UserManagement from "../../components/settings/user-management";
    export default {
        name: "index",
        components: {UserManagement, BusinessCreate, WebsiteCreate, CompanyCreate, ProfileCreate},
        layout: 'DashboardLayout',
        data() {
            return {
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
