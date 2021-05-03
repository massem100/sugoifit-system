<template>
    
    <b-col class="d-flex flex-column justify-content-center align-items-center w-100 h-100">
        <base-alert v-if= "alert_message" 
                    class = "mt-5 d-flex flex-row justify-content-center" 
                    style="width: 25rem; 
                           height: 3rem; " 
                    dismissible      
                    type= "primary">{{alert_message}}
        </base-alert>
        <b-col class="d-flex flex-column align-items-center justify-content-center mt-5 h-100 ">
            <h2 class ="text-center"> Login </h2>                
            <p class ="text-center"> Welcome back, enter your username and password</p>
            
            <b-form id = "LoginForm" 
                    class ="h-100  w-25 d-flex flex-column " 
                    @submit.prevent = "LoginUser" 
                    method ="POST">
             
            
                <label class =" form-label text-left" 
                       for ="email">Email:
                </label>
                <b-form-input class ="form-control mt-2" 
                              type="text" 
                              name="email" 
                              id="email">
                </b-form-input>
            
                <label class ="form-label mt-4" 
                       for="password"> Password:</label> 
                <b-form-input class ="form-control mt-2" 
                              type="password" 
                              name="password" 
                              id="password">
                </b-form-input>
            
                <b-col class =" align-items-center">
                    <div  id="msgBox">
                        <p> {{alert_message}} </p>
                    </div>
                    <button  style = "background-color: #7CC3CD;" 
                             class="d-flex flex-row justify-content-center btn submit text-white" 
                             id="submit"> 
                             Submit 
                    </button>
                    <p class ="login-text m-3">Dont have an account? 
                        <nuxt-link :to="{name:'auth-register'}">Sign up your business! </nuxt-link>
                    </p>
                </b-col>
            </b-form>
        
                
        </b-col> 
    
    
    </b-col>
</template>

<script>
import BaseAlert from '../../components/argon-core/BaseAlert.vue';


export default {
  components: {BaseAlert },
    name: 'auth-login',
    head(){
    return{
 
    }
  },
  mounted(){
      
     
  },
    data(){
        return{
           token: '', 
           alert_message: ''
           
        }

    }, 
    methods:{
        LoginUser: function () {
            let self = this;
            let loginForm = document.getElementById("LoginForm");
            let form_data = new FormData(loginForm);
            form_data.append('form id', loginForm.getAttribute("id"));
            let PATH_API = 'auth/login';
                this.$axios({
                    method: "POST",
                    headers:{
                        'Content-Type': 'application/json',
                    },
                    url: `/api/${PATH_API}`,
                    data: form_data,
                    }).then (res => {
                        if (res.data.success["0"].message){
                            this.alert_message = res.data.success["0"].message;
                            var userid = res.data.success["0"].userid;
                            let jwt_token = res.data.success["0"].token;
                            localStorage.setItem("token", jwt_token);
                            localStorage.setItem("userid", userid);
                            console.info("Token generated and added to localStorage.");
                            self.token = jwt_token;
                            setTimeout(function(){
                                $nuxt.$router.push({name: 'index'});
                            }, 1000);

                        }else{

                        }
                    }), error =>{
                        console.log(error);
                    }
                    }
    }
    }

</script>

<style scoped>

</style>
