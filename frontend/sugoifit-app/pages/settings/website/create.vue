<template>
  <div class="d-flex">
    <side-bar></side-bar>
    <b-container fluid>
        <top-bar/>
        <settings-top/>
        <validation-observer ref="observer" v-slot="{handleSubmit}">

        <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
            <b-row>
                <b-col cols="12" class="text-info mb-3">Welcome Section</b-col>
                    <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                        <validation-provider v-slot="{ errors }" rules="required" name="welcome header">
                        <label for="ref_no">Welcome Heading: </label>
                        <b-form-input v-model="form.wel_head"
                                        type="text"
                                        id="wel_head"
                                        :state="getValidationState(errors)">
                        </b-form-input>
                        <b-form-invalid-feedback>
                            {{ errors[0] }}
                        </b-form-invalid-feedback>
                        </validation-provider>
                    </b-col>
                    <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                        <validation-provider v-slot="{ errors }" rules="required" name="welcome message">
                        <label for="ref_no">Welcome Message: </label>
                        <b-form-input v-model="form.wel_mess"
                                        type="text"
                                        id="wel_mess"
                                        :state="getValidationState(errors)">
                        </b-form-input>
                        <b-form-invalid-feedback>
                            {{ errors[0] }}
                        </b-form-invalid-feedback>
                        </validation-provider>
                    </b-col>
                    

                <b-col cols="12" class="text-info mb-3">Product Section</b-col>
                    <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                        <validation-provider v-slot="{ errors }" rules="required" name="product message">
                        <label for="ref_no">Product Message: </label>
                        <b-form-input v-model="form.prod_mess"
                                        type="text"
                                        id="prod_mess"
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
        </b-form>
        </validation-observer>

        <table class="table">
            <thead class="thead-dark">
                <tr>
                    <th scope="col">Position</th>
                    <th scope="col">Section Name</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th scope="row">1</th>
                    <td>Welcome</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Products</td>
                </tr>
                <tr>
                    <th scope="row">3</th>
                    <td>Receipt</td>
                </tr>
                <tr>
                    <th scope="row">4</th>
                    <td>Contact</td>
                </tr>
            </tbody>
        </table>
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
                form: {
                    wel_head: '',
                    wel_mess: '',
                    prod_mess: '',
                    rec_head: '',
                    rec_mess: '',
                    con_head: '',
                    con_mess: ''
                },
            }
        },
        methods: {
            getValidationState(errors) {
                return errors.length > 0 ? false : null;
            },

            onSubmit() {
                
                this.$axios.post('/api/website-settings', this.form)                    
                .then((result) => { console.log(result.data); })
                .catch(function (error) { console.log(error); });

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
