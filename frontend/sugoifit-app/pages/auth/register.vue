<template>
    
    <div class=" w-100 h-100 ">
    
        <div class="d-flex flex-row ">
            <div  class="login-div">
                <img class = "login-image " src="~assets/uploads/login.svg" alt="">
            </div>
            
            <div class="container  w-50 d-flex flex-column">
                    <div class = "d-flex flex-column ">
                        <h2 class ="text-center"> Register </h2>   
                        <div id="d-flex justify-content-center">               
                            <p class ="login-text text-center"> Welcome back, enter your username and password</p>
                        </div>
                        <div class = "d-flex flex-row justify-content-center">
                            <form id = "RegisterForm" class ="d-flex ml-3 flex-column " @submit.prevent = "LoginUser" method ="POST">
                                <input type="hidden" name="_token" :value="token">
                            
                                <label class ="form-label mt-4" for="first_name"> First Name</label> 
                                <input class ="form-control mt-2" type="text" name="first_name" id="first_name">

                                <label class ="form-label mt-4" for="last_name"> Last Name</label> 
                                <input class ="form-control mt-2" type="text" name="last_name" id="last_name">

                                <label class =" form-label text-left" for ="email">Email:</label>
                                <input class ="form-control mt-2" type="text" name="email" id="email">
                            
                                <label class ="form-label mt-4" for="password"> Password:</label> 
                                <input class ="form-control mt-2" type="password" name="password" id="password">

                                <label class ="form-label mt-4" for="business_name">Business Name</label> 
                                <input class ="form-control mt-2" type="text" name="business_name" id="business_name">
                            
                                <div class ="d-flex flex-column align-items-center">
                                    <div  id="msgBox">
                                        <p> {Display error messages here} </p>
                                    </div>
                                    <button  class="btn submit" id="submit"> Submit </button>
                                    <p class ="login-text m-3">Dont have an account? <a href="">Sign up your business! </a></p>
                                </div>
                            </form>
                        </div>
                    </div>

                    
                       
                    
                    
            </div> 
        </div>  
    </div>
</template>

<script>
import sfNavBar from '../../components/sf-nav-bar.vue'

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
            // this.$router.push({name: 'index'});
        },
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
    .login-page{
        width: 100%; 
        min-height: 100%;
        display:flex;
        justify-content: center;
        align-items: center;
       
        /* background-color: green; */
    }
    .login-text{
        font:400 1rem "Poppins";
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
        font:400 1rem "Poppins";
    }
   
    #RegisterForm input{
        width: 24rem;
        height: 2.7rem;
        border-radius: 20px;
        box-shadow: 1px 2px 12px #d6d8d8;

    }

    .form-container{
        width:50vw;
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
        width:50vw;

    }
      #RegisterForm input{
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

    #RegisterForm input{
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
    #RegisterForm{
        width:50%;
    }

  
    #RegisterForm input{
        width: 32rem;
        display: flex; 
        /* justify-content: center; */
        align-items: center;
    }

    .login-image{
        /* background: #428B95; */
        width:100%;
    }

    
}
</style>