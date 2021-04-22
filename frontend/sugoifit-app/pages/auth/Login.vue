<template>
    
    <div class="d-flex flex-column justify-content-center bg-white w-100 h-100">
        <b-alert class = "alert-comp mt-5 p-4 text-primary" v-if = "alert_message" variant="success" dismissible show>
                    <p class = "d-flex flex-row justify-content-center text-white">{{alert_message}}</p>
        </b-alert>
        <div class="d-flex flex-column align-items-center justify-content-center h-100 ">
            <h2 class ="text-center"> Login </h2>                
            <p class ="text-center"> Welcome back, enter your username and password</p>
            
            <b-form id = "LoginForm" class ="h-100" @submit.prevent = "LoginUser" method ="POST">
                <!-- <b-form-input type="hidden" name="_token" :value="token"> -->
            
                <label class =" form-label text-left" for ="email">Email:</label>
                <b-form-input class ="form-control mt-2" type="text" name="email" id="email"></b-form-input>
            
                <label class ="form-label mt-4" for="password"> Password:</label> 
                <b-form-input class ="form-control mt-2" type="password" name="password" id="password"></b-form-input>
            
                <div class ="d-flex flex-column align-items-center">
                    <div  id="msgBox">
                        <p> {{alert_message}} </p>
                    </div>
                    <button  style = "background-color: #7CC3CD;" class="btn submit text-white" id="submit"> Submit </button>
                    <p class ="login-text m-3">Dont have an account? <nuxt-link :to="{name:'auth-register'}">Sign up your business! </nuxt-link></p>
                </div>
            </b-form>
        
                
        </div> 
    
    
    </div>
</template>

<script>


export default {
  components: { },
    name: 'auth-login',
    head(){
    return{
    //   meta: [{
    //         name:"csrf-token",
    //         content: "{{ csrf_token()}}"
    //   }
                
    
    //   ]
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
                        console.log(res.data);
                        if (res.data.message){
                            this.alert_message = res.data.message;
                            setTimeout(function(){
                                router.push({name: 'dashboard'});
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
