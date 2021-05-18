<template>
  <div class="d-flex mx-3">
    <b-container fluid>
      <base-alert v-if= "alert_message" 
                    class = "mt-5 d-flex flex-row justify-content-center" 
                    style="width: 25rem; 
                           height: 3rem; 
                           z-index:1;" 
                    dismissible      
                    type= "primary">{{alert_message}}
      </base-alert>
      <h3 class="m-2">Add Transaction</h3>
      <b-modal ref="confirmModal" 
                 id = "confirmModal" 
                  >
            Are you sure you want to submit this transaction?
            <template 
                    class = "bg-primary" 
                    v-slot:modal-title> 
                    Confirmation Popup
            </template>
            <template  v-slot:modal-footer>
                <b-button @click="modalCancel" id = "modal-cancel" variant = "outline-secondary">Cancel</b-button>
                <b-button @click="modalSubmit" id = "modal-submit" variant="primary">Submit </b-button>
            </template>
              
        </b-modal>
      <transaction-top/>
      <validation-observer
        ref="observer"
        v-slot="{handleSubmit}"
      >
        <b-form id="LTLiabForm" @submit.stop.prevent="handleSubmit(launchConfirm)">
          <b-row>
            <b-col cols="12" class="text-primary mb-3 pl-0" >Add Long Term Liability</b-col>

            <b-col md="6" cols="12" lg="4" class="bg-secondary px-5 py-3">
              <div class="mb-2">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="liability name"
                >
                  <label>Liability name
                    <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                    "name of what the transaction is for eg. company's short-term debts to a specific place "/>
                  </label>
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
                <label>Creditor name
                  <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                    "name of the person who received payment"/>
                </label>
                <b-form-input v-model="form.person_owed">
                </b-form-input>
              </div>
              <div class="mb-2">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="loan rate"
                >
                  <label>Loan Rate
                     <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                    "rate of return for the lender"/>
                  </label>
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
                  <label>Loan Period
                    <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                    "How long until borrower has to pay loan in full"/>
                  </label>
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
                  <label for="amount_borrowed">Amount Recieved
                    <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                    "Value of the loan"/>
                  </label>
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
                  <label>Loan Borrow Date
                    <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                    "Date the loan was created "/>
                  </label>
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
                  <label>Payment Start Date
                    <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                    "Day in which the borrower should start paying the lender"/>
                  </label>
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
                  <label>Increase/Decrease
                    <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                    " indicates whether a business should be able to meet its short-term obligations "/>
                  </label>
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
    import Modal from '../../../components/argon-core/Modal.vue';
    import BaseAlert from '../../../components/argon-core/BaseAlert.vue';

    export default {
        layout: 'DashboardLayout',
        name: "long-term-liability-create",
        components: {
            ValidationProvider,
            ValidationObserver,
            Modal,
            BaseAlert,
        },
        data() {
            return {
                alert_message: '',
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
            modalCancel(){
                this.$refs['confirmModal'].hide();
            },
            modalSubmit() {
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
                        this.$refs['confirmModal'].hide();
                        console.log(jsonResponse);
                        console.log(form_data);
                        self.alert_message = jsonResponse.message;
                    }).catch(err => {
                          console.log(err);
                      });
            },
            async launchConfirm(){
                let self = this;
                const submit = await this.$refs['confirmModal'].show();
              
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
