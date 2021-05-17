<template> 
    <b-col class=" w-100 h-100 bg-white">
      <base-alert v-if= "alert_message" 
                    class = "mt-5 d-flex flex-row justify-content-center" 
                    style="width: 25rem; 
                           height: 3rem; " 
                    dismissible      
                    type= "primary">{{alert_message}}
        </base-alert>
        <b-col class="container d-flex flex-column align-items-center">
            <h2 class ="text-center"> Register </h2>   
            <p class ="login-text text-center"> Welcome back, enter your username and password</p>
            
            <b-form id = "RegisterForm" class ="d-flex flex-column  " @submit.prevent = "RegisterUser" method ="POST">                        
                <label class ="form-label mt-4" for="first_name"> First Name
                  <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="eg. Jess"/></label> 
                <b-form-input class ="form-control mt-2" type="text" name="first_name" id="first_name"></b-form-input>

                <label class ="form-label mt-4" for="last_name"> Last Name
                  <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="eg. Reid"/></label> 
                <b-form-input class ="form-control mt-2" type="text" name="last_name" id="last_name"></b-form-input>

                <label class =" form-label text-left mt-4" for ="email">Email:
                  <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="Company email eg. compemail@outlook.com"/>
                </label>
                <b-form-input class ="form-control mt-2" type="text" name="email" id="email"></b-form-input>
            
                <label class ="form-label mt-4" for="password"> Password:</label> 
                <b-form-input class ="form-control mt-2" type="password" name="password" id="password"></b-form-input>

                <label class ="form-label mt-4" for="business_name">Business Name
                  <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="eg. Monique's Boutique"/></label> 
                <b-form-input class ="form-control mt-2" type="text" name="business_name" id="business_name"></b-form-input>
            
                <b-col class ="d-flex flex-column align-items-center">
                    <div  id="msgBox" v-show="show">
                        <p> {Display error messages here} </p>
                    </div>
                    <button  class="btn submit" id="submit"> Submit </button>
                    <p class ="login-text m-3">Already have an account? <nuxt-link :to="{name:'auth-Login'}"> Login here. </nuxt-link></p>
                </b-col>
            </b-form>
                
            </b-col>      
    </b-col>
</template>

<script>
import BaseAlert from '../../components/argon-core/BaseAlert.vue';
export default {
  components: {BaseAlert },
    name: 'auth-register',
    head(){
      return{
          title: 'Register'
      }
  },
  mounted(){
  },
    data(){
        return{
          show=false,
          token: '', 
          alert_message: ''
        }
    }, 
    methods:{
        RegisterUser: function () {
            let self = this;
            let regForm = document.getElementById("RegisterForm");
            let form_data = new FormData(regForm);
            form_data.append('form id', regForm.getAttribute("id"));
            let PATH_API = 'users/register';
                this.$axios.post(`/api/${PATH_API}`, form_data, {
                  headers: {
                  'contentType': 'application/json',
                }
              })
              .then( jsonResponse =>{
                return jsonResponse.data;
              })
              .then( jsonResponse =>{
                console.log(jsonResponse);
                self.alert_message = jsonResponse.message;
              })
        }, 
        error: function () {
          if (this.alert_message === ) {
            show= true;
          }

        }
                    
    }
    }

</script>

<style scoped>
   button{
       background-color: #7CC3CD;
   }
</style>