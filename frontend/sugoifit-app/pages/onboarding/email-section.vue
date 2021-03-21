<template>
<div class="d-flex flex-row w-100 color-bg"> 
    <onboarding-side class = "side-bar h-100 m-0"></onboarding-side>

     <div class="email-create-section w-100" >
                
                <div class="email-form-section  d-flex flex-column">
                    <div class = "email-heading">
                        <h4 class ="mb-4">Set up your Business Profile.</h4>
                        <p class="email-text mb-5"> Managing your business has never been this easy. <br>
                            Enter your business email address to continue. 
                        </p>
                    </div>
                    <div class = "email-container  ml-3">
                        <form action="" class="email-form ">
                                <label class ="d-flex text-center align-items-center" for="email">Email Address</label>
                                <input type="text" name ="email" class="form-control" >
                        </form>
                        <div @click ="ChangeComp" class="get-started btn btn-sm ">Get Started <span></span></div>
                    </div>

                </div>
                <div class="w-40">
                    <img class="business-image" src="~assets/uploads/business_board.jpg" alt="">
                    <img class="doodle" src="~assets/uploads/linecurve.svg" alt="">
                </div>
            </div>
    </div>
</template>



<script>
import OnboardingSide from '/components/onboarding-side.vue';

export default {
    components: {OnboardingSide},
    name: 'email-section', 
    data(){
        return{

        }
    }, 
    methods: {
        ChangeComp: function() {
           this.$router.push('company-type');
        //    this.nuxt.$options.router.push({path: this.localePath('company-type')});
        }
    }
    
}
</script>



<style scoped>
    
    .email-create-section{
        margin-top: 8rem;
        margin-left: 2rem;
        display: flex;
        flex-direction: row;
        min-height:100vh;
           }
    .business-image{
        margin-left: 2rem;
        width: 28rem;
        height: 24rem;
        border-radius: 20px;
    }
    
    .email-form-section{
        /* display: flex; */
    }
      .email-heading{
        margin: 20px 20px 20px 20px;

        font: 400 1rem "Poppins";
    }

    .email-container{
        display: flex;
        flex-direction: row;
        /* justify-content: center; */
        align-items: center;
    
    }
    .email-form{
       
        display: flex;
        flex-direction:column;
    }
    .email-form input{
        width: 12rem;
        margin: 10px;
       
    }
    .email-form label{
        margin:10px;
    }
    .get-started{
        display: flex;
        margin-top: 2.8rem;
        width: 8rem;
        height: 3rem;
        align-items:center;
        justify-content: center;
        background-color: #4DC4D4;
        color:white;
    }

    .doodle{
        position:absolute;
        right: 0; 
        top: 32rem;
        z-index: 1; 
        overflow: hidden;   
        width: 42rem;
        
    }
    
    /* Extra small devices (phones, 600px and down) */
@media only screen and (max-width: 600px) {
    .color-bg{
        /* background-color: green; */
    }
    .side-bar{ 
        display:none;
    }

    .business-image{
        display: none;
    }
}

/* Small devices (portrait tablets and large phones, 600px and up) */
@media only screen and (min-width: 600px) {
    /* .color-bg{
        background-color: purple;
    } */
    .side-bar{ 
        display:none;
    }
    .business-image{
        display: none;
    }
    .email-create-section{
        /* align-items: center; */
        justify-content: center ;
    }
    
}

/* Medium devices (landscape tablets, 768px and up) */
@media only screen and (min-width: 768px) {
    .color-bg{
        /* background-color: yellow; */
    }
    .side-bar{ 
        display:block;
    }
     .business-image{
        display: none;

    }

}

/* Large devices (laptops/desktops, 992px and up) */
@media only screen and (min-width: 992px) {
    .color-bg{
        /* background-color: red; */
    }
     .business-image{
        display: block;
        margin-right:10px;
        width: 24rem;
        height: 22rem;
        overflow: hidden;

    }
    
}

/* Extra large devices (large laptops and desktops, 1200px and up) */
@media only screen and (min-width: 1200px) {
    .color-bg{
        /* background-color: blue; */
    }
    .business-image{
        margin-left: 4rem;
        margin-right: 0px;
        z-index: 2;
    }

    .doodle{
        position:absolute;
        right: 0; 
        top: 28rem;
        z-index: 1; 
        overflow: hidden;   
        width: 42rem;
        
    }
    .email-form input{
        width: 16rem;
        margin: 10px;
       
    }
}
</style>