<template>
    <div>
        <b-container fluid>
            <validation-observer ref="observer" v-slot="{handleSubmit}">
                <form id="contactForm" method="POST" @submit.stop.prevent="handleSubmit(onSubmit)" enctype="multipart/form-data">
                    <input type="hidden" name="_token" :value="token">
                    <b-row >
                        
                        <b-col cols="8" >
                            <h2 class="text-center"> Receipt</h2>
                            <h4 class="text-center"> Please upload proof of payment to start the processing of your order.</h4>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col class="mb-2 c-box" xl="6" md="8" sm="10">
                            <validation-provider
                            v-slot="{ errors }"
                            rules="required"
                            name="Customer name"
                            >
                            <label for="name">Full Name</label>
                            <b-form-input v-model="form.name"
                                            type="text"
                                            id="name"
                                            name="name"
                                            :state="getValidationState(errors)">
                            </b-form-input>
                            <b-form-invalid-feedback>
                                {{ errors[0] }}
                            </b-form-invalid-feedback>
                            </validation-provider>
                        </b-col>
                    </b-row>
                    
                    <b-row>
                        <b-col class="mb-2 c-box" xl="6" md="8" sm="10">
                            <validation-provider
                            v-slot="{ errors }"
                            rules="required"
                            name="customer email"
                            >
                            <label for="email">E-mail Address</label>
                            <b-form-input v-model="form.email"
                                            type="email"
                                            id="email"
                                            name="email"
                                            :state="getValidationState(errors)">
                            </b-form-input>
                            <b-form-invalid-feedback>
                                {{ errors[0] }}
                            </b-form-invalid-feedback>
                            </validation-provider>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col class="mb-2 c-box" xl="6" md="8" sm="10">
                            <validation-provider
                            v-slot="{ errors }"
                            rules="required"
                            name="order invoice number"
                            >
                            <label for="invoice_num">Invoice Number</label>
                            <b-form-input v-model="form.phone"
                                            type="number"
                                            id="invoice_num"
                                            name="invoice_num"
                                            :state="getValidationState(errors)">
                            </b-form-input>
                            <b-form-invalid-feedback>
                                {{ errors[0] }}
                            </b-form-invalid-feedback>
                            </validation-provider>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col class="mb-2 c-box" xl="6" md="8" sm="10">
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
                </form>
            </validation-observer>
        </b-container>
    </div>
</template>

<script>
import {ValidationObserver, ValidationProvider} from "vee-validate";
export default {
    name: "PaymentReceipt",
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
            let contactForm = document.getElementById("contactForm");
            let form_data = new FormData(contactForm);
            
            let PATH_API = 'contact';
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
label{
  display:block;
  margin:1em 0 .2em;
}
input{
  display:block;
  width:100%;
  padding:.3em;
  font-size:20px;
  border: none;
  background-color: rgba(119, 255, 187, 0.705);
  border-radius: 20px;
  resize:vertical;
}
</style>
