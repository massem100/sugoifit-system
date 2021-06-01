<template>
  <div class="d-flex mx-3">
    <b-container fluid>
      <base-alert v-if= "alert_message" 
                    class = "mt-5 d-flex flex-row justify-content-center" 
                    style="width: 25rem; 
                           height: 3rem; 
                           z-index:1;" 
                    dismissible      
                    type= "primary">{{message}}
      </base-alert>
      <b-row>
        <back-button class="mt-4 ml-2"></back-button>
        <b-col>
           <h3 class="mt-4 ml-0">Manage Products</h3>
            <p class = "mb-2 mt-2 ">  
                Keep track of your products.
              </p>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="12" class="text-info ml-5 mt-4 mb-3 font-weight-bold">View All Products</b-col>
        <b-col cols="12" md="6" lg="4" class="d-flex ml-5">
          <b-form-input v-model="search"
                        placeholder="enter product name or ID"
                        type="search"
                        id="product_name"
                        class="br-20"
          >
          </b-form-input>
          <b-button class="mx-3 br-20" variant="light">Search</b-button>
        </b-col>
        </b-row>

        <b-col cols="12" class="my-4">
          
            <b-table striped hover :items="products"
                                  :fields="fields" 
                                  :filter="search" 
                                  :per-page="perPage" 
                                  :current-page="currPage">
             <template #cell(image)="data" >
                <img class="d-flex flex-row justify-content-center" style="width: 4rem; height: 4rem;" :src="path + data.value" alt="">
              </template>
                <template #cell(actions)="data">
                  <b-button size="sm" variant="primary"  class="mr-2">
                     Edit
                  </b-button>
                  <b-button size="sm" variant="danger" @click="deleteProduct(data.item.prodID)" class="mr-2">
                    Delete
                  </b-button>
                  
              </template>
           
            </b-table> 
          
          <b-pagination v-model="currPage" :total-rows="rows" :per-page="perPage"></b-pagination>
        </b-col>
    </b-container>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex';
  import BaseAlert from '../../components/argon-core/BaseAlert.vue';
  import BackButton from '../../components/argon-core/BackButton.vue';
    export default {
      components: { BackButton, BaseAlert },
        layout: 'DashboardLayout',
        name: "product-list",
        head(){
          return{
              title: 'Product List'
          }
        },
        data() {
            return {
                path: 'http://localhost:8080/static/uploads/',
                title: 'Products',
                alert_message: '',
                perPage: 5,
                currPage: 1,
                search: '',
                fields: ["image","prodName","unit_price","taxPercent","prodStatus","actions"],
                product_lst: this.products,
            }
        },
        created(){
            this.$store.dispatch('products/displayProducts');
        },
        computed: {
            ...mapGetters({
              products: 'products/allProducts',
            }),         
           
            rows() {
              return this.products.length
            }
        },
        mounted() {
        },
        methods: {
            /* ADD AN ALERT OPTION BEFORE DELETING */
            deleteProduct(id) {
                this.$store.dispatch('products/deleteProduct', id);
                
            }
        }
    }
</script>

<style scoped>
  #chartDiv {
    width: 50%;
    height: 30%;
    position: absolute;
    top: 300px;
    right: 80px;
  }

  .side-bar {
    position: fixed;
  }

  .dashboard-main {
    margin-left: 20rem;
  }
</style>
