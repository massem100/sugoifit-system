<template>
    <div class="wrapper">

        <b-col>
            <b-container fluid>
                
                <validation-observer ref="observer" v-slot="{handleSubmit}">
                <form id="contactForm" method="POST" @submit.stop.prevent="handleSubmit(onSubmit)" enctype="multipart/form-data">
                    <input type="hidden" name="_token" :value="token">
                    <b-row class="mb-5">
                        
                        <b-col cols="12" >
                            <h2 class="text-center"> Contact Us</h2>
                            <h4 class="text-center"> Contact us today, and get reply within 24 hours!</h4>
                            <hr>
                            <b-row>
                                <b-col cols="12" class="text-center">{{items.address}}</b-col>
                                <b-col cols="12" class="text-center">{{items.email}}</b-col>
                                <b-col cols="12" class="text-center">{{items.phone}}</b-col>
                            </b-row>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col class="mb-2 c-box" xl="6" md="6" sm="12">
                            <validation-provider
                            v-slot="{ errors }"
                            rules="required"
                            name="Customer first name"
                            >
                            <label for="fname">First Name</label>
                            <b-form-input v-model="form.fname"
                                            type="text"
                                            id="fname"
                                            name="fname"
                                            :state="getValidationState(errors)">
                            </b-form-input>
                            <b-form-invalid-feedback>
                                {{ errors[0] }}
                            </b-form-invalid-feedback>
                            </validation-provider>
                        </b-col>
                    
                        <b-col class="mb-2 c-box" xl="6" md="6" sm="12">
                            <validation-provider
                            v-slot="{ errors }"
                            rules="required"
                            name="Customer last name"
                            >
                            <label for="lname">Last Name</label>
                            <b-form-input v-model="form.lname"
                                            type="text"
                                            id="lname"
                                            name="lname"
                                            :state="getValidationState(errors)">
                            </b-form-input>
                            <b-form-invalid-feedback>
                                {{ errors[0] }}
                            </b-form-invalid-feedback>
                            </validation-provider>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col class="mb-2 c-box" xl="6" md="6" sm="12">
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
                    
                        <b-col class="mb-2 c-box" xl="6" md="6" sm="12">
                            <validation-provider
                            v-slot="{ errors }"
                            rules="required"
                            name="customer phone number"
                            >
                            <label for="phone">Phone Number</label>
                            <b-form-input v-model="form.phone"
                                            type="number"
                                            id="phone"
                                            name="phone"
                                            :state="getValidationState(errors)">
                            </b-form-input>
                            <b-form-invalid-feedback>
                                {{ errors[0] }}
                            </b-form-invalid-feedback>
                            </validation-provider>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col class="mb-2 c-box" xl="6" md="6" sm="12">
                            <validation-provider
                                v-slot="{ errors }"
                                rules="required"
                                name="customer message"
                            >
                            <label for="message">Message</label>
                            <b-form-textarea v-model="form.message"
                                            type="text"
                                            id="message"
                                            name="message"
                                            rows="3"
                                            max-rows="10"
                                            :state="getValidationState(errors)">
                            </b-form-textarea>
                            <b-form-invalid-feedback>
                                {{ errors[0] }}
                            </b-form-invalid-feedback>
                            </validation-provider>
                        </b-col>
                    </b-row>
                    
                    <b-row>
                        <b-col cols="12" class="text-right my-2">
                            <b-button type="submit" class="submitbtn">Submit</b-button>
                            <button type="button" class="btn btn-outline-danger" @click="resetForm()">Reset</button>
                        </b-col>
                    </b-row>
        <div class="conatainer">
            <!-- contact section -->
            <div class="contact">
                <h2>Contact us!</h2>
                <p>Contact us today, and get reply with in 24 hours!</p>

                <form id="contact" action="" method="post">
                    <fieldset>
                        <label for="name">Full Name</label>
                        <input placeholder="" type="text" tabindex="1" required autofocus>
                    </fieldset>
                    <fieldset>
                        <label for="mail">Email Address</label>
                        <input placeholder="" type="email" tabindex="2" required>
                    </fieldset>
                    <fieldset>
                        <label for="num">Phone Number</label>
                        <input placeholder="" type="tel" tabindex="3" required>
                    </fieldset>
                    <fieldset>
                        <label for="message">Message</label>
                        <textarea placeholder="" tabindex="5" required></textarea>
                    </fieldset>
                    <fieldset>
                        <button name="submit" type="submit" id="contact-submit" data-submit="...Sending">Submit</button>
                    </fieldset>

                </form>
                </validation-observer>
            </b-container>
        </b-col>
    </div>
</template>

<script>

import {ValidationObserver, ValidationProvider} from "vee-validate";
export default {
    name: 'Contact',
    layout:'WebsiteLayout',
    components: {
        ValidationProvider,
        ValidationObserver,
    },
    head(){
          return{
              title: 'Contact Us'
          }
        },
    data() {
        return {
            token: '',
            image: "boutique",
            items: {
                address:"Montego Bay, Jamaica",
                phone: "(876)971-1234",
                email: "monique.boutique@gmail.com"
            },
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
            /* ADD busID - form_data.append() */

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
</script>

<style scoped>
.wrapper{
    margin: 2em;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
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
.submitbtn{
    background-color: white;
    color: rgb(37, 167, 117);
    border-color: rgb(37, 167, 117);
}
</style>