<template>
    <div class="m-0 d-flex flex-row w-100 ">
        <onboarding-side  class = "side-bar m-0"></onboarding-side>
        <div class="main-area d-flex flex-column">
            <email-section v-if ="secfocus" ></email-section>
                <!--  COMPANY TYPE-->
                <div v-else-if = "secfocusN" class="company-type-section m-4" >
                    <div>
                        <h4 class="font-bold m-4">Choose the type of business</h4>
                        <p class="m-4">Choose the option that best describes your business.</p>
                    </div>

                </div>

            <!--  BUSINESS LOCATION + BASIC ADDRESS-->
            <div v-else class="business-detail-sec">
                    <div class="text">SHEJJK</div>
            </div>
            <!-- <button @click= "ChangeSection" class="btn btn-lg bg-primary w-25 justify-content-center">
                Next
            </button> -->
        </div>
    </div>
</template>


<script>
import EmailSection from '../components/onboarding/email-section.vue'
import OnboardingSide from '../components/onboarding/onboarding-side.vue'
export default {
  components: { OnboardingSide, EmailSection },
    name: 'on-boarding',
    data(){
    return{
        secfocus: false,
        secfocusN: true

    }
}, 
methods: {
    ChangeSection: function(){
        // this.secfocus = false;


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
        width: 100vw;
        height:100vh;
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
    .side-bar{ 
        display:none;
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
    }
}

/* Large devices (laptops/desktops, 992px and up) */
@media only screen and (min-width: 992px) {
    .color-bg{
        /* background-color: red; */
    }
}

/* Extra large devices (large laptops and desktops, 1200px and up) */
@media only screen and (min-width: 1200px) {
    .color-bg{
        /* background-color: blue; */
    }
   
}
</style>