<template> 
    <div class=" w-100 h-100 bg-white">
        <div class="container d-flex flex-column align-items-center">
            
            <h2 class ="text-center"> Register </h2>   
            <p class ="login-text text-center"> Welcome back, enter your username and password</p>
            
            <b-form id = "RegisterForm" class ="d-flex flex-column  " @submit.prevent = "LoginUser" method ="POST">                        
                <label class ="form-label mt-4" for="first_name"> First Name</label> 
                <b-form-input class ="form-control mt-2" type="text" name="first_name" id="first_name"></b-form-input>

                <label class ="form-label mt-4" for="last_name"> Last Name</label> 
                <b-form-input class ="form-control mt-2" type="text" name="last_name" id="last_name"></b-form-input>

                <label class =" form-label text-left mt-4" for ="email">Email:</label>
                <b-form-input class ="form-control mt-2" type="text" name="email" id="email"></b-form-input>
            
                <label class ="form-label mt-4" for="password"> Password:</label> 
                <b-form-input class ="form-control mt-2" type="password" name="password" id="password"></b-form-input>

                <label class ="form-label mt-4" for="business_name">Business Name</label> 
                <b-form-input class ="form-control mt-2" type="text" name="business_name" id="business_name"></b-form-input>
            
                <div class ="d-flex flex-column align-items-center">
                    <div  id="msgBox">
                        <p> {Display error messages here} </p>
                    </div>
                    <button  class="btn submit" id="submit"> Submit </button>
                    <p class ="login-text m-3">Already have an account? <nuxt-link :to="{name:'auth-Login'}"> Login here. </nuxt-link></p>
                </div>
            </b-form>
                
            </div>      
    </div>
</template>

<script>

export default {
  components: { },
    name: 'auth-register',
    head(){
        return{}
  },
  mounted(){
  },
    data(){
        return{
           token: ''
        }
    }, 
    methods:{
        LoginUser: function () {
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
                return jsonResponse.json();
              })
              .then( jsonResponse =>{
                console.log(jsonResponse);
              })
            }, 
                    
    }
    }

</script>

<style scoped>
   button{
       background-color: #7CC3CD;
   }
</style>