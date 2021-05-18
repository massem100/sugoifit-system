<template>
  <div class="d-flex flex-column">
      <base-alert v-if= "alert_message" 
                    class = "mt-5 d-flex flex-row justify-content-center" 
                    style="width: 25rem; 
                           height: 3rem; 
                           z-index:1;" 
                    dismissible      
                    type= "primary">{{alert_message}}
      </base-alert>
        <b-row>
          <back-button></back-button>
          <b-col>
            <h2  class="mt-3 ml-0"> Manage Transactions </h2>
            <!-- <p class="mt-3 ml-0  font-weight-bold">Add Non Current Asset </p> -->
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
         <h3 class="text-primary ml-5" :style="[{font: `600 1rem 'Poppins'`}]"
                    v-b-tooltip.hover title="Non-current Assets are......">Add Non Current Asset</h3>
    <validation-observer class="ml-5 w-50 " ref="observer" v-slot="{handleSubmit}">
      <b-form class ="" id= "AddNCAForm"   @submit.stop.prevent="handleSubmit(launchConfirm)">
          <div class="d-flex flex-row m-2 align-items-center">
            <!-- Asset Name -->
            <validation-provider class=" w-50 " v-slot="{ errors }" rules="required" name="asset name" >
                <label for="asset_name">Asset Name</label>
                <b-form-input v-model="form.asset_name" type="text" 
                              id="asset_name" name="asset_name"
                              class="p-4"
                              
                                :state="getValidationState(errors)">
                </b-form-input>
                <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
            </validation-provider>
                  <!-- Amount Input -->
            <validation-provider class="ml-3 w-50" v-slot="{ errors }" rules="required" name="amount">
                <label for="amount">Amount</label>
                <b-form-input v-model="form.amount" type="number"  id="amount" name="amount"
                                :state="getValidationState(errors)">
                </b-form-input>
                <b-form-invalid-feedback>
                    {{ errors[0] }}
                </b-form-invalid-feedback>
            </validation-provider>
          </div>
        <div class="d-flex flex-row m-2 align-items-center">
              <!-- Transaction Date -->
            <validation-provider class="w-50" v-slot="{ errors }" rules="required" name="transaction_date">
              
                    <label for="date">Date</label>
                    <b-form-datepicker id="transaction_date"
                                        name ="transaction_date"
                                        v-model="form.date"
                                        :date-format-options="{ year: 'numeric', month: 'short', day: 'numeric' }"
                                        locale="en-US"
                                        required
                                        calendar-width="200px"
                                        class="p-0 "
                                        
                                        :state="getValidationState(errors)"
                    >
                    </b-form-datepicker>

                    <b-form-invalid-feedback>
                        {{ errors[0] }}
                    </b-form-invalid-feedback>
    
            </validation-provider>
            
            <!-- Tag  -->
            <validation-provider class="m-2 ml-3  w-50" v-slot="{ errors }" rules="required" name="tag" >
                <label for="tag">Tag</label>
                <b-form-select v-model="form.tag"
                            :options="tag_items"
                            id="tag"
                            name="tag"
                            class=""
                            
                            :state="getValidationState(errors)"
                >
                </b-form-select>
                <b-form-invalid-feedback>
                {{ errors[0] }}
                </b-form-invalid-feedback>
            </validation-provider>
        </div>

        <div class="d-flex flex-row align-items-center">
            <!-- Bought Sold -->
            <validation-provider class = "w-50" v-slot="{ errors }" rules="required" name="bought_sold" >
                <label for="bought_sold"> Bought or Sold?</label>
                <b-form-select v-model="form.bought_sold"
                                :options="bought_sold"
                                id="bought_sold"
                                name="bought_sold"
                                class = "border border-radius p-3"
                                style = "Background: #E5E5E5; "
                                size = "lg"
                                :state="getValidationState(errors)"
                >
                </b-form-select>
                

                <b-form-invalid-feedback>
                    {{ errors[0] }}
                </b-form-invalid-feedback>
            </validation-provider>

            <!-- Paid Using -->
            <validation-provider class="m-2 w-50 ml-3" v-slot="{ errors }" rules="required" name="bought_sold" >
            <label for="paid_using"> Paid Using Cash or Cheque</label>
            <b-form-select v-model="form.paid_using"
                            :options="paid_using"
                            id="paid_using"
                            name="paid_using"
                            class = "border border-radius p-3"
                            style = "Background: #E5E5E5; "
                            size = "lg"
                            :state="getValidationState(errors)"
            >
            </b-form-select>
            <b-form-invalid-feedback>
                {{ errors[0] }}
            </b-form-invalid-feedback>
        </validation-provider>
        
         
        </div>

        <div class="text-primary mb-3 pl-0"><strong>Depreciation</strong></div>
        <div class="d-flex flex-row m-2 align-items-center">
             <!-- Depreciation Type Input  -->
            <validation-provider class="w-50 m-2" v-slot="{ errors }" rules="required" name="dep type" >
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

            <!-- Intangible Assets Input  -->
            <validation-provider class="w-50 m-2" v-slot="{ errors }" rules="required" name="tan_in" >
                <label for="tan_in">Type of Asset</label>
                <b-form-select v-model="form.tan_in"
                            :options="tangible_intan"
                            id="tan_in"
                            name="tan_in"
                            
                            :state="getValidationState(errors)"
                >
                </b-form-select>
                <b-form-invalid-feedback>
                {{ errors[0] }}
                </b-form-invalid-feedback>
            </validation-provider>
        </div>
         <div class="d-flex flex-row align-items-center"> 
                <!-- Asset LifeSpan -->
                <validation-provider class="m-2 w-50" v-slot="{ errors }" name="asset lifespan" >
                    <label for="expected_lifespan">Asset Lifespan</label>
                    <b-form-input v-model="form.asset_lifespan"
                                type="number"
                                id="asset_lifespan"
                                name="asset_lifespan"
                                
                                :state="getValidationState(errors)">
                    </b-form-input>
                    <b-form-invalid-feedback>
                    {{ errors[0] }}
                    </b-form-invalid-feedback>
                </validation-provider>
                   <!-- Salvage Value-->  
                <validation-provider class="m-2 w-50 ml-3" v-slot="{ errors }" rules="required" name="salvage value" >
                    <label for="depreciation">Salvage Value</label>
                    <b-form-input v-model="form.salvage_val"
                                type="number"
                                id="salvage_val"
                                name="salvage_val"
                                
                                :state="getValidationState(errors)">
                    </b-form-input>
                    <b-form-invalid-feedback>
                    {{ errors[0] }}
                    </b-form-invalid-feedback>
                </validation-provider>
                                                                                                                                     
         </div>
          
             
               
          <div>
            <!-- Description Input -->
            <b-col class="mb-2 pl-0">
                <label for="description">Description</label>
                <b-form-textarea v-model="form.description" type="text" id="description"></b-form-textarea>
            </b-col>    

        </div>
          <!-- Submit and Reset -->
              <b-row cols="12" class="text-right my-2">
                <b-button type="submit" variant="primary" >Submit</b-button>
                <b-button type="reset" variant="danger" @click="resetForm()">Reset</b-button>
              </b-row>
      </b-form>
    </validation-observer>
 
  </div>
</template>

<script>
    // import axios from '@nuxtjs/axios';
    import {ValidationObserver, ValidationProvider} from "vee-validate";
import Modal from '../../../components/argon-core/Modal.vue';
import BaseAlert from '../../../components/argon-core/BaseAlert.vue';
import BackButton from '../../../components/argon-core/BackButton.vue';

    export default {
        name: "non-current-asset-create",
        layout:"DashboardLayout",
        components: {
            ValidationProvider,
            ValidationObserver,
      
                Modal,
                BaseAlert,
                BackButton,
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
                ], 
                tag_items: [
                    {value: 'Property Plant & Equipment', text: 'Property Plant & Equipment'},
                    {value: 'Intangible Asset', text: 'Intangible Asset'},
                    {value: 'Long Term Investment', text: 'Long Term Investment'},
                    {value: 'Other Non Current Asset', text: 'Other Non Current Asset'},
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
