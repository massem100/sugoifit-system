<template>
  <div class="d-flex mx-3">
    <b-container fluid>
      <h3 class="m-2">Add Transaction</h3>
      <transaction-top/>
      <validation-observer
        ref="observer"
        v-slot="{handleSubmit}"
      >
        <b-form class="" id="AddNCAForm" @submit.stop.prevent="handleSubmit(AddCA)">
          <b-row class="m-1 w-100">
            <b-col cols="12" class="text-primary mb-3 pl-0">Add Revenue</b-col>

            <b-col md="6" cols="12" class="bg-secondary px-5 py-3">
              <div class="mb-2">
                <validation-provider v-slot="{ errors }" rules="required" name="Revenue name">
                  <label>Revenue Name</label>
                  <b-form-input v-model="form.revenue_name" type="text" required
                                :state="getValidationState(errors)">
                  </b-form-input>
                  <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
                </validation-provider>
              </div>
              <div class="mb-2">
                <validation-provider v-slot="{ errors }" rules="required" name="transaction_date">
                  <label for="date">Transaction Date</label>
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
                <b-form-textarea v-model="form.revenue_desc" type="text" id="description"
                                 maxlength="200"></b-form-textarea>
              </div>
            </b-col>
            <b-col md="6" cols="12" class="px-3">
               <div class="mb-2">
                <validation-provider v-slot="{ errors }" rules="required" name="tan_in">
                  <label>Revenue Type</label>
                  <b-form-radio-group v-model="form.revenue_type"
                                      :options="inc_dec"
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
                <validation-provider v-slot="{ errors }" rules="required" name="tan_in">
                  <label>Increase/Decrease</label>
                  <b-form-radio-group v-model="form.increase_decrease"
                                      :options="inc_dec"
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
          <b-row class="text-right my-4 px-3">
            <b-button type="submit" variant="primary">Submit</b-button>
            <b-button type="reset" variant="danger" @click="resetForm()">Reset</b-button>
          </b-row>
        </b-form>
      </validation-observer>
    </b-container>
  </div>
</template>

<script>
    import {ValidationObserver, ValidationProvider} from "vee-validate";

    export default {
        layout: 'DashboardLayout',
        name: "current-asset-create",
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                form: {
                    transaction_date: new Date().toISOString().substr(0, 10)
                },
                inc_dec: [
                    {value: 'Increase', text: 'Increase'},
                    {value: 'Decrease', text: 'Decrease'}
                ],

                paid_using: [
                    {value: 'Cash', text: 'Cash '},
                    {value: 'Cheque', text: 'Cheque '},
                    {value: 'Credit', text: 'Credit '},
                ],
            }
        },
        methods: {
            AddCA() {
                let PATH_API = 'transaction/revenue';
                let form_data = new FormData();
                Object.entries(this.form).forEach(entry => {
                    const [key, value] = entry;
                    form_data.append(key, value);
                });
                form_data.append('form_id', 'ExpForm');
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
