<template>
  <div class="d-flex mx-3">
    <b-container fluid>
      <h3 class="m-2">Add Transaction</h3>
      <transaction-top/>
      <validation-observer
        ref="observer"
        v-slot="{handleSubmit}"
      >
<!--        <b-form @submit.stop.prevent="handleSubmit(onSubmit)">-->
<!--          <b-row>-->
<!--            <b-col cols="12" class="text-info mb-3">Add Supplier</b-col>-->
<!--            <b-col class="mb-2 c-box" xl="3" md="6" sm="12">-->
<!--              <validation-provider-->
<!--                v-slot="{ errors }"-->
<!--                rules="required"-->
<!--                name="Name"-->
<!--              >-->
<!--                <label for="name">Name</label>-->
<!--                <b-form-input v-model="form.name"-->
<!--                              type="text"-->
<!--                              id="name"-->
<!--                              :state="getValidationState(errors)">-->
<!--                </b-form-input>-->
<!--                <b-form-invalid-feedback>-->
<!--                  {{ errors[0] }}-->
<!--                </b-form-invalid-feedback>-->
<!--              </validation-provider>-->
<!--            </b-col>-->
<!--            <b-col class="mb-2 c-box" xl="3" md="6" sm="12">-->
<!--              <validation-provider-->
<!--                v-slot="{ errors }"-->
<!--                rules="required"-->
<!--                name="address"-->
<!--              >-->
<!--                <label for="address">Address</label>-->
<!--                <b-form-textarea v-model="form.address"-->
<!--                              type="text"-->
<!--                              id="name"-->
<!--                              :state="getValidationState(errors)">-->
<!--                </b-form-textarea>-->
<!--                <b-form-invalid-feedback>-->
<!--                  {{ errors[0] }}-->
<!--                </b-form-invalid-feedback>-->
<!--              </validation-provider>-->
<!--            </b-col>-->
<!--            <b-col class="mb-2 c-box" xl="3" md="6" sm="12">-->
<!--              <validation-provider-->
<!--                v-slot="{ errors }"-->
<!--                rules="required"-->
<!--                name="product"-->
<!--              >-->
<!--                <label for="product">Product</label>-->
<!--                <b-form-select v-model="form.product"-->
<!--                               :options="product_options"-->
<!--                               id="product"-->
<!--                               :state="getValidationState(errors)"-->

<!--                >-->
<!--                </b-form-select>-->
<!--                <b-form-invalid-feedback>-->
<!--                  {{ errors[0] }}-->
<!--                </b-form-invalid-feedback>-->
<!--              </validation-provider>-->
<!--            </b-col>-->
<!--            <b-col class="mb-2 c-box" xl="3" md="6" sm="12">-->
<!--              <validation-provider-->
<!--                v-slot="{ errors }"-->
<!--                rules="required"-->
<!--                name="date of entry"-->
<!--              >-->
<!--                <label for="date_of_entry">Date of Entry</label>-->
<!--                <b-form-datepicker id="date"-->
<!--                                   v-model="form.date_of_entry"-->
<!--                                   :transaction_date-format-options="{ year: 'numeric', month: 'short', day: 'numeric' }"-->
<!--                                   locale="en-US"-->
<!--                                   required-->
<!--                                   calendar-width="180px"-->
<!--                                   :state="getValidationState(errors)"-->
<!--                >-->
<!--                </b-form-datepicker>-->
<!--                <b-form-invalid-feedback>-->
<!--                  {{ errors[0] }}-->
<!--                </b-form-invalid-feedback>-->
<!--              </validation-provider>-->
<!--            </b-col>-->
<!--            <b-col cols="12" class="text-right my-2">-->
<!--              <b-button type="submit" variant="primary">Submit</b-button>-->
<!--              <b-button type="reset" variant="danger" @click="resetForm()">Reset</b-button>-->
<!--            </b-col>-->
<!--          </b-row>-->
<!--        </b-form>-->
      </validation-observer>
    </b-container>
  </div>
</template>

<script>
    import {ValidationObserver, ValidationProvider} from "vee-validate";

    export default {
        layout:'dashboard',
        name: "supply-create",
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                form: {
                    date: new Date().toISOString()
                },
                product_options: [
                    {value: null, text: 'Please select an option'},
                    {value: 'a', text: 'This is First option'},
                    {value: 'b', text: 'Selected Option'},
                ]
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

</style>
