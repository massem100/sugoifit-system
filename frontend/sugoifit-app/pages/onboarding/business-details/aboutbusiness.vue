<template>
    <div class="about-business-page "> 
        <div class="about-business-main">
            <div class="about-business-heading">
                <h5> About your business </h5>
                <p> Help us personalize your experience by providing some details about your business.</p>
            </div>

            <div class="about-business-form-div">
                <validation-observer ref="observer" v-slot="{}">
                <!-- <b-form action="" class="about-business-form"> -->
                    <div class="about-business-form-item">
                        <label for = "comp-name">Company Name</label>
                        <div class="name-container d-flex flex-row">
                            <validation-provider v-slot="{ errors }" rules="required" name="comp name" >
                                <b-form-input 
                                    placeholder="E.g. Monique's Boutique" 
                                    class = "mr-2 w-80" 
                                    id = "comp_name" 
                                    name="comp_name"
                                    v-model="form.comp_name"
                                    >
                                </b-form-input>
                                <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
                            </validation-provider>
                            <validation-provider v-slot="{ errors }" rules="required" name="name_end" >
                                <b-form-input 
                                    placeholder = "eg. Ltd." 
                                    class = "w-25" 
                                    id="name_end" 
                                    name = "name_end"
                                    v-model="form.name_end"
                                    >
                                </b-form-input>
                            <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
                            </validation-provider>
                        </div>  
                    </div>
                    
                    <div class="shares-div "> 
                        <div class = "about-business-form-item"> 
                            <validation-provider v-slot="{ errors }" rules="required" name="corp_type" >
                                <label for = ""> Product or Service </label>
                                <b-form-select 
                                    id = "corp_type" 
                                    name= "corp_type" 
                                    :options="busNature"
                                    v-model="form.corp_type"
                                > 
                                </b-form-select>
                                <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
                            </validation-provider>
                        </div>
                        <div class="about-business-form-item">
                            <validation-provider v-slot="{ errors }" rules="required" name="bus_tel" >
                                <label for = ""> Telephone </label>
                                <b-form-input 
                                    placeholder="(555)-XXX-XXXX" 
                                    id = "bus_tel"
                                    name = "bus_tel"
                                    v-model="form.bus_tel"
                                    >
                                </b-form-input>
                                <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
                            </validation-provider>
                        </div>
                        
                    </div>
                
                    <div class="about-business-form-item">
                        <validation-provider v-slot="{ errors }" rules="required" name="bus_address" >    
                            <label for = ""> Business Address</label>
                            <b-form-input 
                                placeholder="1234 Plaza Square, Place, Jamaica, JMDCN10" 
                                class = "bus-address" 
                                id = "bus_address"
                                name = "bus_address"
                                v-model="form.bus_address"
                                >
                            </b-form-input>
                            <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
                        </validation-provider>
                    </div>
                    <div class="about-business-form-item">
                        <validation-provider v-slot="{ errors }" rules="required" name="industry" >
                            <label for="industry"> Business Description</label>
                            <b-form-input 
                                placeholder = "Write 2 or 3 sentences" 
                                class = "bus-desc" 
                                id = "industry"
                                name= "industry"
                                v-model="form.industry"
                                >
                            </b-form-input>
                            <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
                        </validation-provider>
                    </div>
                    <button 
                        @click="TeamAdd" 
                        type="button" 
                        class="btn bus-btn "
                        >
                        Next
                    </button>
                <!-- </b-form> -->
                </validation-observer>
            </div>
        </div>
    </div>
</template>


<script > 

export default{
  components: {  },
    name: 'about-businessDetails', 
    layout: 'onboarding',
    data () { 
        return { 
            corp_types: [
                {value : null, text: 'Please select your type of incorporation.'},
                {value : 'a', text: 'Private Company '},
                {value : 'b', text: 'Unlimited Liability Company'},
                {value : 'c', text: 'Limited Liability Company'},
                
            ], 
            busNature: [
                {value: null, text: 'Select Product-Based or Service-Based'},
                {value: 'a', text: 'Product-Based'},
                {value: 'b', text: 'Service-Based'},
            ],
            form: {
                comp_name: '', 
                name_end : '', 
                bus_tel: '', 
                bus_address: '', 
                industry: '',
            }
        }
    }, 
    methods: {
        TeamAdd: function (){
            this.$router.push("../../onboarding/personal-details");
        }
    }
}

</script>

<style scoped>
    .about-business-page{

        display: flex;
        flex-direction: row;
        min-height: 100vh;
 
        
    }

    .side-bar{
        display:none;
        /* min-height:100vh; */
    }
    .about-business-main{
        margin-left: 15rem;
        margin: 2rem;
        margin-top: 4rem;
        font: 400 1rem "Poppins";

    }

    .about-business-heading p{ 
        margin: 2rem 0;
        
        font: 400 1rem "Poppins";

    }
    .shares-div{
        display: flex;
        flex-direction: row;
        width: 26rem;
    

    }
    .shares-div .about-business-form-item{
        margin-right: 1rem;
    }
    .shares-div b-form-input{
        margin-right: 1rem;
        
    }

    .about-business-heading h5{ 
        font: 600 1.8rem "Poppins";
    }

    .about-business-form-item{ 
        margin: 1rem 0;
        width: 25rem;
    }

    .about-business-form-item b-form-input{

    }

    .bus-desc{
        height: 6rem;
    }
    .bus-address{
        height: 3rem;
    }
    /* Extra small devices (phones, 600px and down) */
    @media only screen and (max-width: 600px) {
        
    }
/* Small devices (portrait tablets and large phones, 600px and up) */
    @media only screen and (min-width: 600px) {
         .about-business-heading p{
            width: 26rem;
        }
    }
/* Medium devices (landscape tablets, 768px and up) */
    @media only screen and (min-width: 768px) {
        .side-bar{
            display: block;
            position:fixed;
            /* height: 100vh; */
        
        }

        .about-business-main{
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