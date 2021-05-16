<template>
  <div class="d-flex mx-3">
    <b-container fluid>
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
        <b-form id= "equityForm" @submit.stop.prevent="handleSubmit(launchConfirm)">
          <b-row>
            <b-col cols="12" class="text-info mb-3" v-b-tooltip.hover title="An equity is......">Add Equity</b-col>
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
        name: "equity-create",
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
                customer_name_options: [
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
                let PATH_API = 'transaction/equity';
                let form_data = new FormData();
                Object.entries(this.form).forEach(entry => {
                    const [key, value] = entry;
                    form_data.append(key, value);
                });
                form_data.append('form_id', 'equityForm');
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
                    }).catch(err => {
                         
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
