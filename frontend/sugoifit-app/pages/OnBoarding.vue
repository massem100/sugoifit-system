<template>
    <div class="m-0 d-flex flex-row w-100 ">
        <div v-if= "form_toggle" class="main-area d-flex flex-column">
            <img src="~assets/uploads/onboard-img.svg" alt="" class="onboard-img ">
            <div class = "onboard-container d-flex flex-column align-items-center ">
                <p class="onboard-p">Click to begin setting up your business.</p>
                <button @click = "GetStarted" class="onboard-btn btn btn-sm justify-content-center">
                         Get Started
                </button>
            </div>
        </div>
        
        <b-form> 
            
            <email-section></email-section>
            <corporation></corporation>

        </b-form>
     
    </div>
   
</template>


<script>
import EmailSection from './onboarding/email-section';
// import EmailSection from './onboarding/firstStep';
import Corporation from './onboarding/business-details/corporation.vue';

export default {
  components: {
    EmailSection,
    Corporation
 
    },
    name: 'on-boarding',
    layout: 'onboarding',
    data(){
        return{
            secfocus: true,
            secfocusN: true, 
            form_toggle: true,

        }
}, 
methods: {
    GetStarted: function(){
        this.form_toggle = false;
    }
    }
}

</script>

<style scoped>
    .side-bar{ 
        display:none;

    }
    .icon-placeholder{
        width:5rem;
        height: 5rem;
    }

    .company-options{
        margin:40px;
        padding:10px;
        display:flex; 
        flex-direction: row;
        width: 8rem; 
        height:2rem;
    }

    .company-type-section{
        margin-top: 2rem;
        height:100vh;
    }

    .main-area{
        /* background-color: aquamarine; */
        display:flex;
        flex-direction: column;
        /* justify-content:flex-start; */
        /* align-items: center; */
        margin-left: 10rem;
        width: 100vw;
        height:100vh;
    }
    .onboard-p{
        margin-top: 2rem;
        /* margin-left: 0.2rem; */
        /* position:absolute; 
        top:24rem; 
        left: 6rem; */
        z-index: 2; 
        text-align: center;
        font: 400 0.8rem "Poppins"; 
    
        /* width: 4rem; */
    }

    .onboard-btn{
        /* position:absolute; 
        top:24rem; 
        right: 13rem;
        z-index: 2;  */
        display: flex;
        justify-content: center;
        align-items: center;
        width: 8rem; 
        height: 3rem;
               
        background-color: rgb(79, 201, 218,0.5);
        box-shadow: 0 2px 2px 0 rgba(107, 104, 104, 0.15), 0 6px 20px 0 rgba(119, 114, 114, 0.15);
    
    }
    .onboard-img{
        width: 100vw;
    }
    /* Extra small devices (phones, 600px and down) */
@media only screen and (max-width: 600px) {
    .color-bg{
        /* background-color: green; */
    }
    .side-bar{ 
        display:none;
    }


}

/* Small devices (portrait tablets and large phones, 600px and up) */
@media only screen and (min-width: 600px) {
    .color-bg{
        /* background-color: purple; */
    }
    
}

/* Medium devices (landscape tablets, 768px and up) */
@media only screen and (min-width: 768px) {
    .color-bg{
        /* background-color: yellow; */
    }
    .side-bar{ 
        display:block;
        z-index: 1; 
        height: 100%;

    }

    
}

/* Large devices (laptops/desktops, 992px and up) */
@media only screen and (min-width: 992px) {
    .color-bg{
        background-color: red;
    }

    .onboard-btn{
        margin-top: -2px;
    }

    .onboard-p{
        margin-top: 2px;
    }
}

/* Extra large devices (large laptops and desktops, 1200px and up) */
@media only screen and (min-width: 1200px) {
    .color-bg{
        background-color: blue;
    }
     .onboard-p{
        margin-left: 0.2rem;
        position:absolute; 
        top:20rem; 
        right: 4rem;
        z-index: 2; 
        text-align: center;
        font: 400 0.8rem "Poppins"; 
    
        /* width: 4rem; */
    }

    .onboard-btn{
        position:absolute; 
        top:22rem; 
        right: 8rem;
        z-index: 2; 

        width: 8rem; 
        height: 3rem;
        
        background-color: rgb(79, 201, 218,0.5);
        box-shadow: 0 2px 2px 0 rgba(107, 104, 104, 0.15), 0 6px 20px 0 rgba(119, 114, 114, 0.15);
    
    }

    .onboard-img{
        max-height:100vh;
    }
}
</style>