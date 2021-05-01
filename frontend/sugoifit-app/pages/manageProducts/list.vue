<template>
  <div class="d-flex mx-3">
    <b-container fluid>
      <b-row>
        <b-col cols="12" class="text-info mb-3 font-weight-bold">View All Products</b-col>
        <b-col cols="12" md="6" lg="4" class="d-flex">
          <b-form-input v-model="search"
                        type="text"
                        id="product_name"
                        class="br-20"
          >
          </b-form-input>
          <b-button class="mx-3 br-20" variant="light">Search</b-button>
        </b-col>
        <b-col cols="12" class="my-4">
          <b-table striped hover :items="items" :filter="search"></b-table>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

    export default {
        layout: 'DashboardLayout',
        name: "Reports",
        data() {
            return {
                search: '',
                items: [
                    {product_id: 1, product_name: 'A', unit: 4, threshold: 2, unit_price: 34},
                    {product_id: 2, product_name: 'B', unit: 4, threshold: 2, unit_price: 34},
                    {product_id: 3, product_name: 'C', unit: 4, threshold: 2, unit_price: 34},
                    {product_id: 4, product_name: 'D', unit: 4, threshold: 2, unit_price: 34},
                    {product_id: 5, product_name: 'E', unit: 4, threshold: 2, unit_price: 34},
                ]
            }
        },
        head() {
            return {
                title: 'Reports',
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
