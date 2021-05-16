<template>
    <div class="d-flex mx-3">
      
      <b-container fluid>
        
       <base-alert v-if= "alert_message" 
                    class = "mt-5 d-flex flex-row justify-content-center" 
                    style="width: 25rem; 
                           height: 3rem; 
                           z-index:1;" 
                    dismissible      
                    type= "primary">{{message}}
      </base-alert>
      <b-row>
        <back-button class="mt-4 ml-2"></back-button>
        <b-col>
           <h3 class="mt-4 ml-0">Manage Products</h3>
            <p class = "mb-2 mt-2 ">  
                Keep track of your products.
              </p>
        </b-col>
      </b-row>
     
      <b-modal ref="confirmModal" 
                 id = "confirmModal" 
                  >
            Are you sure you want to add this product?
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
        <validation-observer
          ref="observer"
          v-slot="{handleSubmit}"
        >
        
          <b-form id="newProductForm" method="POST" @submit.stop.prevent="handleSubmit(launchConfirm)" enctype="multipart/form-data">
            <input type="hidden" name="_token" :value="token">
            <b-row class="m-1 w-100">
              <b-col cols="12" class="text-primary mb-3 pl-0">Add Product</b-col>
              <b-col md="12" cols="12" class="bg-secondary px-5 py-3">
                <b-row>
                  <div class="mb-2 w-50">
                    <validation-provider
                    v-slot="{ errors }"
                    rules="required"
                    name="product name"
                  >
                    <label for="product_name">Product Name
                      <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="eg. "/>
                    </label>
                    <b-form-input v-model="form.product_name"
                                  type="text"
                                  id="product_name"
                                  name="product_name"
                                  :state="getValidationState(errors)">
                    </b-form-input>
                    <b-form-invalid-feedback>
                      {{ errors[0] }}
                    </b-form-invalid-feedback>
                  </validation-provider>
                  </div>
                </b-row>
                <b-row>
                  <div class=" mb-2">
                    <validation-provider
                      v-slot="{ errors }"
                      rules="required"
                      name="product image"
                    >
                      <label for="image">Product Image
                        <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="eg. "/>
                      </label>
                      <b-form-file  v-model="form.image_file"
                                    class="w-100"
                                    id="image"
                                    name="image"
                                    placeholder="Choose a file or drop it here..."
                                    drop-placeholder="Drop file here..."
                                    :state="getValidationState(errors)">
                      </b-form-file>
                      <b-form-invalid-feedback>
                        {{ errors[0] }}
                      </b-form-invalid-feedback>
                    </validation-provider>
                  </div>
                </b-row>
                  
                
              
              <!--<div class="mb-2">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="product description"
                >
                  <label for="desc">Product Description
                    <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="eg. "/>
                  </label>
                  <b-form-textarea v-model="form.desc"
                                class="w-100"
                                id="desc"
                                name="desc"
                                :state="getValidationState(errors)">
                  </b-form-textarea>
                  <b-form-invalid-feedback>
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </validation-provider>
              </div>
              
              <div class="mb-2">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="measurement unit"
                >
                  <label for="uom">Unit of Measurement
                    <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="eg. "/>
                  </label>
                  <b-form-select v-model="form.uom"
                                class="w-100"
                                id="uom"
                                name="uom"
                                :options="uom_options"
                                :state="getValidationState(errors)">
                  </b-form-select>
                  <b-form-invalid-feedback>
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </validation-provider>
              </div>
              -->
                <b-row>
                  <div class="mb-2 ">
                    <validation-provider
                      v-slot="{ errors }"
                      rules="required"
                      name="quantity stock"
                    >
                      <label for="quantity">Quantity In Stock
                        <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="eg. "/>
                      </label>
                      <b-form-input v-model="form.quanitity"
                                    type="number"
                                    class="w-100"
                                    id="quantity"
                                    name="quantity"
                                    :state="getValidationState(errors)">
                      </b-form-input>
                      <b-form-invalid-feedback>
                        {{ errors[0] }}
                      </b-form-invalid-feedback>
                    </validation-provider>
                  </div>

                  <div class="ml-5 mb-2">
                    <validation-provider
                      v-slot="{ errors }"
                      rules="required"
                      name="unit price"
                    >
                      <label for="unit_price">Unit Price
                        <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="eg. "/>
                      </label>
                      <b-form-input v-model="form.unit_price"
                                    type="number"
                                    class="w-100"
                                    id="unit_price"
                                    name="unit_price"
                                    :state="getValidationState(errors)">
                      </b-form-input>
                      <b-form-invalid-feedback>
                        {{ errors[0] }}
                      </b-form-invalid-feedback>
                    </validation-provider>
                  </div>

                  <div class="ml-5 mb-2">
                    <validation-provider
                      v-slot="{ errors }"
                      rules="required"
                      name="tax percent"
                    >
                      <label for="tax">Tax percent
                        <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="eg. "/>
                      </label>
                      <b-form-input v-model="form.tax"
                                    type="number"
                                    class="w-100"
                                    id="tax"
                                    name="tax"
                                    :state="getValidationState(errors)">
                      </b-form-input>
                      <b-form-invalid-feedback>
                        {{ errors[0] }}
                      </b-form-invalid-feedback>
                    </validation-provider>
                  </div>
                </b-row>

                <b-row>
                  <div class="mb-2">
                    <validation-provider
                      v-slot="{ errors }"
                      rules="required"
                      name="product status"
                    >
                      <label for="status">Product Status</label>
                      <b-form-select v-model="form.status"
                                    class="w-100"
                                    id="status"
                                    name="status"
                                    :options="status_options"
                                    :state="getValidationState(errors)">
                      </b-form-select>
                      <b-form-invalid-feedback>
                        {{ errors[0] }}
                      </b-form-invalid-feedback>
                    </validation-provider>
                  </div>

                  
                </b-row>

              </b-col>
            </b-row>
            <b-row class=" my-4 px-3">
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
    import Modal from '../../components/argon-core/Modal.vue';
    import BaseAlert from '../../components/argon-core/BaseAlert.vue';
    import BackButton from '../../components/argon-core/BackButton.vue';
    export default {
        components: { ValidationObserver, ValidationProvider, BackButton, Modal, BaseAlert },
        layout: 'DashboardLayout',
        name: "add",
        head(){
          return{
              title: 'Add Product'
          }
        },
        data() {
            return {
                alert_message:'',
                token: '',
                form: {
                  date: new Date().toISOString()
                },
                uom_options: [
                    {value: null, text: 'Please select an option'},
                    {value: 'Kilogram(kg)', text: 'Kilogram(kg)'},
                    {value: 'Gram(g)', text: 'Gram(g)'},
                    {value: 'Cup', text: 'Cup'},
                    {value: 'Ounce(oz)', text: 'Ounce(oz)'},
                    {value: 'Litre(L)', text: 'Litre(L)'},
                    {value: 'Millilitre(ml)', text: 'Millilitre(ml)'},
                    {value: 'Teaspoon(tsp)', text: 'Teaspoon(tsp)'},
                    {value: 'Tablespoon(tbsp)', text: 'Tablespoon(tbsp)'},
                    {value: 'Dress', text: 'Dress'},
                    {value: 'Skirt', text: 'Skirt'},
                    {value: 'Pants', text: 'Pants'},
                    {value: 'Top', text: 'Top'},
                ],
                status_options: [
                    {value: null, text: 'Please select an option'},
                    {value: 'Active', text: 'Active'},
                    {value: 'Inactive', text: 'Inactive'},
                ]
            }
        },
        computed: {
            alert () {
                return this.$store.state.alert
            }
        },
        watch:{
            $route (to, from){
                // clear alert on location change
                this.$store.dispatch('alert/clear');
            }
        },
        methods: {
            getValidationState(errors) {
                return errors.length > 0 ? false : null;
            },
            resetForm() {
                this.form = {};
                this.$nextTick(() => {
                    this.$refs.observer.reset();
                });
            },
            async launchConfirm(){
                let self = this;
                const submit = await this.$refs['confirmModal'].show();
            },
            modalCancel(){
                this.$refs['confirmModal'].hide();
            },
            modalSubmit() {
              let newProductForm = document.getElementById("newProductForm");
              let form_data = new FormData(newProductForm);
              
              try {
                 if (form_data) {
             
                    this.$store.dispatch('products/addProduct', {form_data});
                    //$nuxt.$router.push('/');
                    this.$store.dispatch('alert/clear');
                        
                }
              } catch (error) {
                  console.log(error);
                }
            }
        },
    }
</script>

<style scoped>

</style>
