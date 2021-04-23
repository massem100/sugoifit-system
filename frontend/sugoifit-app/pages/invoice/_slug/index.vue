<template>
  <div class="d-flex mx-3">
    <b-container fluid>
      <b-card>
        <b-row>
          <b-col cols="12" class="text-info mb-3 font-weight-bold text-capitalize">Invoice of {{invoice.billed_to.user}}</b-col>
          <b-col cols="12" v-if="invoice">
            <b-row style="border-bottom: 2px solid #00bcd4" class="mx-0 pb-3">
              <b-col sm="2">
                <b-img-lazy :src="invoice.img" thumbnail></b-img-lazy>
              </b-col>
              <b-col sm="10">
                <b-row>
                  <b-col sm="6">
                    <h3 class="text-info text-capitalize my-0">{{invoice.name}}</h3>
                    <div class="mb-2">
                      <h5 class="my-0 text-info">Invoice ID:<span class="ml-3 text-dark">{{invoice.invoice_id}}</span>
                      </h5>
                    </div>
                    <div class="mb-2">
                      <h5 class="my-0 text-info">Address:<span class="ml-3 text-dark">{{invoice.address}}</span></h5>
                    </div>
                  </b-col>
                  <b-col sm="6" class="mb-2">
                    <b-row>
                      <h5 class="my-0 text-info col-12 col-md-6">Balance Due:</h5>
                      <h4 class="my-0 font-weight-bold col-12 col-md-6">${{invoice.balance}}</h4>
                      <h5 class="my-0 text-info col-12 col-md-6">Date Issued:</h5>
                      <h5 class="my-0 col-12 col-md-6">{{invoice.issue_Date}}</h5>
                      <h5 class="my-0 text-info col-12 col-md-6">Due Date:</h5>
                      <h5 class="my-0 col-12 col-md-6">{{invoice.due_date}}</h5>
                      <h5 class="my-0 text-info col-12 col-md-6">Billed to:</h5>
                      <h5 class="my-0 col-12 col-md-6">
                        {{invoice.billed_to.user}}<br>
                        {{invoice.billed_to.user_mail}}<br>
                        {{invoice.billed_to.user_phone}}
                      </h5>
                    </b-row>
                  </b-col>
                </b-row>
              </b-col>
            </b-row>
          </b-col>
          <b-col cols="12" class="my-4 table-responsive">
            <table class="w-100 custom-table">
              <thead>
              <tr class="text-info">
                <th>Description</th>
                <th class="text-center">Unity Price</th>
                <th class="text-center">Quantity</th>
                <th class="text-center">Amount</th>
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
                <td class="text-right text-info" colspan="3" style="padding-top: 80px">Subtotal</td>
                <td class="text-center" style="padding-top: 80px">${{subtotal}}</td>
              </tr>
              <tr class="br-bottom">
                <td class="text-right text-info" colspan="3">Tax</td>
                <td class="text-center">${{tax.toFixed(2)}}</td>
              </tr>
              <tr>
                <td class="text-right font-weight-bold text-info" colspan="3">Total</td>
                <td class="text-center font-weight-bold">${{total}}</td>
              </tr>
              </tbody>
            </table>
          </b-col>
        </b-row>
      </b-card>

    </b-container>
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
