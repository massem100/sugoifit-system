<template>
  <div class="d-flex mx-3">
    <b-container fluid>
      <b-row>
        <b-col cols="12" class="text-info mb-3 font-weight-bold">
          <h4>Sales</h4>
          <h6>< Buisness name ></h6>
        </b-col>
        <b-col cols="12" md="4">
          <b-form-datepicker v-model="start_date" class="mb-2"></b-form-datepicker>
        </b-col>
        <b-col cols="12" md="4">
          <b-form-datepicker v-model="end_date" class="mb-2"></b-form-datepicker>
        </b-col>
        <b-col cols="12" md="4">
          <b-button class="mx-3 br-20" variant="info">Search</b-button>
        </b-col>
      </b-row>
      <b-row class="mt-3">
        <b-col cols="12" md="4" class="c-box">
          <label class="mb-0">Customer</label>
          <b-form-input v-model="customer"
                        type="text"
                        class="br-20 m-2"
          >
          </b-form-input>
        </b-col>
        <b-col cols="12" md="4">
          <label class="mb-0">Product</label>
          <b-form-input v-model="product"
                        type="text"
                        class="br-20 m-2"
          >
          </b-form-input>
        </b-col>
        <b-col cols="12" md="4">
          <label class="mb-0">Status</label>
          <b-form-input v-model="status"
                        type="text"
                        class="br-20 m-2"
          >
          </b-form-input>
        </b-col>
        <b-col cols="12" class="my-4">
          <b-table striped hover :items="items" :filter="search" :fields="fields"></b-table>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

    export default {
        layout: 'dashboard',
        name: "Reports",
        data() {
            return {
                search: '',
                start_date: null,
                end_date: null,
                customer: null,
                product: null,
                status: null,
                fields:[
                    {key:'name',label:'Prod/Service Name'},
                    {key:'quantity',label:'Quantity',tdClass:'text-center',thClass:'text-center'},
                    {key:'date',label:'Date',tdClass:'text-center',thClass:'text-center'},
                    {key:'amount',label:'Amount',tdClass:'text-center',thClass:'text-center'},
                    {key:'paid',label:'Amt Paid',tdClass:'text-center',thClass:'text-center'},
                    {key:'customer_name',label:'Cust Name'},
                    {key:'status',label:'Status',tdClass:'text-center',thClass:'text-center'},
                    {key:'tax',label:'Tax',tdClass:'text-center',thClass:'text-center'},
                ],
                items: [
                    {product_id: 1, name: 'A', quantity: 4, amount: 2, paid: 34,customer_name:'asd',status:'pending',tax:'1%',date:'1/4/2021'},
                    {product_id: 2, name: 'B', quantity: 4, amount: 2, paid: 34,customer_name:'asd',status:'pending',tax:'1%',date:'1/4/2021'},
                    {product_id: 3, name: 'C', quantity: 4, amount: 2, paid: 34,customer_name:'asd',status:'pending',tax:'1%',date:'1/4/2021'},
                    {product_id: 4, name: 'A', quantity: 4, amount: 2, paid: 34,customer_name:'asd',status:'pending',tax:'1%',date:'1/4/2021'},
                    {product_id: 5, name: 'D', quantity: 4, amount: 2, paid: 34,customer_name:'asd',status:'pending',tax:'1%',date:'1/4/2021'},
                    {product_id: 6, name: 'E', quantity: 4, amount: 2, paid: 34,customer_name:'asd',status:'pending',tax:'1%',date:'1/4/2021'},
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
