<template>
    <div class="business-page"> 
        <onboarding-side class = "side-bar m-0 h-100 "> </onboarding-side>

        <div class="business-main">
            <div class="business-heading">
                <h5> Business Details </h5>
                <p> Help us personalize your experience by providing some details about your business.</p>
            </div>

            <div class="business-form-div">
                <b-form action="" class="business-form">
                    <!--
                    Type of Business , 
                    Business Industry -->
                    <div class="business-form-item">
                        <label for = "corp_type">Type of corporation</label>
                        <b-form-select aria-placeholder="Select business type." id = corp_type :options="corp_types"> </b-form-select>
                        
                        <!-- <div class="alert alert-info mt-4" role="alert">
                            This is a info alert—check it out!
                        </div> -->
                    </div>
                    
                    <div class="shares-div "> 
                        <div class = "business-form-item"> 
                            <label for = ""> Number of Shares </label>
                            <b-form-input placeholder="Standard: 10000" id = ""></b-form-input>
                        </div>
                        <div class="business-form-item">
                            <label for = ""> Per value </label>
                            <b-form-input placeholder= "Cost per share" id = ""></b-form-input>
                        </div>
                    </div>
                        <div class="business-form-item">
                            <label for="industry"> Industry</label>
                            <b-form-input placeholder="e.g Technology / Finance"
                             id = "industry"></b-form-input>
                        </div>

                       <button @click="AboutComp" type="button" class="btn bus-btn ">Next</button>
                </b-form>
            </div>


        </div>
    </div>
    
</template>


<script > 
import onboardingSide from '../../../components/onboarding-side.vue'
export default{
  components: { onboardingSide },
    name: 'BusinessDetails', 
    data() { 
        return { 
            corp_types: 
                    [
                        {value : null, text: 'Please select your type of incorporation.'},
                        {value : 'a', text: 'Private Company '},
                        {value : 'b', text: 'Unlimited Liability Company'},
                        {value : 'c', text: 'Limited Liability Company'}
                    ]
        }
    },
    methods: {
        AboutComp: function(){
            this.$router.push("aboutbusiness");

        }
    }
}

</script>

<style scoped>
    .business-page{

        display: flex;
        flex-direction: row;
        
    }

    .side-bar{
        display:none;
    }
    .business-main{
        margin: 2rem;
        margin-top: 4rem;
        font: 400 1rem "Poppins";

    }

    .business-heading p{ 
        margin: 2rem 0;
        
        font: 400 1rem "Poppins";

    }
    .shares-div{
        display: flex;
        flex-direction: row;
        width: 26rem;
    

    }
    .shares-div .business-form-item{
        margin-right: 1rem;
    }
    .shares-div b-form-input{
        margin-right: 1rem;
        
    }

    .business-heading h5{ 
        font: 600 1.8rem "Poppins";
    }

    .business-form bus-btn{
        display: flex;
        justify-content: center;
        

    }
    .business-form-item{ 
        margin: 1rem 0;
        width: 25rem;
    }

    .business-form-div{
        display: flex;
        flex-direction: column;
        /* justify-content: center; */
        align-items: center;
    }

    .bus-btn{
        display: flex; 
        flex-direction: row;
        justify-self: center;
        background-color: #A7E4EC;
        width: 6rem;
        text-align: center;
    }


    /* Extra small devices (phones, 600px and down) */
    @media only screen and (max-width: 600px) {
        
    }
/* Small devices (portrait tablets and large phones, 600px and up) */
    @media only screen and (min-width: 600px) {
        .business-heading p{
            width: 26rem;
        }
    }
/* Medium devices (landscape tablets, 768px and up) */
    @media only screen and (min-width: 768px) {
        .side-bar{
            display:block;
            position:fixed;
        
        }

        .business-main{
            margin-left: 20rem;
        }

        
    }
    /* Large devices (laptops/desktops, 992px and up) */
    @media only screen and (min-width: 992px) {
        
    }
    /* Extra large devices (large laptops and desktops, 1200px and up) */
    @media only screen and (min-width: 1200px) {
        
    }
   

   
</style>