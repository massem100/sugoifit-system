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
                <th class="text-right">$'000</th>
              </tr>
              </thead>
              <tbody>
              <tr class="br-bottom">
                <td colspan="2" class="font-weight-bold">Assets</td>
              </tr>
               <tr  class="br-bottom">
                <td class="pl-4">Non Current Assets</td>
                <td class="text-right"></td>
              </tr>
              <tr v-for= "(bal,line_item) in non_current_assets" :key="line_item"  class="br-bottom">
                <td class="pl-5">{{line_item}}</td>
                <td class="text-right">{{bal}}</td>
              </tr>
               <tr  class="br-bottom">
                <td class="pl-4">Total Non Current Assets</td>
                <td class="text-right">{{total.nca_total}}</td>
              </tr>
              <tr  class="br-bottom">
                <td class="pl-4">Current Assets</td>
                <td class="text-right">$20</td>
              </tr>
              <tr v-for= "asset in current_assets" :key="asset[1]" class="br-bottom">
                <td class="pl-5">{{asset[0]}}</td>
                <td class="text-right">{{asset[1]}}</td>
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
              <tr v-for= "liab_item in liab" :key="liab_item[0]" class="br-bottom">
                <td class="pl-5">{{liab_item[0]}}</td>
                <td class="text-right">{{liab_item[1]}}</td>
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
import BackButton from '../../../../components/argon-core/BackButton.vue';
    export default {
        name: "invoice-card",
        layout: 'DashboardLayout',
        components: { BackButton },
        head(){
          return{
              title: 'Balance Sheet'
          }
        },
        data(){
          return{
            line_items: [],
            current_assets: [],
            non_current_assets: [], 
            current_liabilities: [], 
            long_term_liabilities: [], 
            capital: [], 
            total: {
              nca_total: null,
              ca_total: null,
              cl_total: null,
              lt_total: null,
            }, 
            liab: []

          }
        },
        mounted(){
          let self=this;
          const busID = localStorage.getItem('busID');
          const year =2021
          this.$axios.get(`/api/financialstmt/balancesheet/${busID}/${year}`
              ).then(res =>{
                  return res.data;
              }).then(res =>{
                  if (res){
                      self.line_items = res;
                      self.current_assets= res["Current Asset"]; 
                      self.non_current_assets= res["Non Current Asset"]; 
                      self.current_liabilities.push(res["Current Liabilities"]); 
                      self.long_term_liabilities= res["Long Term Liability"]; 
                      let ap = new Number(self.current_liabilities["Accounts Payable"]);
                      self.liab.push(["Accounts Payable",ap] );
                      self.liab.push(["Current Portion of Long Term Loans", self.current_liabilities["Current Portion of Long Term Loans"]]);
                      self.liab.push(["Other Current Liabilities", self.current_liabilities["Other Current Liabilities"]]);
                      self.liab.push(["Short Term Loans", self.current_liabilities["Short Term Loans"]]);
                      self.liab.push(["Accrued Expenses", self.current_liabilities["Accrued Expenses"]]);
                      self.liab.push(["Tax Payable", self.current_liabilities["Tax Payable"]]);
                      self.liab.push(["Unearned Revenue", self.current_liabilities["Unearned Revenue"]]);
                      // self.capital= res["Capital"]; 
                      // self.total.nca_total = new Intl.NumberFormat('en-IN', { maximumSignificantDigits: 10
                      //                        }).format(this.non_current_assets["Total Non Current Assets"]);


                      // console.log(res["Current Liabilities"]);
              
              }else{
                  console.log('Data not found')
              }
              });

          },
        methods:{
         
        }
    };
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
