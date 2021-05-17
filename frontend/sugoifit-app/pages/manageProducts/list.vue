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
          
            <b-table striped hover :items="allproducts"
                                  :fields="fields" 
                                  :filter="search" 
                                  :per-page="perPage" 
                                  :current-page="currPage">
              <template v-slot:cell(image)="data">
                <img :src="path+'/static/uploads'+data.products.image" alt="">
              </template>
              
              <template v-slot:cell(actions)="data">
                <b-button variant="danger" @click="deleteItem(data.products.id)"> Delete </b-button>
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
              path: 'http://localhost:8080',
              title: 'Products',
            }
        },
        data() {
            return {
                alert_message: '',
                perPage: 5,
                currPage: 1,
                search: '',
                fields: ["name","price","tax","status","image","actions"],
            }
        },
         computed: {
            ...mapGetters(['products/allproducts']),
            rows() {
              return this.$store.state.products.length
            }
        },
        mounted() {
          this.$store.dispatch('products/displayProducts');
        },
        methods: {
            /* ADD AN ALERT OPTION BEFORE DELETING */
            deleteItem(id) {
                const index = this.items.indexOf((x) => x.id == id);
                this.items.splice(index, 1);
            }
        }
    }
</script>

<style scoped>
  /*.row {*/
  /*  display: flex;*/
  /*  flex-direction: row;*/
  /*}*/
  /*  .col {*/
  /*    display: flex;*/
  /*    flex-direction: column;*/
  /*  }*/
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
