<template>
  <v-container>
      <v-row>
        <v-col cols="12" class="info--text mb-3 font-weight-bold">View Invoices</v-col>
        <v-col cols="12" lg="4" xl="3" class="d-flex">
          <v-text-field v-model="search"
                        label="Search"
          >
          </v-text-field>
        </v-col>
        <v-col cols="12" class="my-3" v-for="(invoice,idx) in invoices" :key="idx">
          <invoice-card :invoice="invoice"></invoice-card>
        </v-col>
      </v-row>
    </v-container>
</template>

<script>

    import InvoiceCard from "../../components/invoice-card";

    export default {
        components: {InvoiceCard},
        layout: 'dashboard',
        name: "invoice-list",
        data() {
            return {
                search: '',
                invoices: [
                    {
                        name: 'moniques botique',
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
                        name: 'moniques botique 2',
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
                        name: 'moniques botique 3',
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

