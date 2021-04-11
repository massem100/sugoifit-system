<template>
  <div class="d-flex mx-3">
  <b-container fluid>
    <h3 class="m-2">Add Transaction</h3>
    <transaction-top/>
    <validation-observer
      ref="observer"
      v-slot="{handleSubmit}"
    >
      <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
        <b-row>
          <b-col cols="12" class="text-info mb-3">Add Purchases</b-col>
          <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
            <validation-provider
              v-slot="{ errors }"
              rules="required"
              name="product name"
            >
              <label for="product_name">Product Name</label>
              <b-form-input v-model="form.product_name"
                            type="text"
                            id="product_name"
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
              name="supplier name"
            >
              <label for="supplier_name">Supplier Name</label>
              <b-form-select v-model="form.supplier_name"
                             :options="supplier_name_options"
                             id="supplier_name"
                             :state="getValidationState(errors)"
              >
              </b-form-select>
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
              name="date"
            >
              <label for="date">Date</label>
              <b-form-datepicker id="date"
                                 v-model="form.date"
                                 :date-format-options="{ year: 'numeric', month: 'short', day: 'numeric' }"
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
              name="amount/cost"
            >
              <label for="amount_cost">Amount/Cost</label>
              <b-form-input v-model="form.amount_cost"
                            type="number"
                            id="amount_cost"
                            :state="getValidationState(errors)">
              </b-form-input>
              <b-form-invalid-feedback>
                {{ errors[0] }}
              </b-form-invalid-feedback>
            </validation-provider>
          </b-col>
          <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <label for="description">Description</label>
              <b-form-textarea v-model="form.description"
                            type="text"
                            id="description"
                            >
              </b-form-textarea>
          </b-col>
          <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
            <validation-provider
              v-slot="{ errors }"
              rules="required"
              name="shipping methods"
            >
              <label for="shipping_methods">Shipping Methods</label>
              <b-form-select v-model="form.shipping_methods"
                             :options="shipping_methods_options"
                             id="shipping_methods"
                             :state="getValidationState(errors)"
              >
              </b-form-select>
              <b-form-invalid-feedback>
                {{ errors[0] }}
              </b-form-invalid-feedback>
            </validation-provider>
          </b-col>
          <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
            <validation-provider
              v-slot="{ errors }"
              rules="required"
              name="discount"
            >
              <label for="discount">Discount</label>
              <b-form-input v-model="form.discount"
                            type="number"
                            id="discount"
                            :state="getValidationState(errors)">
              </b-form-input>
              <b-form-invalid-feedback>
                {{ errors[0] }}
              </b-form-invalid-feedback>
            </validation-provider>
          </b-col>
          <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <label for="notes">Notes</label>
              <b-form-textarea v-model="form.notes"
                            type="text"
                            id="notes"
                            >
              </b-form-textarea>
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
        layout:'dashboard',
        name: "purchase-create",
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                form: {
                    date: new Date().toISOString()
                },
                asset_options: [
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
