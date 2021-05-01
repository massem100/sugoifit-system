<template>
  <div class="d-flex ">
    <b-container fluid>
      <h3 class="mt-3 ml-0">Add Transaction</h3>
      <transaction-top class="w-100"/>
      <validation-observer
        ref="observer"
        v-slot="{handleSubmit}"
      >
        <b-form class="" id="AddNCAForm" @submit.stop.prevent="handleSubmit(AddNCA)">
          <b-row class="m-1 w-100">
            <b-col cols="12" class="text-primary mb-3 pl-0">Add Non Current Asset</b-col>

            <b-col md="6" cols="12" lg="4" class="bg-secondary px-5 py-3">
              <div class="mb-2">
                <validation-provider v-slot="{ errors }" rules="required" name="asset name">
                  <label for="asset_name">Asset Name</label>
                  <b-form-input v-model="form.asset_name" type="text" id="asset_name" required
                                :state="getValidationState(errors)">
                  </b-form-input>
                  <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
                </validation-provider>
              </div>
              <div class="mb-2">
                <validation-provider v-slot="{ errors }" rules="required" name="transaction_date">
                  <label for="date">Date</label>
                  <b-form-datepicker id="transaction_date"
                                     v-model="form.transaction_date"
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
              </div>
              <div class="mb-2">
                <validation-provider v-slot="{ errors }" rules="required" name="amount">

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
              </div>
              <div class="mb-2"><label for="description">Description</label>
                <b-form-textarea v-model="form.asset_desc" type="text" id="description"
                                 maxlength="200"></b-form-textarea>
              </div>
            </b-col>
            <b-col md="6" cols="12" lg="4" class="px-5">
              <div class="mb-2 text-primary">{{reduct_hide?'Amortization':'Depreciation'}}</div>
              <div class="mb-2">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="dep type"
                >
                  <label for="dep_type">Depreciation Type</label>
                  <b-form-select v-model="form.dep_type"
                                 :options="asset_options"
                                 id="dep_type"
                                 :state="getValidationState(errors)"
                  >
                  </b-form-select>
                  <b-form-invalid-feedback>
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </validation-provider>
              </div>
              <div class="mb-2">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="depreciation rate"
                >
                  <label for="depreciation">Depreciation Rate</label>
                  <b-form-input v-model="form.depreciation_rate"
                                type="number"
                                id="depreciation_rate"
                                :state="getValidationState(errors)">
                  </b-form-input>
                  <b-form-invalid-feedback>
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </validation-provider>
              </div>
              <div class="mb-2">
                <validation-provider
                  v-slot="{ errors }"

                  name="asset lifespan"
                >
                  <label for="asset_lifespan">Asset Lifespan</label>
                  <b-form-input v-model="form.asset_lifespan"
                                type="text"
                                id="asset_lifespan"
                                :state="getValidationState(errors)">
                  </b-form-input>
                  <b-form-invalid-feedback>
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </validation-provider>
              </div>
            </b-col>
            <b-col md="6" cols="12" lg="4" class="px-3">
              <div class="mb-2">
                <validation-provider v-slot="{ errors }" rules="required" name="tan_in">
                  <label for="tan_in">Type of Asset</label>
                  <b-form-radio-group v-model="form.tan_in"
                                      :options="tangible_intan"
                                      id="tan_in"
                                      class="border border-radius px-4 py-3"
                                      style="Background: #E5E5E5; "
                                      stacked
                                      :state="getValidationState(errors)"
                  >
                  </b-form-radio-group>
                  <b-form-invalid-feedback>
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </validation-provider>
              </div>
              <div class="mb-2">
                <validation-provider v-slot="{ errors }" rules="required" name="bought_sold">
                  <label for="bought_sold"> Bought or Sold?</label>
                  <b-form-radio-group v-model="form.bought_sold"
                                      :options="bought_sold"
                                      id="bought_sold"
                                      stacked
                                      class="border border-radius py-3 px-4"
                                      style="Background: #E5E5E5; "
                                      :state="getValidationState(errors)"
                  >
                  </b-form-radio-group>
                  <b-form-invalid-feedback>
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </validation-provider>
              </div>
              <div class="mb-2">
                <validation-provider v-slot="{ errors }" rules="required" name="paid_using">
                  <label for="paid_using"> Paid Using</label>
                  <b-form-radio-group v-model="form.paid_using"
                                      :options="paid_using"
                                      id="paid_using"
                                      stacked
                                      class="border border-radius py-3 px-4"
                                      style="Background: #E5E5E5; "
                                      :state="getValidationState(errors)"
                  >
                  </b-form-radio-group>


                  <b-form-invalid-feedback>
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </validation-provider>
              </div>
            </b-col>
          </b-row>
          <!-- Submit and Reset -->
          <b-row cols="12" class="text-right my-4 px-3">
            <b-button type="submit" variant="primary">Submit</b-button>
            <b-button type="reset" variant="danger" @click="resetForm()">Reset</b-button>
          </b-row>
        </b-form>
      </validation-observer>
    </b-container>
  </div>
</template>

<script>
    // import axios from '@nuxtjs/axios';
    import {ValidationObserver, ValidationProvider} from "vee-validate";

    export default {
        name: "non-current-asset-create",
        layout: "DashboardLayout",
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                reduct_hide: false,
                form: {
                    date: new Date().toISOString().substr(0,10)
                },
                asset_options: [
                    {value: null, text: 'Please select an option'},
                    {value: 'Straight-Line Method', text: 'Straight-Line'},
                    {value: 'Declining Balance', text: 'Declining Balance '},
                    {value: 'Units of Production', text: 'Units of Production'},
                    {value: 'Sum of Year\'s Digits', text: 'Sum of Year\'s Digits'},
                ],
                tangible_intan: [
                    {value: 'Tangible Asset', text: 'Tangible Asset'},
                    {value: 'Intangible Asset', text: ' Intangible Asset'}
                ],

                paid_using: [
                    {value: 'Cash', text: 'Cash '},
                    {value: 'Cheque', text: 'Cheque '},
                    {value: 'Credit', text: 'Credit '},
                ],

                bought_sold: [
                    {value: 'Bought', text: 'Bought Asset'},
                    {value: 'Sold', text: ' Sold Asset'}
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

            },
            AddNCA: function () {
                let PATH_API = 'transaction/noncurrentasset';
                let form_data = new FormData();
                Object.entries(this.form).forEach(entry => {
                    const [key, value] = entry;
                    form_data.append(key, value);
                });
                form_data.append('form_id', 'AddNCAForm');
                this.$axios.post(`/api/${PATH_API}`, form_data, {
                    headers: {
                        'contentType': 'application/json',
                        "Authorization": "Bearer " + localStorage.getItem("token"),
                    }
                })
                    .then(jsonResponse => {
                        return jsonResponse.json();
                    })
                    .then(jsonResponse => {
                        console.log(jsonResponse);
                    })
            },

        }
    }
</script>

<style scoped>

</style>
