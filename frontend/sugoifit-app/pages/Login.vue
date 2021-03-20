<template>
    
    <div class=" login-page">
        <!-- Add nav component here -->
        <!-- <sf-nav-bar class="w-100"/> -->

        <div class="w-100 d-flex flex-row ">
            <div  class="login-div">
                
                <img class = "login-image" src="~assets/uploads/login.svg" alt="">
            </div>
            
            <div class="form-container">
                    <div class = "d-flex flex-column justify-content-start">
                        <h2 class ="text-center"> Login </h2>   
                        <div id="d-flex justify-content-center">               
                            <p class ="login-text tcext-center"> Welcome back, enter your username and password</p>
                        </div>
                    </div>
                    <div class="d-flex justify-content-center m-3">
                        <form id = "LoginForm" class ="d-flex flex-column" @submit.prevent = "LoginUser " method ="POST">
                            <input type="hidden" name="_token" :value="token">
                           
                            <label class =" form-label text-left" for ="email">Email:</label>
                            <input class ="form-control mt-2" type="text" name="email" id="email">
                        
                            <label class ="form-label mt-4" for="password"> Password:</label> 
                            <input class ="form-control mt-2" type="text" name="password" id="password">
                           
                            <div class ="d-flex flex-column align-items-center">
                                <div  id="msgBox">
                                    <p> {Display error messages here} </p>
                                </div>
                                <button @click= "ChangeRoute" class="btn submit" id="submit"> Submit </button>
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
        ChangeRoute: function(){
            this.$router.push({name: 'index'});
        },
        LoginUser: function () {
      let self = this;
      let loginForm = document.getElementById("LoginForm");
      let form_data = new FormData(loginForm);
      fetch("http://localhost:8080/api/auth/login", {
        method: "POST",
        body: form_data,
        headers: {
          "X-CSRFToken": token,
        },
        credentials: "same-origin",
       })
        .then(function (response) {
          return response.json();
      })
      .then(function (jsonResponse){
            console.log("working");
      }).catch(function (error) {
          console.log(error);
        });

    }
    }
    }

</script>

<style scoped>
    .login-page{
        width: 100%; 
        height: 100vh;
        display:flex;
        justify-content: center;
        align-items: center;
        /* background-color: green; */
    }
    .login-text{
        font:200 0.6rem;
    }
    .login-image{
        margin: 0.8;
        width: 40rem;
        /* background-color: navy; */
        display: none;
    }   
  
    .submit{
        display:flex;
        width: 10rem;
        height: 3rem;
        background-color: #428B95;
        border-radius: 80px;
        justify-content: center;
        align-items: center;
        text-align: center;
        color: white;
       
    }
    #msgBox{
        margin-top:16px;
    }
   
    #LoginForm input{
        width: 24rem;
        height: 2.7rem;
        border-radius: 20px;
        box-shadow: 1px 2px 12px #d6d8d8;

    }

    .form-container{
          width:50rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
      /* Extra small devices (phones, 600px and down)
@media only screen and (max-width: 600px) {
    .login-page{
        background-color: green;
    }
    

} */

/* Small devices (portrait tablets and large phones, 600px and up) */
@media only screen and (min-width: 600px) {
  
    .login-page{
        /* background-color: purple; */
        width: 100%; 
        height: 100vh;
        display:flex; 
        flex-direction: column;
        justify-content: center;
        align-items: center;
        /* background-color: green; */
    }
    .form-container{
        margin: 2rem;
        /* background-color: beige; */
        display:flex; 
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
}

/* Medium devices (landscape tablets, 768px and up) */
@media only screen and (min-width: 768px) {
    .login-page{
        /* background-color: yellow; */
    }

    .login-div{
        margin: 1rem;
        /* background-color: beige; */
        display:flex;
        justify-content: center;  
        align-items: center;
    }
    
    .login-image{
        margin: 1rem;
        /* padding: 20px; */
        display: block;
        width: 50vw;
        height: 80vh;
    }
    
    .form-container{
        /* background-color: #428B95; */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 10px;
        width: 40vw;

    }
      #LoginForm input{
        width: 18rem;
        height: 2.4rem;
        border-radius: 20px;
        box-shadow: 1px 2px 12px #d6d8d8;
      
      }

      .login-text{
          font-size: 0.8rem;
          margin: 10px;
          text-align: center;
      }
}

/* Large devices (laptops/desktops, 992px and up) */
@media only screen and (min-width: 992px) {
    .login-page{
        /* background-color: red; */
    }

    #LoginForm input{
        width: 24rem;
    }
    .login-image{
         margin: 1rem;
        /* padding: 20px; */
        display: block;
        width: 30rem;
        /* height: 80vh; */
    }

    .login-text{
         font-size: 1rem;
         margin: 10px;
         text-align:center;

    }
}

/* Extra large devices (large laptops and desktops, 1200px and up) */
@media only screen and (min-width: 1200px) {
    .login-page{
        /* background-color: blue; */
        
    }

    .form-container{
        /* background-color: tomato; */
        width:50vw; 
        height: 100vh;
    }

    .login-div{
        width: 50vw;
        height:100vh;
        /* background-color: gold; */
    }
    #loginForm input{
        width: 32rem;
    }

    .login-image{
        /* background: #428B95; */
        width:100%;
    }

    
}
</style>