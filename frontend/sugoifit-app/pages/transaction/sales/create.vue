<template>
  <div class="d-flex">
    <side-bar></side-bar>
    <b-container fluid>
      <top-bar/>
      <h3 class="m-2">Add Transaction</h3>
      <transaction-top/>
      <validation-observer
        ref="observer"
        v-slot="{handleSubmit}"
      >
        <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
          <b-row>
            <b-col cols="12" class="text-info mb-3">Add Sales</b-col>
            <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <validation-provider
                v-slot="{ errors }"
                rules="required"
                name="product/item name"
              >
                <label for="product_item_name">Product/Item Name</label>
                <b-form-input v-model="form.product_item_name"
                              type="text"
                              id="product_item_name"
                              :state="getValidationState(errors)">
                </b-form-input>
                <b-form-invalid-feedback>
                  {{ errors[0] }}
                </b-form-invalid-feedback>
              </validation-provider>
            </b-col>
            <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <validation-provider
                v-slot="{ errors }"
                rules="required"
                name="reference number"
              >
                <label for="ref_no">Reference Number</label>
                <b-form-input v-model="form.ref_no"
                              type="text"
                              id="ref_no"
                              :state="getValidationState(errors)">
                </b-form-input>
                <b-form-invalid-feedback>
                  {{ errors[0] }}
                </b-form-invalid-feedback>
              </validation-provider>
            </b-col>
            <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <validation-provider
                v-slot="{ errors }"
                rules="required"
                name="quantity"
              >
                <label for="quantity">Quantity</label>
                <b-form-input v-model="form.quantity"
                              type="number"
                              id="quantity"
                              :state="getValidationState(errors)">
                </b-form-input>
                <b-form-invalid-feedback>
                  {{ errors[0] }}
                </b-form-invalid-feedback>
              </validation-provider>
            </b-col>
            <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <validation-provider
                v-slot="{ errors }"
                rules="required"
                name="amount"
              >
                <label for="amount">Amount</label>
                <b-form-input v-model="form.amount"
                              type="number"
                              id="amount"
                              :state="getValidationState(errors)">
                </b-form-input>
                <b-form-invalid-feedback>
                  {{ errors[0] }}
                </b-form-invalid-feedback>
              </validation-provider>
            </b-col>
            <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <validation-provider
                v-slot="{ errors }"
                rules="required"
                name="transaction date"
              >
                <label for="transaction_date">Transaction Date</label>
                <b-form-datepicker id="date"
                                   v-model="form.transaction_date"
                                   :transaction_date-format-options="{ year: 'numeric', month: 'short', day: 'numeric' }"
                                   locale="en-US"
                                   required
                                   calendar-width="180px"
                                   :state="getValidationState(errors)"
                >
                </b-form-datepicker>
                <b-form-invalid-feedback>
                  {{ errors[0] }}
                </b-form-invalid-feedback>
              </validation-provider>
            </b-col>
            <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <validation-provider
                v-slot="{ errors }"
                rules="required"
                name="transaction time"
              >
                <label for="transaction_time">Transaction Time</label>
                <b-form-timepicker v-model="form.transaction_time"
                                   id="transaction_time"
                                   required
                                   :state="getValidationState(errors)">
                </b-form-timepicker>
                <b-form-invalid-feedback>
                  {{ errors[0] }}
                </b-form-invalid-feedback>
              </validation-provider>
            </b-col>
            <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <validation-provider
                v-slot="{ errors }"
                rules="required"
                name="customer name"
              >
                <label for="customer_name">Customer Name</label>
                <b-form-select v-model="form.customer_name"
                               :options="customer_name_options"
                               id="customer_name"
                               :state="getValidationState(errors)"
                >
                </b-form-select>
                <b-form-invalid-feedback>
                  {{ errors[0] }}
                </b-form-invalid-feedback>
              </validation-provider>
            </b-col>
            <b-col cols="12" class="text-right my-2">
              <b-button type="submit" variant="primary">Submit</b-button>
              <b-button type="reset" variant="danger" @click="resetForm()">Reset</b-button>
            </b-col>
          </b-row>
        </b-form>
      </validation-observer>
    </b-container>
  </div>
</template>

<script>
    import {ValidationObserver, ValidationProvider} from "vee-validate";

    export default {
        name: "sales-create",
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                form: {
                    date: new Date().toISOString()
                },
                customer_name_options: [
                    {value: null, text: 'Please select an option'},
                    {value: 'a', text: 'This is First option'},
                    {value: 'b', text: 'Selected Option'},
                ]
            }
        },
        methods: {
            getValidationState(errors) {
                return errors.length > 0 ? false : null;
            },

            onSubmit() {
                alert(JSON.stringify(this.form))
            },
            resetForm() {
                this.form = {};
                this.$nextTick(() => {
                    this.$refs.observer.reset();
                });

            }
        }
    }
</script>

<style scoped>

</style>
