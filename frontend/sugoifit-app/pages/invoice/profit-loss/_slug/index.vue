<template>
    <v-container>
      <v-card>
        <v-card-text>
          <v-row>
          <v-col cols="12" class="text-left">
            <h3 class="font-weight-bold text-capitalize my-0">Marqui bottique</h3>
            <h2 class="info--text font-weight-bold text-capitalize my-0">Balance Sheet</h2>
            <h4 class="my-0">Date: March 25,2323</h4>
            <h4 class="my-0">Currency: JMD</h4>
          </v-col>

          <v-col cols="12" class="my-4 table-responsive">
            <v-simple-table class="custom-table">
              <thead>
              <tr style="border-bottom: 4px solid #7cc3cd">
                <th></th>
                <th v-for="mon in field" class="text-capitalize">
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
                <td v-for="mon in field">
                  ${{sales[mon]}}
                </td>
              </tr>
              <tr class="br-bottom">
                <td class="pl-4">Cost of Goods Sold</td>
                <td v-for="mon in field">
                  ${{cost_sold[mon]}}
                </td>
              </tr>
              <tr>
                <td class="font-weight-bold">Gross Profit</td>
                <td v-for="mon in field" class="font-weight-bold">
                  ${{sales[mon]+cost_sold[mon]}}
                </td>
              </tr>
              <tr class="br-bottom font-weight-bold">
                <td>Other Operating Income</td>
                <td v-for="mon in field">
                  ${{operate_income[mon]}}
                </td>
              </tr>
              <tr class="br-bottom font-weight-bold">
                <td>Less Expenses</td>
                <td v-for="mon in field">
                  ${{sales[mon]}}
                </td>
              </tr>
              <tr class="br-bottom">
                <td class="pl-4">Expenses</td>
                <td v-for="mon in field">
                  ${{cost_sold[mon]}}
                </td>
              </tr>
              <tr class="br-bottom">
                <td class="font-weight-bold">Total Expense</td>
                <td v-for="mon in field" class="font-weight-bold">
                  ${{sales[mon]+cost_sold[mon]}}
                </td>
              </tr>
              <tr>
                <td class="font-weight-bold">Net Profit</td>
                <td v-for="mon in field" class="font-weight-bold">
                  ${{sales[mon]+cost_sold[mon]}}
                </td>
              </tr>
              </tbody>
            </v-simple-table>
            <hr>
            <hr>
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
