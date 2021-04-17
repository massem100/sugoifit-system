<template>
    <div class="d-flex mx-3">
      <b-container fluid>
        <validation-observer
          ref="observer"
          v-slot="{handleSubmit}"
        >
          <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
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
                  name="add quantity"
                >
                  <label for="ref_no">Add Quantity</label>
                  <b-form-input v-model="form.add_quantity"
                                type="number"
                                class="w-100"
                                id="add_quantity"
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
                  name="unit price"
                >
                  <label for="unit_price">Unit Price</label>
                  <b-form-input v-model="form.unit_price"
                                type="number"
                                class="w-100"
                                id="unit_price"
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
                  name="threshold"
                >
                  <label for="threshold">Threshold</label>
                  <b-form-input v-model="form.threshold"
                                type="number"
                                class="w-100"
                                id="threshold"
                                :state="getValidationState(errors)">
                  </b-form-input>
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
                form: {}
            }
        },
        methods: {
            getValidationState(errors) {
                return errors.length > 0 ? false : null;
            },
        }
    }
</script>

<style scoped>

</style>
