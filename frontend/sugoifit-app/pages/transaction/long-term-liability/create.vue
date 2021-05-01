<template>
  <div class="d-flex mx-3">
    <b-container fluid>
      <h3 class="m-2">Add Transaction</h3>
      <transaction-top/>
      <validation-observer
        ref="observer"
        v-slot="{handleSubmit}"
      >
        <b-form id="LTLiabForm" @submit.stop.prevent="handleSubmit(onSubmit)">
          <b-row>
            <b-col cols="12" class="text-primary mb-3 pl-0">Add Long Term Liability</b-col>

            <b-col md="6" cols="12" lg="4" class="bg-secondary px-5 py-3">
              <div class="mb-2">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="liability name"
                >
                  <label>Liability name</label>
                  <b-form-input v-model="form.liab_name"
                                required
                                :state="getValidationState(errors)">
                  </b-form-input>
                  <b-form-invalid-feedback>
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </validation-provider>
              </div>
              <div class="mb-2">
                <label>Creditor name</label>
                <b-form-input v-model="form.person_owed">
                </b-form-input>
              </div>
              <div class="mb-2">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="loan rate"
                >
                  <label>Loan Rate</label>
                  <b-form-input v-model="form.loan_rate"
                                type="number"
                                required
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
                  rules="required"
                  name="Loan Period"
                >
                  <label>Loan Period</label>
                  <b-form-input v-model="form.loan_periods"
                                type="number"
                                required
                                :state="getValidationState(errors)">
                  </b-form-input>
                  <b-form-invalid-feedback>
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </validation-provider>
              </div>
            </b-col>
            <b-col md="6" cols="12" lg="4" class="px-5 py-3">
              <div class="mb-2">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="amount borrowed"
                >
                  <label for="amount_borrowed">Amount Recieved</label>
                  <b-form-input v-model="form.amount_borrowed"
                                type="number"
                                id="amount_borrowed"
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
                  rules="required"
                  name="borrow date"
                >
                  <label>Loan Borrow Date</label>
                  <b-form-datepicker
                    v-model="form.borrow_date"
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
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="Payment Start Date"
                >
                  <label>Payment Start Date</label>
                  <b-form-datepicker
                    v-model="form.payment_start_date"
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
            </b-col>
            <b-col md="6" cols="12" lg="4" class="px-5 py-3">
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
                  <b-form-radio-group v-model="form.account_affected"
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

            <b-col cols="12" class="text-right my-2 px-3">
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
        layout: 'DashboardLayout',
        name: "long-term-liability-create",
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                form: {
                    borrow_date: new Date().toISOString().substr(0, 10),
                    payment_start_date: new Date().toISOString().substr(0, 10),
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
            getValidationState(errors) {
                return errors.length > 0 ? false : null;
            },

            onSubmit() {
                let PATH_API = 'transaction/ltliabform';
                let form_data = new FormData();
                Object.entries(this.form).forEach(entry => {
                    const [key, value] = entry;
                    form_data.append(key, value);
                });
                form_data.append('form_id', 'LTLiabForm');
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
