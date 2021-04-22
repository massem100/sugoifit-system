<template>
  <div v-if="invoice">
    <v-card class="sky">
      <v-card-text>
        <v-row>
          <v-col sm="3" lg="2" cols="12">
            <v-avatar
              class="ma-3"
              size="125"
              tile
            >
              <v-img :src="invoice.img" thumbnail></v-img>
            </v-avatar>
          </v-col>
          <v-col sm="9" lg="10" cols="12">
            <v-row>
              <v-col sm="6" cols="12">
                <div class="info--text text-capitalize text-h5 mb-3">{{invoice.name}}</div>
                <v-row class="mx-0">
                  <div class="info--text pa-1 col subtitle-1">Invoice ID:</div>
                  <div class="col pa-1 subtitle-1">{{invoice.invoice_id}}</div>
                </v-row>
              </v-col>
              <v-col sm="6" cols="12">
                <v-row class="mx-0">
                  <div class="info--text col pa-1 subtitle-1">Balance Due:</div>
                  <div class="col text-h6 pa-1 font-weight-bold">${{invoice.balance}}</div>
                </v-row>
              </v-col>
              <v-col sm="6" cols="12">
                <v-row class="mx-0">
                  <div class="info--text col pa-1 subtitle-1">Billed to:</div>
                  <div class="col pa-1 subtitle-2">{{invoice.billed_to.user}}<br>
                    {{invoice.billed_to.user_mail}}<br>
                    {{invoice.billed_to.user_phone}}
                  </div>
                </v-row>
              </v-col>
              <v-col sm="6" cols="12">
                <v-row class="mx-0">
                  <div class="info--text col pa-1">Date Issued:</div>
                  <div class="col pa-1">{{invoice.issue_Date}}</div>
                </v-row>
                <v-row class="mx-0">
                  <div class="info--text col pa-1">Due Date:</div>
                  <div class="col pa-1">{{invoice.due_date}}</div>
                </v-row>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-card-text>

      <v-btn class="right-arrow"
             color="info"
             icon
             large
             :to="{name:'invoice-slug',params:{slug:invoice.invoice_id}}">
        <v-icon>mdi-chevron-right</v-icon>
      </v-btn>

    </v-card>
  </div>
</template>

<script>
    export default {
        name: "invoice-card",
        props: {
            invoice: {
                type: Object,
                default: () => {
                }
            }
        }
    }
</script>

<style scoped>
  .right-arrow {
    position: absolute;
    right: 10px;
    top: calc(50% - 20px);
  }
</style>
