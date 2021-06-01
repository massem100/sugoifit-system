<template>
  <div class="w-100">
    <div class="mx-3">
      <b-row>
        <back-button class="mt-4 ml-2"></back-button>
        <b-col>
            <h3 class="mb-2 mt-4 h2 set-index">Manage Transactions </h3>
            <p class = "mb-2 mt-2 "> 
              Transactions are used to automatically generate your financials. 
              Keep track of your daily transactions.
            </p>
        </b-col>
         

      </b-row>
     
      <transaction-top class="d-flex flex-row justify-content-center mt-4 w-100"/>
 
    
    <b-col class= "mt-4 ml-0 d-flex flex-column align-items-start w-100">
        
        <b-row class="w-100">
           <b-form-group
            label="Filter"
            label-for="filter-input"
            label-cols-sm="3"
            label-align-sm="center"
            label-size="lg"
            class="mb-0"
          >
            <b-input-group 
                size="md"
                class="mb-0">
              <b-form-input
                id="filter-input"
                v-model="filter"
                type="search"
                placeholder="Type to Search"
               
              ></b-form-input>

              <b-input-group-append>
                <b-button variant="primary" :disabled="!filter" @click="filter = ''">Clear</b-button>
              </b-input-group-append>
            </b-input-group>
          </b-form-group>
          <b-form-group
          label="Transaction Type"
          label-for="sort-by-select"
          label-cols-sm="3"
          label-align-sm="right"
          label-size="lg"
          class="mb-0 ml-2 w-50"
          v-slot="{ ariaDescribedby }"
        >
          <b-input-group size="md">
              <b-form-select
                id="sort-by-select"
                v-model="sortBy"
                :options="sortOptions"
                :aria-describedby="ariaDescribedby"
                class=""
              >
                <template #first>
                  <option value="">selec transaction type</option>
                </template>
              </b-form-select>
          </b-input-group>
          </b-form-group>
        </b-row>
        <b-row class="w-100">
            <b-table class = "mt-4 ml-3 w-100 text-black"
                    :items="items" 
                    :fields="fields" 
                    :current-page="currentPage"
                    :per-page="perPage"
                    :filter="filter"
                    :filter-included-fields="filterOn"
                    :sort-by.sync="sortBy"
                    :sort-desc.sync="sortDesc"
                    :sort-direction="sortDirection"
                    show-empty
                    large
                    @filtered="onFiltered"
                    bordered
                    striped 
                    hover
                    head-row-variant="white"
                    responsive="sm"
                    variant="primary"> 
              <template #cell(actions)="row">
                  <b-button size="sm" variant="primary" @click="row.toggleDetails" class="mr-2">
                     Adjust
                  </b-button>
                  <b-button size="sm" variant="danger" @click="row.toggleDetails" class="mr-2">
                    Delete
                  </b-button>
                  
              </template>
         

            </b-table>
            <b-pagination class="m-lg-auto" v-model="currentPage" :total-rows="totalRows" :per-page="perPage"></b-pagination>
        </b-row>
      </b-col>
    </div>
  </div>
</template>

<script>


import BackButton from '../components/argon-core/BackButton.vue';

    export default {
        components: {  BackButton },
        name: "manage-transaction",
        layout: 'DashboardLayout',
        head(){
          return{
              title: 'Transactions'
          }
        },
        methods: {
            addTransaction: () => {
                console.log('working');
            }
        },
        data() {
            return {
                transForm: null,
                assetName: "",
                assetType: "",
                depreciationMethod: "",
                sortOptions:{},
                el: "",
                // totalRows: null,
                currentPage: 1,
                perPage: 8,
                pageOptions: [5, 10, 15, { value: 100, text: "Show a lot" }],
                sortBy: '',
                sortDesc: false,
                sortDirection: 'asc',
                filter: null,
                filterOn: [],
                // fields: ['date', 'transaction_id', 'transaction_name', 'related_entry', 'amount', 'actions'],
                items: [],
                fields: [
                          {key:'date', sortable: true},
                          {key: 'transaction_id', sortable: false},
                          {key: 'transaction_name', sortable: true},
                          {key: 'related_entry', sortable: false}, 
                          {key:'amount', sortable: true},
                          {key:'actions', sortable: false},
              
                        ],
            };
                
        },
        created(){


        }, 
        computed: {
             totalRows(){
               return this.items.length;
          }
      
        }, 
        watch:{
         
        }, 
        mounted() {
            // Set the initial number of items
          let self=this;
  
          const busID = localStorage.getItem('busID');
          this.$axios.get(`/api/transactions/${busID}`
              ).then(res =>{
                  return res.data;
              }).then(res =>{
                  if (res){
                      self.items = res.transaction;
                      console.log(res);
                      // this.totalRows = this.res.transaction.length; 
              
              }else{
                  console.log('Data not found')
              }
              });
          },
        methods:{
          onFiltered(filteredItems) {
            this.totalRows = filteredItems.length
            this.currentPage = 1
          },
           async launchConfirm(){
                let self = this;
                const submit = await this.$refs['confirmModal'].show();
              
            },
            
        }
    };
</script>


<style>
  .box {
    width: 130px;
    height: 120px;
    text-align: center;
    font-size: 30px;
  }


</style>
