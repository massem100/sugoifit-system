<template>
  <div class="d-flex mx-3">
    <b-container fluid>
      <b-row>
        <b-col cols="12" class="text-info mb-3 font-weight-bold">View All Products</b-col>
        <b-col cols="12" md="6" lg="4" class="d-flex">
          <b-form-input v-model="search"
                        placeholder="enter product name or ID"
                        type="search"
                        id="product_name"
                        class="br-20"
          >
          </b-form-input>
          <b-button class="mx-3 br-20" variant="light">Search</b-button>
        </b-col>
        <b-col cols="12" class="my-4">
          <b-table striped hover :fields="fields" :items="products" :filter="search" :per-page="perPage" :current-page="currPage">
            <!--<template v-slot:cell(image)="data">
              <img :src="'./app/static/uploads/'+ data.products.image" alt="">
            </template>-->
            
            <template v-slot:cell(actions)="data">
              <b-button variant="danger" @click="deleteItem(data.products.id)"> Delete </b-button>
            </template>
          </b-table>
          <b-pagination v-model="currPage" :total-rows="rows" :per-page="perPage"></b-pagination>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

    export default {
        layout: 'dashboard',
        name: "product-list",
        head() {
            return {
                title: 'Products',
            }
        },
        data() {
            return {
                perPage: 8,
                currPage: 1,
                search: '',
                fields: ["name","price","tax","status","image","actions"],

                products: [],
                
                
            }
        },
        computed: {
          rows() {
            return this.products.length
          }
        },
        async created() {
            const response = await fetch('http://localhost:8080/api/products');
            const data = await response.json();
            this.products = data;
            console.log(this.products);
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
