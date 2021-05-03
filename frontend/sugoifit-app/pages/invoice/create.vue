<template>
  <div class="d-flex mx-3">
    <b-container fluid>
      <top-bar/>
      <h3 class="m-2">Create Invoice</h3>
      <invoice-top/>
      <validation-observer
        ref="observer"
        v-slot="{handleSubmit}"
      >
        <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
          <b-row>
            <b-col cols="12" class="text-info mb-3">Add Invoice</b-col>

            <!-- Customer Name -->
            <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
            <validation-provider
              v-slot="{ errors }"
              rules="required"
              name="cust-name"
            >
              <label for="cust-name">Billed to:</label>
               <b-form-input v-model="form.cust_name"
                            id="cust-name"
                            :state="getValidationState(errors)">
              </b-form-input>
              <b-form-invalid-feedback>
                {{ errors[0] }}
              </b-form-invalid-feedback>
            </validation-provider>
            </b-col>

              <!-- Customer Email -->
              <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                  <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="cust_email"
                  >
                  <label for="cust_email">Customer Email: </label>
                  <b-form-select v-model="form.cust_email"
                                  :options="person_creditor_options"
                                  id="cust_email"
                                  :state="getValidationState(errors)"
                  >
                  </b-form-select>
                  <b-form-invalid-feedback>
                      {{ errors[0] }}
                  </b-form-invalid-feedback>
                  </validation-provider>
              </b-col>

              <!-- Customer Telephone -->
              <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
                  <validation-provider
                  v-slot="{ errors }"
                  rules="required"
                  name="cust_num"
                  >
                  <label for="cust_num">Customer Telephone: </label>
                  <b-form-select v-model="form.cust_num"
                                  :options="person_creditor_options"
                                  id="cust_email"
                                  :state="getValidationState(errors)"
                  >
                  </b-form-select>
                  <b-form-invalid-feedback>
                      {{ errors[0] }}
                  </b-form-invalid-feedback>
                  </validation-provider>
              </b-col>

              <!-- Date Issued -->
              <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <validation-provider
                v-slot="{ errors }"
                rules="required"
                name="date-issued"
              >
                <label for="date-issued"> Date Issued:</label>
                <b-form-datepicker id="date-issued"
                                  v-model="form.date_issued"
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

              <!-- Date Due -->
              <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <validation-provider
                v-slot="{ errors }"
                rules="required"
                name="date-due"
              >
                <label for="date-due"> Date Due:</label>
                <b-form-datepicker id="date-due"
                                  v-model="form.date_due"
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

              <!-- Balance Due -->
            <b-col class="mb-2 c-box" xl="3" md="6" sm="12">
              <validation-provider
                v-slot="{ errors }"
                rules="required"
                name="amount-due"
              >
                <label for="amount_borrowed">Balance Due: </label>
                <b-form-input v-model="form.amount_due"
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
        name: "invoice-create",
        layout: 'DashboardLayout',
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

</style>
