<template>
  <div v-if="invoice">
    <b-card class="bg-secondary-3">
      <b-row>
        <b-col sm="3">
          <b-img-lazy :src="invoice.img" thumbnail></b-img-lazy>
        </b-col>
        <b-col sm="9">
          <b-row>
            <b-col sm="6">
              <h3 class="text-info text-capitalize my-0">{{invoice.name}}</h3>
              <b-row class="mb-2">
                <h5 class="my-0 text-info col-12 col-md-6">Invoice ID:</h5>
                <h5 class="my-0 col-12 col-md-6">{{invoice.invoice_id}}</h5>
              </b-row>
            </b-col>
            <b-col sm="6" class="mb-2">
              <b-row>
                <h5 class="my-0 text-info col-12 col-md-6">Balance Due:</h5>
                <h4 class="my-0 font-weight-bold col-12 col-md-6">${{invoice.balance}}</h4>
              </b-row>
            </b-col>
            <b-col sm="6" class="mb-2">
              <b-row>
                <h5 class="my-0 text-info col-12 col-md-6">Billed to:</h5>
                <h5 class="my-0 col-12 col-md-6">
                  {{invoice.billed_to.user}}<br>
                  {{invoice.billed_to.user_mail}}<br>
                  {{invoice.billed_to.user_phone}}
                </h5>
              </b-row>

            </b-col>
            <b-col sm="6">
              <b-row class="mb-2">
                <h5 class="my-0 text-info col-12 col-md-6">Date Issued:</h5>
                <h5 class="my-0 col-12 col-md-6">{{invoice.issue_Date}}</h5>
              </b-row>
              <b-row class="mb-2">
                <h5 class="my-0 text-info col-12 col-md-6">Due Date:</h5>
                <h5 class="my-0 col-12 col-md-6">{{invoice.due_date}}</h5>
              </b-row>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
      <b-button class="right-arrow text-info"
                variant="white"
                size="lg"
                :to="{name:'invoice-slug',params:{slug:invoice.invoice_id}}">
        <font-awesome-icon :icon="['fas','chevron-right']" ></font-awesome-icon>
      </b-button>

    </b-card>
  </div>
</template>

<script>
    export default {
        name: "invoice-card",
        props:{
            invoice:{
                type:Object,
                default:()=>{}
            }
        }
    }
</script>

<style scoped>
  .right-arrow{
    position: absolute;
    right:10px;
    top:calc(50% - 20px);
  }
</style>
