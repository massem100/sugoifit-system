<template>
    <div class="m-0 d-flex flex-row ">
        <onboarding-side class = "side-bar m-0"></onboarding-side>
        <!--  COMPANY TYPE-->
        <div class="company-type-section">
            
            <div>
                <h2 class="font-bold m-4">Choose the type of business</h2>
                <p class="m-4">Choose the option that best describes your business.</p>
            </div>
        </div>

        <!--  BUSINESS LOCATION + BASIC ADDRESS-->
    </div>
</template>


<script>
import OnboardingSide from '../components/onboarding/onboarding-side.vue'
export default {
  components: { OnboardingSide },
    name: 'on-boarding',
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