<template>
  <div class="d-flex mx-3">
  <b-container fluid>]
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
      <b-form @submit.stop.prevent="handleSubmit(launchConfirm)">
        <b-row>
          <b-col cols="12" class="text-info mb-3" v-b-tooltip.hover title="Example of purchases are......">Add Purchases</b-col>
          <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
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
          <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
            <validation-provider
              v-slot="{ errors }"
              rules="required"
              name="supplier name"
            >
              <label for="supplier_name">Supplier Name</label>
              <b-form-select v-model="form.supplier_name"
                             :options="supplier_name_options"
                             id="supplier_name"
                             :state="getValidationState(errors)"
              >
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
              name="quantity"
            >
              <label for="quantity">Quantity</label>
              <b-form-input v-model="form.quantity"
                            type="number"
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
              name="date"
            >
              <label for="date">Date</label>
              <b-form-datepicker id="date"
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
          <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
            <validation-provider
              v-slot="{ errors }"
              rules="required"
              name="amount/cost"
            >
              <label for="amount_cost">Amount/Cost</label>
              <b-form-input v-model="form.amount_cost"
                            type="number"
                            id="amount_cost"
                            :state="getValidationState(errors)">
              </b-form-input>
              <b-form-invalid-feedback>
                {{ errors[0] }}
              </b-form-invalid-feedback>
            </validation-provider>
          </b-col>
          <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <label for="description">Description</label>
              <b-form-textarea v-model="form.description"
                            type="text"
                            id="description"
                            >
              </b-form-textarea>
          </b-col>
          <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
            <validation-provider
              v-slot="{ errors }"
              rules="required"
              name="shipping methods"
            >
              <label for="shipping_methods">Shipping Methods</label>
              <b-form-select v-model="form.shipping_methods"
                             :options="shipping_methods_options"
                             id="shipping_methods"
                             :state="getValidationState(errors)"
              >
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
              name="discount"
            >
              <label for="discount">Discount</label>
              <b-form-input v-model="form.discount"
                            type="number"
                            id="discount"
                            :state="getValidationState(errors)">
              </b-form-input>
              <b-form-invalid-feedback>
                {{ errors[0] }}
              </b-form-invalid-feedback>
            </validation-provider>
          </b-col>
          <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <label for="notes">Notes</label>
              <b-form-textarea v-model="form.notes"
                            type="text"
                            id="notes"
                            >
              </b-form-textarea>
          </b-col>
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
    import Modal from '../../../components/argon-core/Modal.vue';
    import BaseAlert from '../../../components/argon-core/BaseAlert.vue';

    export default {
        layout: 'DashboardLayout',
        name: "purchase-create",
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
                    date: new Date().toISOString()
                },
                asset_options: [
                    {value: null, text: 'Please select an option'},
                    {value: 'a', text: 'This is First option'},
                    {value: 'b', text: 'Selected Option'},
                ]
            }
        },
        methods: {
            modalCancel(){
                this.$refs['confirmModal'].hide();
            },
            modalSubmit(){
              let PATH_API = 'transaction/purchases';
                let form_data = new FormData();
                Object.entries(this.form).forEach(entry => {
                    const [key, value] = entry;
                    form_data.append(key, value);
                });
                // form_data.append('form_id', 'AddCAForm');
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
                    }).catch(err=>{
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
