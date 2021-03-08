<template>
    
    <div id ="login-page" class="d-flex flex-column justify-content-center align-items-center">
        <!-- Add nav component here -->
        <sf-nav-bar class="w-100"/>

        <div class="d-flex flex-row m-4 w-100 justify-content-center align-items-center">
            <div  class="login-image d-flex  w-50 justify-content-center">
                <LoginImage  class=" m-0 "/>
            </div>
            
            <div id ="main-area" class="d-flex flex-column  w-50 p-4">
                    <div class = "d-flex flex-column justify-content-start">
                        <h2 class ="text-center"> Login </h2>   
                        <div id="login-text-div d-flex justify-content-center">               
                            <p class ="login-text text-center"> Welcome back, enter your username and password</p>
                        </div>
                    </div>
                    <div class="d-flex justify-content-center m-3">
                        <form id = "LoginForm" class ="d-flex flex-column" method ="POST">
                            <input type="hidden" name="_token" :value="token">
                            <label class ="text-left" for ="email">Email:</label>
                            <input class ="mt-2" type="text" name="email" id="email">
                        
                            <label class ="mt-4" for="password"> Password:</label> 
                            <input class ="mt-2" type="text" name="password" id="password">
                            <div class ="d-flex flex-column align-items-center">
                                 <!-- <div  id="msgBox">
                            <p> {Display error messages here} </p>
                        </div> -->
                                <button class="btn submit" id="submit"> Submit </button>
                                <p class ="m-3">Dont have an account? <a href="">Sign up your business! </a></p>
                             </div>
                        </form>
                    </div>
                    
            </div> 
        </div>  
    </div>
</template>

<script>
import sfNavBar from '../components/sf-nav-bar.vue'

export default {
  components: { sfNavBar },
    name: 'Login',
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
           token: ''
           
        }

    }, 
    methods:{
    }
}

</script>

<style scoped>
    #login-page{
        width:100%;
        height: 70%;

    }

    #main-area{
        justify-content: center;
        align-content: center;
        padding: 16px;
        margin: 24px;
        
    }
    #login-text-div{
        width: 200px;
        
    }
    .login-text{
        font:200 1rem "Poppins";

    }
    input[type=text], input[type=password] {
        align-content: center;
        width: 20rem;
        height: 45px;
        left: 392px;
        top: 171px;
        border: none;
        background: #f3f2f2;
        border-radius: 80px;
        
    }

    .submit{
        display:flex;
        width: 10rem;
        height:4rem;
        background-color: #f3f2f2;
        border-radius: 80px;
        justify-content: center;
        align-items: center;
       
    }
    #msgBox{
        margin-top:16px;
    }
</style>