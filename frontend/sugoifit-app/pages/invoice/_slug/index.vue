<template>
  <div class="d-flex mx-3">
    <v-container fluid>
      <v-card>
        <v-card-text>
          <v-row>
          <v-card-title class="info--text mb-3 font-weight-bold text-capitalize">Invoice of {{invoice.billed_to.user}}</v-card-title>
          <v-col cols="12" v-if="invoice">
            <v-row style="border-bottom: 2px solid #00bcd4" class="mx-0 pb-3">
              <v-col sm="2" cols="12">
                <v-img :src="invoice.img" thumbnail></v-img>
              </v-col>
              <v-col sm="10" cols="12">
                <v-row>
                  <v-col sm="6" cols="12">
                    <div class="info--text text-capitalize text-h6">{{invoice.name}}</div>
                    <div class="mb-2">
                      <h4 class="my-0 info--text">Invoice ID:<span class="ml-3 grey--text">{{invoice.invoice_id}}</span>
                      </h4>
                    </div>
                    <div class="mb-2">
                      <h4 class="my-0 info--text">Address:<span class="ml-3 grey--text">{{invoice.address}}</span></h4>
                    </div>
                  </v-col>
                  <v-col sm="6" cols="12" class="mb-2">
                    <v-row>
                      <h4 class="my-0 info--text col-12 col-md-6 pa-1">Balance Due:</h4>
                      <h3 class="my-0 font-weight-bold col-12 col-md-6 pa-1">${{invoice.balance}}</h3>
                      <h4 class="my-0 info--text col-12 col-md-6 pa-1">Date Issued:</h4>
                      <h4 class="my-0 col-12 col-md-6 pa-1">{{invoice.issue_Date}}</h4>
                      <h4 class="my-0 info--text col-12 col-md-6 pa-1">Due Date:</h4>
                      <h4 class="my-0 col-12 col-md-6 pa-1">{{invoice.due_date}}</h4>
                      <h4 class="my-0 info--text col-12 col-md-6 pa-1">Billed to:</h4>
                      <h4 class="my-0 col-12 col-md-6 pa-1">
                        {{invoice.billed_to.user}}<br>
                        {{invoice.billed_to.user_mail}}<br>
                        {{invoice.billed_to.user_phone}}
                      </h4>
                    </v-row>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
          </v-col>
          <v-col cols="12" class="my-4 table-responsive">
            <v-simple-table class="custom-table">
              <thead>
              <tr>
                <th class="info--text">Description</th>
                <th class="text-center info--text">Unity Price</th>
                <th class="text-center info--text">Quantity</th>
                <th class="text-center info--text">Amount</th>
              </tr>
              </thead>
              <tbody>
              <tr class="br-bottom" v-for="(bill,idx) in invoice.bills" :key="bill">
                <td>{{bill.name}}</td>
                <td class="text-center">${{bill.unit_price}}</td>
                <td class="text-center">{{bill.quantity}}</td>
                <td class="text-center">${{bill.unit_price*bill.quantity}}</td>
              </tr>
              <tr>
                <td class="text-right info--text" colspan="3" style="padding-top: 80px">Subtotal</td>
                <td class="text-center" style="padding-top: 80px">${{subtotal}}</td>
              </tr>
              <tr class="br-bottom">
                <td class="text-right info--text" colspan="3">Tax</td>
                <td class="text-center">${{tax.toFixed(2)}}</td>
              </tr>
              <tr>
                <td class="text-right font-weight-bold info--text" colspan="3">Total</td>
                <td class="text-center font-weight-bold">${{total}}</td>
              </tr>
              </tbody>
            </v-simple-table>
          </v-col>
        </v-row>
        </v-card-text>

      </v-card>

    </v-container>
  </div>
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
                    address: 'Shop #3, xyz plaza. kingsater, Kingston',
                    balance: 1000,
                    billed_to: {
                        user: 'jessica reid',
                        user_mail: 'jess@gmail.com',
                        user_phone: '(844) 43543-345435'
                    },
                    issue_Date: 'March 18, 2021',
                    due_date: 'March 18, 2021',
                    img: require('../../../assets/uploads/onboard-img.svg'),
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

  .br-bottom {
    border-bottom: 2px solid #8080801c;
  }
</style>
