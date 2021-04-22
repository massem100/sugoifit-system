<template>
    <div class="d-flex mx-3">
      <b-container fluid>
        <validation-observer
          ref="observer"
          v-slot="{handleSubmit}"
        >
          <b-form id="newProductForm" method="POST" @submit.stop.prevent="handleSubmit(onSubmit)" enctype="multipart/form-data">
            <input type="hidden" name="_token" :value="token">
            <b-row>
              <b-col cols="12" class="text-info mb-3 font-weight-bold">Add Product</b-col>
              <b-col class="mb-2 c-box" xl="6" md="6" sm="12">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="product name"
                >
                  <label for="product_name">Product Name</label>
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
              </b-col>
            </b-row>
            <b-row>
              <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="quantity stock"
                >
                  <label for="quantity">Quantity In Stock</label>
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
              </b-col>
              <!--
              <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="measurement unit"
                >
                  <label for="uom">Unit of Measurement</label>
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
              </b-col>
              -->
            </b-row>
            <b-row>
              <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="unit price"
                >
                  <label for="unit_price">Unit Price</label>
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
              </b-col>
              <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="tax percent"
                >
                  <label for="tax">Tax percent</label>
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
              </b-col>
            </b-row>
            <b-row>
              <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
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
              </b-col>

              <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="product image"
                >
                  <label for="image">Product Image</label>
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
              </b-col>
            </b-row>
            <b-row>
              <b-col cols="12" class="text-right my-2">
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
        layout: 'dashboard',
        name: "add",
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                
                token: '',
                form: {
                  date: new Date().toISOString()
                },
                uom_options: [
                    {value: null, text: 'Please select an option'},
                    {value: 'a', text: 'Kilogram(kg)'},
                    {value: 'b', text: 'Gram(g)'},
                    {value: 'c', text: 'Cup'},
                    {value: 'd', text: 'Ounce(oz)'},
                    {value: 'e', text: 'Litre(L)'},
                    {value: 'f', text: 'Millilitre(ml)'},
                    {value: 'g', text: 'Teaspoon(tsp)'},
                    {value: 'h', text: 'Tablespoon(tbsp)'},
                    {value: 'i', text: 'Dress'},
                    {value: 'j', text: 'Skirt'},
                    {value: 'k', text: 'Pants'},
                    {value: 'l', text: 'Top'},
                ],
                status_options: [
                    {value: null, text: 'Please select an option'},
                    {value: 'Active', text: 'Active'},
                    {value: 'Inactive', text: 'Inactive'},
                ]
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
            onSubmit() {
              let self = this;
              let newProductForm = document.getElementById("newProductForm");
              let form_data = new FormData(newProductForm);

              let PATH_API = 'newproduct';
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
