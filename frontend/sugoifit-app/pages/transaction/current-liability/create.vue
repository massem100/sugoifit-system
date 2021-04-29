<template>
  <div class="d-flex mx-3">
  <b-container fluid>
    <h3 class="m-2">Add Transaction</h3>
    <transaction-top/>
    <validation-observer
      ref="observer"
      v-slot="{handleSubmit}"
    >
      <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
        <b-row>
          <b-col cols="12" class="text-info mb-3">Add Current Liability</b-col>
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
              name="life of loan"
            >
              <label for="life_of_loan">Life of Loan</label>
               <b-form-input v-model="form.life_of_loan"
                            id="life_of_loan"
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
              name="person/creditor"
            >
              <label for="person_creditor">Person/Creditor</label>
              <b-form-select v-model="form.person_creditor"
                             :options="person_creditor_options"
                             id="person_creditor"
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
              name="amount borrowed"
            >
              <label for="amount_borrowed">Amount Borrowed</label>
              <b-form-input v-model="form.amount_borrowed"
                            type="number"
                            id="amount_borrowed"
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
              name="interest"
            >
              <label for="interest">Interest</label>
              <b-form-input v-model="form.interest"
                            type="number"
                            id="interest"
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
  </b-container>
  </div>
</template>

<script>
    import {ValidationObserver, ValidationProvider} from "vee-validate";

    export default {
        layout: 'DashboardLayout',
        name: "current-liability-create",
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                form: {
                    date: new Date().toISOString()
                },
                person_creditor_options: [
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
