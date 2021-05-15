<template>
  <div class="d-flex ">
    <b-container fluid>

       <base-alert v-if= "alert_message" 
                    class = "mt-5 d-flex flex-row justify-content-center" 
                    style="width: 25rem; 
                           height: 3rem; 
                           z-index:1;" 
                    dismissible      
                    type= "primary">{{alert_message}}
      </base-alert>
      <b-row>
        <back-button class="mt-4 "></back-button>
        <b-col>
           <h3 class="mt-4 ml-0">Manage transactions</h3>
            <p class = "mb-2 mt-2 "> 
                Transactions are used to automatically generate your financials. 
                Keep track of your daily transactions.
              </p>
        </b-col>
      </b-row>
     
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
      <transaction-top class="d-flex- justify-content-center"/>
      <validation-observer
        ref="observer"
        v-slot="{handleSubmit}"
      >
        <b-form class="" id="AddNCAForm" @submit.stop.prevent="handleSubmit(launchConfirm)">
          <b-row class="m-1 w-100">
            <b-col cols="12" class="text-primary mb-3 pl-0">Add Current Asset</b-col>

            <b-col md="6" cols="12" class="px-5 py-3">
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
                <b-form-textarea v-model="form.asset_desc" type="text" id="description"
                                 maxlength="200"></b-form-textarea>
              </div>
            </b-col>
            <b-col md="6" cols="12" class="px-3">
              <div class = "mb-2">
                 <validation-provider
                      v-slot="{ errors }"
                      rules="required"
                      name="tag"
                    >
                      <label for="tag">Select a Tag</label>
                      <b-form-select v-model="form.tag"
                                    :options="asset_tags"
                                    id="tag"
                                    name="tag"
                                    class="text-black"
                                    :state="getValidationState(errors)"
                      >
                      </b-form-select>
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
                                      class="px-4 py-3"
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
                                      class="py-3 px-4"
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
          <b-row  class="text-right my-4 px-3">
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
    import Modal from '../../../components/argon-core/Modal.vue';
    import BaseAlert from '../../../components/argon-core/BaseAlert.vue';
    import BackButton from '../../../components/argon-core/BackButton.vue';

    export default {
        layout: 'DashboardLayout',
        name: "current-asset-create",
        components: {
            ValidationProvider,
            ValidationObserver,
            Modal,
            BaseAlert,
            BackButton
        },
        data() {
            return {
                alert_message:'',
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
                asset_tags:[ 
                    {value: null, text: 'Please select an option'},
                    {value: 'Inventory', text: 'Inventory'},
                    {value: 'Cash', text: 'Cash'},
                    {value: 'Cash Equivalents', text: 'Cash Equivalents'},
                    {value: 'Accounts Receivables', text: 'Accounts Receivables'},
                    {value: 'Prepaid Expenses', text: 'Prepaid Expenses'},
                    {value: 'Marketable Securities', text: 'Marketable Securities'},
                    {value: 'Other Current Assets', text: 'Other Current Assets'},

                    
                ]
            }
        },
        methods: {
            modalCancel(){
                this.$refs['confirmModal'].hide();
            },
            modalSubmit() {
                let PATH_API = 'transaction/currentasset';
                let form_data = new FormData();
                Object.entries(this.form).forEach(entry => {
                    const [key, value] = entry;
                    form_data.append(key, value);
                });
                form_data.append('form_id', 'AddCAForm');
                this.$axios.post(`/api/${PATH_API}`, form_data, {
                    headers: {
                        'contentType': 'application/json',
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
