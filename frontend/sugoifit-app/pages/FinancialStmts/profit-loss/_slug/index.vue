<template>
  <div class="d-flex mx-3">
    <b-container fluid>
      <b-card>
        <b-row>
          <back-button class="mt-4 ml-2"></back-button>
          <b-col cols="12" class="text-left">
            <h4 class="font-weight-bold text-capitalize my-0">Marqui bottique</h4>
            <h3 class="text-info font-weight-bold text-capitalize my-0">Balance Sheet</h3>
            <h5 class="my-0">Date: March 25,2323</h5>
            <h5 class="my-0">Currency: JMD</h5>
          </b-col>

          <b-col cols="12" class="my-4 table-responsive">
            <table class="w-100 custom-table">
              <thead>
              <tr style="border-bottom: 4px solid #7cc3cd">
                <th></th>
                <th v-for="(mon,index) in field" :key="index" class="text-capitalize">
                  {{mon}}
                </th>
              </tr>
              </thead>
              <tbody>
              <tr class="br-bottom">
                <td :colspan="field.length+1" class="font-weight-bold">Income</td>
              </tr>
              <tr class="br-bottom">
                <td class="pl-4">Sales</td>
                <td v-for="(mon,index) in field" :key="index">
                  ${{sales[mon]}}
                </td>
              </tr>
              <tr class="br-bottom">
                <td class="pl-4">Cost of Goods Sold</td>
                <td v-for="(mon,index) in field" :key="index">
                  ${{cost_sold[mon]}}
                </td>
              </tr>
              <tr>
                <td class="font-weight-bold">Gross Profit</td>
                <td v-for="(mon,index) in field" :key="index" class="font-weight-bold">
                  ${{sales[mon]+cost_sold[mon]}}
                </td>
              </tr>
              <tr class="br-bottom font-weight-bold">
                <td>Other Operating Income</td>
                <td v-for="(mon,index) in field" :key="index">
                  ${{operate_income[mon]}}
                </td>
              </tr>
              <tr class="br-bottom font-weight-bold">
                <td>Less Expenses</td>
                <td v-for="(mon,index) in field" :key="index">
                  ${{sales[mon]}}
                </td>
              </tr>
              <tr class="br-bottom">
                <td class="pl-4">Expenses</td>
                <td v-for="(mon,index) in field" :key="index">
                  ${{cost_sold[mon]}}
                </td>
              </tr>
              <tr class="br-bottom">
                <td class="font-weight-bold">Total Expense</td>
                <td v-for="(mon,index) in field" :key="index" class="font-weight-bold">
                  ${{sales[mon]+cost_sold[mon]}}
                </td>
              </tr>
              <tr>
                <td class="font-weight-bold">Net Profit</td>
                <td v-for="(mon,index) in field" :key="index" class="font-weight-bold">
                  ${{sales[mon]+cost_sold[mon]}}
                </td>
              </tr>
              </tbody>
            </table>
            <hr>
            <hr>
          </b-col>
        </b-row>
      </b-card>

    </b-container>
  </div>
</template>

<script>
import BackButton from '../../../../components/argon-core/BackButton.vue';
    export default {
        components: { BackButton },
        name: "invoice-card",
        layout: 'dashboard',
        head(){
          return{
              title: 'Profit-Loss'
          }
        },
        data() {
            return {
                field: ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'
                ],
                sales: {
                    jan: 20,
                    feb: 20,
                    mar: 40,
                    apr: 20,
                    may: 20,
                    jun: 70,
                    jul: 20,
                    aug: 30,
                    sep: 20,
                    oct: 80,
                    nov: 120,
                    dec: 520
                },
                cost_sold: {
                    jan: 20,
                    feb: 320,
                    mar: 20,
                    apr: 220,
                    may: 320,
                    jun: 20,
                    jul: 20,
                    aug: 220,
                    sep: 420,
                    oct: 20,
                    nov: 20,
                    dec: 20
                },
                operate_income: {
                    jan: 20,
                    feb: 320,
                    mar: 20,
                    apr: 220,
                    may: 320,
                    jun: 20,
                    jul: 20,
                    aug: 220,
                    sep: 420,
                    oct: 20,
                    nov: 20,
                    dec: 20
                },
            }
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
    border-top: 1px solid #d8d9d9;
  }

  .br-bottom {
    border-bottom: 1px solid #d8d9d9;
  }
</style>
