<template>
  <div class="d-flex">
    <side-bar></side-bar>
  <b-container fluid>
    <top-bar/>
    <h3 class="m-2">Add Transaction</h3>
    <transaction-top/>
    <validation-observer
      ref="observer"
      v-slot="{handleSubmit}"
    >
      <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
        <b-row>
           <b-col cols="12" class="text-info mb-3">Add Expenses</b-col>
          <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
            <validation-provider
              v-slot="{ errors }"
              rules="required"
              name="reference number"
            >
              <label for="ref_no">Reference Number</label>
              <b-form-input v-model="form.ref_no"
                            type="text"
                            id="ref_no"
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
              name="expense type"
            >
              <label for="expense_type">Expense Type</label>
              <b-form-select v-model="form.expense_type"
                             :options="expense_options"
                             id="expense_type"
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
              name="depreciation"
            >
              <label for="depreciation">Depreciation</label>
              <b-form-input v-model="form.depreciation"
                            type="number"
                            id="depreciation"
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
              name="amount"
            >
              <label for="amount">Amount</label>
              <b-form-input v-model="form.amount"
                            type="number"
                            id="amount"
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
        name: "expense-create",
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                form: {
                    date: new Date().toISOString()
                },
                expense_options: [
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
