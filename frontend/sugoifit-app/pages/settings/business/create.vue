<template>
  <div class="d-flex">
    <side-bar></side-bar>
    <b-container fluid>
        <top-bar/>
        <settings-top/>
        <validation-observer ref="observer" v-slot="{handleSubmit}">
        <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
            <b-row>
                <b-col cols="12" class="text-info mb-3">Company Details:</b-col>
                    <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                        <validation-provider v-slot="{ errors }" rules="required" name="reference number">
                        <label for="ref_no">Company Name: </label>
                        <b-form-input v-model="form.ref_no"
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
                        <validation-provider v-slot="{ errors }" rules="required" name="reference number">
                        <label for="ref_no">Company: </label>
                        <b-form-input v-model="form.ref_no"
                                        type="text"
                                        id="Wel_mess"
                                        :state="getValidationState(errors)">
                        </b-form-input>
                        <b-form-invalid-feedback>
                            {{ errors[0] }}
                        </b-form-invalid-feedback>
                        </validation-provider>
                    </b-col>
                    <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                        <validation-provider v-slot="{ errors }" rules="required" name="reference number">
                        <label for="ref_no">Company: </label>
                        <b-form-input v-model="form.ref_no"
                                        type="text"
                                        id="wel_img"
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
        name: "business-create",
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                form: {
                    date: new Date().toISOString()
                }
            }
        },
        methods: {
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
.side-bar{
  position: fixed;
}
</style>
