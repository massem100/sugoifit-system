<template>
  <v-container fluid>
    <v-card>
      <v-card-text>
        <v-row v-if="invoice">
          <v-col cols="12" class="text-center">
            <h3 class="info--text text-capitalize">{{invoice.name}}</h3>
            <h5 class="info--text text-capitalize" v-html="invoice.address"></h5>
          </v-col>
          <v-col cols="12" class="sky text-center py-5">
            <h2 class="text-capitalize info--text">Thank you for your Buisness</h2>
          </v-col>
          <v-col cols="12" class="d-flex py-3 justify-space-between">
            <div class="subtitle-2">
              <div>Employee: Beth</div>
              <div>Customer Name: {{invoice.billed_to.user}}</div>
              <div>Receipt Number: R0001</div>
            </div>
            <div class="text-right subtitle-2">
              Date: {{new Date().toISOString().substr(0,10)}}
            </div>
          </v-col>

          <v-col cols="12" class="my-4 table-responsive">
            <v-simple-table class="custom-table">
              <thead>
              <tr class="br-top br-bottom">
                <th>Description</th>
                <th class="text-center">Quantity</th>
                <th class="text-center">Price</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="(bill,idx) in invoice.bills" :key="bill">
                <td>{{bill.name}}</td>
                <td class="text-center">{{bill.quantity}}</td>
                <td class="text-center">${{bill.unit_price*bill.quantity}}</td>
              </tr>
              <tr>
                <td colspan="3" style="padding-top: 60px"></td>
              </tr>
              <tr class="br-bottom br-top">
                <td class="text-right font-weight-bold" colspan="2">Total</td>
                <td class="text-center font-weight-bold">${{total}}</td>
              </tr>
              </tbody>
            </v-simple-table>
          </v-col>
        </v-row>
      </v-card-text>

    </v-card>

  </v-container>
</template>

<script>
    export default {
        name: "invoice-card",
        layout: 'dashboard',
        data() {
            return {
                invoice: {
                    name: 'moniques botique',
                    invoice_id: 'invoice0001',
                    address: 'Shop #3, xyz plaza,<br> kingsater,<br> Kingston',
                    balance: 1000,
                    billed_to: {
                        user: 'jessica reid',
                        user_mail: 'jess@gmail.com',
                        user_phone: '(844) 43543-345435'
                    },
                    issue_Date: 'March 18, 2021',
                    due_date: 'March 18, 2021',
                    img: require('@/assets/uploads/onboard-img.svg'),
                    bills: [
                        {name: 'Blank tank top', unit_price: 500, quantity: 1},
                        {name: 'Blank Mini skirt', unit_price: 500, quantity: 1}
                    ]
                },
                subtotal: 0,
                total: 0,
                tax: 0
            }
        },
        created() {
            let totalAmount = 0;
            this.invoice.bills.forEach(data => totalAmount = totalAmount + data.unit_price * data.quantity)
            this.subtotal = totalAmount;
            this.total = this.subtotal + this.tax
        }
    }
</script>

<style scoped lang="scss">
  .custom-table {
    th, td {
      padding: 8px 5px;
    }
  }

  .br-top {
    border-top: 1px solid #759297;
  }

  .br-bottom {
    border-bottom: 1px solid #759297;
  }
</style>
