<template>
  <div class="d-flex mx-3">
    <b-container fluid>
      <b-card>
        <b-row>
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
                <th class="text-right">$'000</th>
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
                <td class="font-weight-bold">Total Liabilities</td>
                <td class="text-right font-weight-bold">$40</td>
              </tr>
              <tr>
                <td class="font-weight-bold">Total Liabilities & Equity</td>
                <td class="text-right font-weight-bold">$40</td>
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
