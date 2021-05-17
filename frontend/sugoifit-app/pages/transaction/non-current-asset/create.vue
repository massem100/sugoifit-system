<template>
  <div class="d-flex">
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
          
          <b-col>
            <h3  class="mt-3 ml-0"> Manage Transactions </h3>
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

        <transaction-top class = "d-flex justify-content-center w-100"/>
        <validation-observer
        ref="observer"
        v-slot="{handleSubmit}"
        >
      
      <b-form class ="" id= "AddNCAForm"   @submit.stop.prevent="handleSubmit(launchConfirm)">
          <b-row cols = "12" class = "m-1 S "> 
            <b-col  class = "m-1">
              
              <!-- Add Non Current Asset heading -->
              <b-col cols="12" class="text-primary mb-3 pl-0" xl="8" md="8" v-b-tooltip.hover title="Non-current Assets are......">Add Non Current Asset</b-col>
              <!-- Major Form Fields -->
              <b-col cols = "12" class = "ml-1 mt-4   ">
              <!-- Asset Name -->
                <b-col cols = "8" class="mb-2   pl-0" xl="9" md="6" sm="12">
                  <validation-provider v-slot="{ errors }" rules="required" name="asset name" >
                    <label for="asset_name">Asset Name
                       <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                       "name of what the transaction is for eg.commercial paper, Treasury bills "/>
                    </label>
                    <b-form-input v-model="form.asset_name" type="text" id="asset_name" name="asset_name"
                                  :state="getValidationState(errors)">
                    </b-form-input>
                    <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
                  </validation-provider>
                </b-col>

                <!-- Transaction Date -->
                <b-col class="mb-2 pl-0" xl="9" md="6" sm="12">
                  <validation-provider v-slot="{ errors }" rules="required" name="transaction_date">
                    <label for="date"> Transaction Date
                      <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="Date transaction was made "/>
                    </label>
                    <b-form-datepicker id="transaction_date"
                                      name ="transaction_date"
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
              

                <!-- Amount Input -->
                <b-col  class="mb-2 pl-0" xl="9" md="6" sm="12">
                  <validation-provider v-slot="{ errors }" rules="required" name="amount">
                  
                    <label for="amount">Amount
                      <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="Cost of the transaction "/>
                    </label>
                    <b-form-input v-model="form.amount" type="number" id="amount" name="amount"
                                  :state="getValidationState(errors)">
                    </b-form-input>
                    <b-form-invalid-feedback>
                      {{ errors[0] }}
                    </b-form-invalid-feedback>
                  </validation-provider>
                </b-col>
                <!-- Amortization Selected -->
              
                  <!-- Description Input -->
                <b-col class="mb-2 pl-0" xl="9" md="6" sm="12">
                    <label for="description">Description
                      <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                    " eg. for intellectual propert: Utility patents, design patents etc."/>
                    </label>
                    <b-form-textarea v-model="form.description" type="text" id="description"></b-form-textarea>
                </b-col>
              
                
              </b-col>

              
            
            </b-col>
             <b-col>
                <div v-if= "reduct_hide">
                  <b-col cols="8" class="text-info mb-3 pl-0">Amortization
                    <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                    " cost of those intangible assets that have a specific useful life
                     eg. Broadcast licenses. Copyrights"/>
                    cost of those intangible assets that have a specific useful life
                  </b-col>
                  <b-col class = "m-2">
                    
                  <!-- Depreciation Type Input  -->
                  <b-col cols = "6" class="mb-2 c-box pl-0" xl="4" md="8" sm="12">
                    <validation-provider
                      v-slot="{ errors }"
                      rules="required"
                      name="dep type"
                    >
                      <label for="dep_type">Depreciation Type</label>
                      <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                      "Depreciation: refers to the decline in the value of fixed assets due to their usage, passage of time or obsolescence"/>
                      <b-form-select v-model="form.asset_type"
                                    :options="asset_options"
                                    id="dep_type"
                                    name="dep_type"
                                    :state="getValidationState(errors)"
                      >
                      </b-form-select>
                      <b-form-invalid-feedback>
                        {{ errors[0] }}
                      </b-form-invalid-feedback>
                    </validation-provider>
                  </b-col>
                  <!-- Depreciation  Rate -->
                  <b-col class="mb-2 mr-3 c-box pl-0" xl="7" md="6" sm="12">
                    <validation-provider
                      v-slot="{ errors }"
                      rules="required"
                      name="depreciation rate"
                    >
                      <label for="depreciation">Depreciation Rate</label>
                      <b-form-input v-model="form.depreciation"
                                    type="number"
                                    id="depreciation_rate"
                                    name="depreciation_rate"
                                    :state="getValidationState(errors)">
                      </b-form-input>
                      <b-form-invalid-feedback>
                        {{ errors[0] }}
                      </b-form-invalid-feedback>
                    </validation-provider>
                  </b-col>

                  <!-- Asset LifeSpan -->
                  <b-col class="mb-2 c-box pl-0" xl="7" md="6" sm="12">
                    <validation-provider
                      v-slot="{ errors }"
                      
                      name="asset lifespan"
                    >
                      <label for="expected_lifespan">Asset Lifespan</label>
                      <b-form-input v-model="form.asset_lifespan"
                                    type="text"
                                    id="asset_lifespan"
                                    name="asset_lifespan"
                                    :state="getValidationState(errors)">
                      </b-form-input>
                      <b-form-invalid-feedback>
                        {{ errors[0] }}
                      </b-form-invalid-feedback>
                    </validation-provider>
                  </b-col>
                    </b-col>
                </div>
                <div v-else>
                  <b-col cols="8" class="text-primar mb-3 pl-0">Depreciation</b-col>
                  <!-- Depreciation Selected -->
                  <b-row class = "ml-2">
                  <!-- Depreciation Type Input  -->
                  
                  <b-col class="mb-2 c-box pl-0" xl="7" md="6" sm="12">
                    <validation-provider
                      v-slot="{ errors }"
                      rules="required"
                      name="dep type"
                    >
                      <label for="dep_type">Depreciation Type</label>
                      <b-form-select v-model="form.asset_type"
                                    :options="asset_options"
                                    id="dep_type"
                                    name="dep_type"
                                    :state="getValidationState(errors)"
                      >
                      </b-form-select>
                      <b-form-invalid-feedback>
                        {{ errors[0] }}
                      </b-form-invalid-feedback>
                    </validation-provider>
                  </b-col>
                  <!-- Depreciation  Rate -->
                  <b-col class="mb-2 mr-3 c-box pl-0" xl="7" md="6" sm="12">
                    <validation-provider
                      v-slot="{ errors }"
                      rules="required"
                      name="depreciation rate"
                    >
                      <label for="depreciation">Depreciation Rate</label>
                      <b-form-input v-model="form.depreciation"
                                    type="number"
                                    id="depreciation_rate"
                                    name="depreciation_rate"
                                    :state="getValidationState(errors)">
                      </b-form-input>
                      <b-form-invalid-feedback>
                        {{ errors[0] }}
                      </b-form-invalid-feedback>
                    </validation-provider>
                  </b-col>

                  <!-- Asset LifeSpan -->
                  <b-col class="mb-2 c-box pl-0" xl="7" md="6" sm="12">
                    <validation-provider
                      v-slot="{ errors }"
                      
                      name="asset lifespan"
                    >
                      <label for="expected_lifespan">Asset Lifespan</label>
                      <b-form-input v-model="form.asset_lifespan"
                                    type="text"
                                    id="asset_lifespan"
                                    name="asset_lifespan"
                                    :state="getValidationState(errors)">
                      </b-form-input>
                      <b-form-invalid-feedback>
                        {{ errors[0] }}
                      </b-form-invalid-feedback>
                    </validation-provider>
                  </b-col>
                    </b-row>
                  </div>
              </b-col>
            <b-col class = "ml-auto m-2">
                <!-- Intangible/Tangible Asset Radio Input  -->
                  <b-col cols= "8" class="mt-5 mb-2 ml-2 c-box pl-0 " xl="7" md="6" sm="12">
                    <br/>
                    <validation-provider v-slot="{ errors }" rules="required" name="tan_in" >
                      <label for="tan_in">Type of Asset</label>
                      <b-form-radio-group @change="onChange($event)" v-model="selected"
                                    :options="tangible_intan"
                                    id="tan_in"
                                    name="tan_in"
                                    class = "border border-radius p-3"
                                    style = "Background: #E5E5E5; "
                                  
                                    :state="getValidationState(errors)"
                      >
                      </b-form-radio-group>
                      
        
                      <b-form-invalid-feedback>
                        {{ errors[0] }}
                      </b-form-invalid-feedback>
                    </validation-provider>
                  
                  </b-col>
                  
                  <!-- Bought/Sold Radio Input  -->
                <b-col class="mb-2 ml-2 c-box pl-0" xl="7" md="6" sm="12">
                  <validation-provider v-slot="{ errors }" rules="required" name="bought_sold" >
                    <label for="bought_sold"> Bought or Sold?</label>
                    <b-form-radio-group v-model="form.bought_sold"
                                  :options="bought_sold"
                                  id="bought_sold"
                                  name="bought_sold"
                                  class = "border border-radius p-3"
                                  style = "Background: #E5E5E5; "
                                  :state="getValidationState(errors)"
                    >
                    </b-form-radio-group>
                    
      
                    <b-form-invalid-feedback>
                      {{ errors[0] }}
                    </b-form-invalid-feedback>
                  </validation-provider>
                
                </b-col>
                  <!-- Paid Using Radio Input  -->
                <b-col cols = "6" class=" mb-2 ml-2 c-box pl-0" xl="7" md="10" sm="12">
                  <validation-provider v-slot="{ errors }" rules="required" name="paid_using" >
                    <label for="paid_using"> Paid Using</label>
                    <b-form-radio-group v-model="form.paid_using"
                                  :options="paid_using"
                                  id="paid_using"
                                  name="paid_using"
                                  class = "border border-radius p-3"
                                  style = "Background: #E5E5E5; "
                                  :state="getValidationState(errors)"
                    >
                    </b-form-radio-group>
                    
      
                    <b-form-invalid-feedback>
                      {{ errors[0] }}
                    </b-form-invalid-feedback>
                  </validation-provider>
                
                </b-col>
              </b-col>

          </b-row>
          <!-- Submit and Reset -->
              <b-row cols="12" class="text-right my-2">
                <b-button type="submit" variant="primary" >Submit</b-button>
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
import Modal from '../../../components/argon-core/Modal.vue';
import BaseAlert from '../../../components/argon-core/BaseAlert.vue';

    export default {
        name: "non-current-asset-create",
        layout:"DashboardLayout",
        components: {
            ValidationProvider,
            ValidationObserver,
      
                Modal,
                BaseAlert,
             },
        data() {
            return {
                reduct_hide: false,
                selected: '',
                alert_message:'',
                form: {
                    date: new Date().toISOString()
                },
                asset_options: [
                    {value:'', text: 'Please select an option'},
                    {value: 'Straight-Line Method', text: 'Straight-Line'},
                    {value: 'Declining Balance', text: 'Declining Balance '},
                    {value: 'Units of Production', text: 'Units of Production'},
                    {value: 'Sum of Year\'s Digits', text: 'Sum of Year\'s Digits'},
                ], 
                tangible_intan: [
                  {value: 'Tangible Asset', text: 'Tangible Asset'},
                  {value: 'Intangible Asset', text:' Intangible Asset'}
                ], 

                paid_using: [
                   {value: 'Cash', text: 'Cash '},
                  {value: 'Cheque', text:'Cheque '},
                  {value: 'Credit', text:'Credit '},
                ], 

                bought_sold: [
                   {value: 'Bought', text: 'Bought Asset'},
                   {value: 'Sold', text:' Sold Asset'}
                ]
            }
        },
        methods: {
            onChange: (event)=> { 
              // let self = this;
              let radio = document.getElementById("tan_in"); 
              console.log(event);
              let data = event;
              // if (data== "Tangible Asset"){
              //   this.reduct_hide = false;
              //   // console.log(this.reduct_hide);
              //   console.log("apples");
              //   // this.reduct_hide = 'True';
              
              // }
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

            },
            modalCancel(){
                this.$refs['confirmModal'].hide();
            },
            modalSubmit(){
                let self = this;
                let PATH_API = 'transaction/noncurrentasset';
                let NCAForm = document.getElementById('AddNCAForm');
                let form_data = new FormData(NCAForm);
                form_data.append('form_id','AddNCAForm' );
                this.$axios.post(`/api/${PATH_API}`, form_data, {
                        headers: {
                        'contentType': 'application/json',
      
                        }
                })
                .then( jsonResponse =>{
                    return jsonResponse.json();
                })
                .then( jsonResponse =>{
                    this.$refs['confirmModal'].hide();
                    console.log(jsonResponse);
                    console.log(form_data);
                    self.alert_message = jsonResponse.message;
                }).catch(err => {
                        console.log(err);
                })
        },
            async launchConfirm(){
                let self = this;
                const submit = await this.$refs['confirmModal'].show();
              
            }
            
        }
    }
</script>

<style scoped>

</style>
