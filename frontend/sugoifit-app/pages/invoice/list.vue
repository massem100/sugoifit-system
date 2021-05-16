<template>
  <div class="d-flex mx-3">
    <b-container fluid>
      <b-row>
        <back-button class="mt-4 ml-2"></back-button>
        <b-col cols="12" class="text-info mb-3 font-weight-bold">View Invoices</b-col>
        <b-col cols="12" lg="6" xl="4" class="d-flex">
          <b-form-input v-model="search"
                        type="text"
                        id="product_name"
                        class="br-20"
          >
          </b-form-input>
          <b-button class="mx-3 br-20" variant="light">Search</b-button>
        </b-col>
        <b-col cols="12" class="my-3" v-for="(invoice,idx) in invoices" :key="idx">
          <invoice-card :invoice="invoice"></invoice-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

    import InvoiceCard from "../../components/invoice-card";
    import BackButton from '../../components/argon-core/BackButton.vue';
    export default {
        components: {InvoiceCard, BackButton},
        layout: 'DashboardLayout',
        name: "invoice-list",
        head(){
          return{
              title: 'Invoice List'
          }
        },
        data() {
            return {
                search: '',
                invoices: [
                    {
                        name: 'moniques boutique',
                        invoice_id: 'invoice0001',
                        balance: 1000,
                        billed_to:{
                            user:'jessica reid',
                            user_mail:'jess@gmail.com',
                            user_phone:'(844) 43543-345435'
                        },
                        issue_Date:'March 18, 2021',
                        due_date:'March 18, 2021',
                        img:require('../../assets/uploads/onboard-img.svg')
                    },
                    {
                        name: 'moniques boutique 2',
                        invoice_id: 'invoice0002',
                        balance: 1000,
                        billed_to:{
                            user:'jessica reid',
                            user_mail:'jess@gmail.com',
                            user_phone:'(844) 43543-345435'
                        },
                        issue_Date:'March 18, 2021',
                        due_date:'March 18, 2021',
                        img:require('../../assets/uploads/onboard-img.svg')
                    },
                    {
                        name: 'moniques boutique 3',
                        invoice_id: 'invoice0003',
                        balance: 1000,
                        billed_to:{
                            user:'jessica reid',
                            user_mail:'jess@gmail.com',
                            user_phone:'(844) 43543-345435'
                        },
                        issue_Date:'March 18, 2021',
                        due_date:'March 18, 2021',
                        img:require('../../assets/uploads/onboard-img.svg')
                    }
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

