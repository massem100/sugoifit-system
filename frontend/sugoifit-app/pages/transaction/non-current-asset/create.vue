<template>
  <div class="d-flex mx-3">
  <b-container fluid>
    <h3 class="m-2">Add Transaction</h3>
    <transaction-top/>
    <validation-observer
      ref="observer"
      v-slot="{handleSubmit}"
    >
      <b-form id= "AddNCAForm" @submit.stop.prevent="handleSubmit(AddNCA)">
        
          <b-col class = "pl-0">
            
            <!-- Add Non Current Asset heading -->
            <b-col cols="8" class="text-info mb-3 pl-0">Add Non Current Asset</b-col>
            <b-row>
              <!-- Intangible/Tangible Asset Radio Input  -->
                <b-row class="mb-2 ml-2 c-box pl-0" xl="3" md="6" sm="12">
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
                
                </b-row>
                
                <!-- Bought/Sold Radio Input  -->
              <b-row class="mb-2 ml-2 c-box pl-0" xl="3" md="6" sm="12">
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
              
              </b-row>
                <!-- Paid Using Radio Input  -->
              <b-row class="mb-2 ml-2 c-box pl-0" xl="3" md="6" sm="12">
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
              
              </b-row>
            </b-row>
            
            <!-- Major Form Fiels -->
            <b-row class = "ml-1 pl-0 mt-4">
            <!-- Asset Name -->
              <b-col class="mb-2 c-box  pl-0" xl="3" md="6" sm="12">
                <validation-provider v-slot="{ errors }" rules="required" name="asset name" >
                  <label for="asset_name">Asset Name</label>
                  <b-form-input v-model="form.asset_name" type="text" id="asset_name" name="asset_name"
                                :state="getValidationState(errors)">
                  </b-form-input>
                  <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
                </validation-provider>
              </b-col>

              <!-- Transaction Date -->
              <b-col class="mb-2 c-box pl-0" xl="3" md="6" sm="12">
                <validation-provider v-slot="{ errors }" rules="required" name="transaction_date">
                  <label for="date">Date</label>
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
              <b-col  class="mb-2 c-box pl-0" xl="3" md="6" sm="12">
                <validation-provider v-slot="{ errors }" rules="required" name="amount">
                
                  <label for="amount">Amount</label>
                  <b-form-input v-model="form.amount" type="number" id="amount" name="amount"
                                :state="getValidationState(errors)">
                  </b-form-input>
                  <b-form-invalid-feedback>
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </validation-provider>
              </b-col>
              <!-- Amortization Selected -->
              <div>
                <div v-if= "reduct_hide">
                  <b-col cols="8" class="text-info mb-3 pl-0">Amortization</b-col>
                  <b-row class = "m-2">
                    
                  <!-- Depreciation Type Input  -->
                  <b-col class="mb-2 c-box pl-0" xl="3" md="6" sm="12">
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
                  <b-col class="mb-2 mr-3 c-box pl-0" xl="3" md="6" sm="12">
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
                  <b-col class="mb-2 c-box pl-0" xl="3" md="6" sm="12">
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
                <div v-else>
                  <b-col cols="8" class="text-info mb-3 pl-0">Depreciation</b-col>
                  <!-- Depreciation Selected -->
                  <b-row class = "ml-2">
                  <!-- Depreciation Type Input  -->
                  
                  <b-col class="mb-2 c-box pl-0" xl="3" md="6" sm="12">
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
                  <b-col class="mb-2 mr-3 c-box pl-0" xl="3" md="6" sm="12">
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
                  <b-col class="mb-2 c-box pl-0" xl="3" md="6" sm="12">
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
              </div>
                <!-- Description Input -->
              <b-col class="mb-2 c-box pl-0" xl="3" md="6" sm="12">
                  <label for="description">Description</label>
                  <b-form-textarea v-model="form.description" type="text" id="description"></b-form-textarea>
              </b-col>
             
              
            </b-row>

            
           <!-- Submit and Reset -->
            <b-col cols="12" class="text-right my-2">
              <b-button type="submit" variant="primary">Submit</b-button>
              <b-button type="reset" variant="danger" @click="resetForm()">Reset</b-button>
            </b-col>
          </b-col>
          
        
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
        layout:"dashboard",
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                reduct_hide: false,
                selected: '',
                form: {
                    date: new Date().toISOString()
                },
                asset_options: [
                    {value: null, text: 'Please select an option'},
                    {value: 'a', text: 'This is First option'},
                    {value: 'b', text: 'Selected Option'},
                ], 
                tangible_intan: [
                  {value: 'Tangible Asset', text: 'Tangible Asset'},
                  {value: 'Intangible Asset', text:' Intangible Asset'}
                ], 

                paid_using: [
                   {value: 'Cash', text: 'Cash'},
                  {value: 'Cheque', text:'Cheque'},
                  {value: 'Credit', text:'Credit'},
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
            AddNCA: function(){
              let self = this;
              let PATH_API = 'transaction/asset';
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
                console.log(jsonResponse);
              })
            },
            
        }
    }
</script>

<style scoped>

</style>
