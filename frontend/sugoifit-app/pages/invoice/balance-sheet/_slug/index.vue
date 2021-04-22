<template>
<v-container fluid>
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
                <th class="text-right">$000</th>
              </tr>
              </thead>
              <tbody>
              <tr class="br-bottom">
                <td colspan="2" class="font-weight-bold">Assets</td>
              </tr>
              <tr class="br-bottom">
                <td class="pl-4">Non Current Assets</td>
                <td class="text-right">$20</td>
              </tr>
              <tr class="br-bottom">
                <td class="pl-4">Non Current Assets</td>
                <td class="text-right">$20</td>
              </tr>
              <tr>
                <td class="font-weight-bold">Total Assets</td>
                <td class="text-right font-weight-bold">$40</td>
              </tr>
              <tr class="br-bottom">
                <td class="font-weight-bold">Equity</td>
                <td class="text-right font-weight-bold">$40</td>
              </tr>
              <tr class="br-bottom">
                <td colspan="2" class="font-weight-bold">Liabilities</td>
              </tr>
              <tr class="br-bottom">
                <td class="pl-4">Long Term liabilities</td>
                <td class="text-right">$20</td>
              </tr>
              <tr class="br-bottom">
                <td class="pl-4">Current liabilities</td>
                <td class="text-right">$20</td>
              </tr>
              <tr>
                <td class="font-weight-bold">Total Shareholders & Equity</td>
                <td class="text-right font-weight-bold">$40</td>
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
