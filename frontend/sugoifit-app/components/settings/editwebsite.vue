<template>
  <div class="d-flex">
    <side-bar></side-bar>
    <b-container fluid>
        <top-bar/>
        <settings-top/>
        <validation-observer ref="observer" v-slot="{handleSubmit}">
        <form id = "websiteForm" @submit.stop.prevent="handleSubmit(onSubmit)">
            <b-row>
                <b-col cols="12" class="text-info mb-3">Welcome Section</b-col>
                    <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                        <validation-provider v-slot="{ errors }" rules="required" name="welcome header">
                        <label for="ref_no">Welcome Heading: </label>
                        <b-form-input v-model="form.wel_head"
                                        type="text"
                                        id="wel_head"
                                        name="wel_head"
                                        :state="getValidationState(errors)">
                        </b-form-input>
                        <b-form-invalid-feedback>
                            {{ errors[0] }}
                        </b-form-invalid-feedback>
                        </validation-provider>
                    </b-col>
                    <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                        <validation-provider v-slot="{ errors }" rules="required" name="welcome message">
                        <label for="ref_no">Welcome message: </label>
                        <b-form-input v-model="form.ref_no"
                                        type="text"
                                        id="Wel_mess"
                                        name="Wel_mess"
                                        :state="getValidationState(errors)">
                        </b-form-input>
                        <b-form-invalid-feedback>
                            {{ errors[0] }}
                        </b-form-invalid-feedback>
                        </validation-provider>
                    </b-col>
                    <!--
                    <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                        <validation-provider v-slot="{ errors }" rules="required" name="reference number">
                        <label for="ref_no">Welcome image: </label>
                        <b-form-input v-model="form.ref_no"
                                        type="text"
                                        id="wel_img"
                                        name="wel_img"
                                        :state="getValidationState(errors)">
                        </b-form-input>
                        <b-form-invalid-feedback>
                            {{ errors[0] }}
                        </b-form-invalid-feedback>
                        </validation-provider>
                    </b-col>
                    -->

                <b-col cols="12" class="text-info mb-3">Product Section</b-col>
                    <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                        <validation-provider v-slot="{ errors }" rules="required" name="product message">
                        <label for="ref_no">Product Message: </label>
                        <b-form-input v-model="form.prod_mess"
                                        type="text"
                                        id="prod_mess"
                                        name="prod_mess"
                                        :state="getValidationState(errors)">
                        </b-form-input>
                        <b-form-invalid-feedback>
                            {{ errors[0] }}
                        </b-form-invalid-feedback>
                        </validation-provider>
                    </b-col>
                    
                <b-col cols="12" class="text-info mb-3">Receipt Section</b-col>
                    <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                        <validation-provider v-slot="{ errors }" rules="required" name="receipt header">
                        <label for="ref_no">Receipt Heading: </label>
                        <b-form-input v-model="form.rec_head"
                                        type="text"
                                        id="rec_head"
                                        name="rec_head"
                                        :state="getValidationState(errors)">
                        </b-form-input>
                        <b-form-invalid-feedback>
                            {{ errors[0] }}
                        </b-form-invalid-feedback>
                        </validation-provider>
                    </b-col>
                    <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                        <validation-provider v-slot="{ errors }" rules="required" name="receipt message">
                        <label for="ref_no">Receipt Message: </label>
                        <b-form-input v-model="form.rec_mess"
                                        type="text"
                                        id="rec_mess"
                                        name="rec_mess"
                                        :state="getValidationState(errors)">
                        </b-form-input>
                        <b-form-invalid-feedback>
                            {{ errors[0] }}
                        </b-form-invalid-feedback>
                        </validation-provider>
                    </b-col>
                
                <b-col cols="12" class="text-info mb-3">Contact Section</b-col>
                    <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                        <validation-provider v-slot="{ errors }" rules="required" name="contact header">
                        <label for="ref_no">Contact Heading: </label>
                        <b-form-input v-model="form.con_head"
                                        type="text"
                                        id="con_head"
                                        name="con_head"
                                        :state="getValidationState(errors)">
                        </b-form-input>
                        <b-form-invalid-feedback>
                            {{ errors[0] }}
                        </b-form-invalid-feedback>
                        </validation-provider>
                    </b-col>
                    <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                        <validation-provider v-slot="{ errors }" rules="required" name="contact message">
                        <label for="ref_no">Contact Message: </label>
                        <b-form-input v-model="form.con_mess"
                                        type="text"
                                        id="con_mess"
                                        name="con_mess"
                                        :state="getValidationState(errors)">
                        </b-form-input>
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
        </form>
        </validation-observer>
        
        <b-table :items = "section"> </b-table>
          <h6>{{section}}</h6>
          <!-- <h1>{{msg}}</h1> -->
    </b-container>
  </div>
</template>

<script>
    import {ValidationObserver, ValidationProvider} from "vee-validate";

    export default {
        name: "website-create",
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                section: []
            }
        },
        methods: {
            SubmitForm(){
                let self = this;
              let PATH_API = 'test';
              let WebsiteForm = document.getElementById('websiteForm');
              let form_data = new FormData(WebsiteForm); 
              $axios.post(`/api/${PATH_API}`, {
                body: form_data,
                headers:{
                  'contentType': 'application/json',
                }
              })             
              .then( jsonResponse =>{
                return jsonResponse.json();
              })
              .then( jsonResponse =>{
                console.log(jsonResponse);
              });

            },
            getValidationState(errors) {
                return errors.length > 0 ? false : null;
            },

            onSubmit() {
                let self = this;
                let websiteForm = document.getElementById("websiteForm");
                let form_data = new FormData(websiteForm);
                let PATH_API = 'website-settings'

                fetch(`/api/${PATH_API}`, {
                    method: "POST",
                    body: form_data,
                    
                })
                    .then(function (response) {
                    return response.json();
                })
                .then(function (jsonResponse){
                        console.log("form_data");
                }).catch(function (error) {
                    console.log(error);
                });

            },
            resetForm() {
                this.form = {};
                this.$nextTick(() => {
                    this.$refs.observer.reset();
                });

            },
            ViewSections: function (){
              let self = this;
              fetch("http://localhost:8080/api/testdrop",{
                  method: "GET", 
                  headers:{
                    "Accept": "application/json"
                  }, 
                  credentials: "same-origin",
              })
              .then(function (response){
                  return response.json();
              })
                .then(function(jsonResponse){
                  console.log(jsonResponse);
                  self.stmt = jsonResponse;
                })
                .catch( function(error){
                 // console.log(error);
              });
        }
        }
    }
</script>

<style scoped>
</style>
