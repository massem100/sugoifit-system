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
            <b-col cols="12" class="text-info mb-3">Add Equity</b-col>
          </b-row>
        </b-form>
      </validation-observer>
    </b-container>
  </div>
</template>

<script>
    import {ValidationObserver, ValidationProvider} from "vee-validate";

    export default {
        name: "equity-create",
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                form: {
                    date: new Date().toISOString()
                },
                customer_name_options: [
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
