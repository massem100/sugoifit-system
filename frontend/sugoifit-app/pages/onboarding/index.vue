<template>
  <div class="m-3">
    <b-container fluid>
      <b-card>
        <h2 class="mb-4">Setting up your business</h2>
        <b-tabs content-class="mt-3" v-model="tabIndex">
          <b-tab :title="item"
                 v-for="(item,idx) in TabItems"
                 :key="item"
                 :active="idx===0"
          >
            <div>
              <div v-if="idx===0">
               <business-setup></business-setup>
                <b-col cols="12" class="text-right my-3">
                  <b-button @click="tabIndex=1">Next</b-button>
                </b-col>
              </div>
              <div v-if="idx===1">
                <business-detail></business-detail>
                <b-col cols="12" class="text-right my-3">
                  <b-button @click="tabIndex=0" class="mx-3">Previous</b-button>
                  <b-button @click="tabIndex=2">Next</b-button>
                </b-col>
              </div>
              <div v-if="idx===2">
                <personal-detail></personal-detail>
                <b-col cols="12" class="text-right my-3">
                  <b-button @click="tabIndex=1" class="mx-3">Previous</b-button>
                  <!-- <b-button @click="tabIndex=3">Next</b-button> -->
                  <b-button>Done</b-button>
                </b-col>
              </div>
              <!-- <div v-if="idx===3">
                <add-team></add-team>
                <b-col cols="12" class="text-right my-3">
                  <b-button @click="tabIndex=2" class="mx-3">Previous</b-button>
                  <b-button>Done</b-button>
                </b-col>
              </div> -->
            </div>
          </b-tab>
        </b-tabs>
      </b-card>

    </b-container>
  </div>
</template>

<script>

    import BusinessSetup from "../../components/onboarding/business-setup";
    import BusinessDetail from "../../components/onboarding/business-details";
    import PersonalDetail from "../../components/onboarding/personal-details";
    import AddTeam from "../../components/onboarding/add-team";

    export default {
        name: "index",
        components: {BusinessDetail, BusinessSetup,PersonalDetail,AddTeam},
        layout: '',
        data() {
            return {
                tabIndex:0,
                TabItems: [
                    'Business Profile', 'Business Details', 'Personal Details'
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
