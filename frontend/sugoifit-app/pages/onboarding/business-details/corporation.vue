<template>
    <div class="business-page"> 
        <div class="business-main">
            <div class="business-heading">
                <h5> Business Details </h5>
                <p> Help us personalize your experience by providing some details about your business.</p>
            </div>
            <div class="business-form-div">
                    <div class="business-form-item">
                        <label for = "corp_type">Type of corporation
                            <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                            "Private Company: business entity owned by a private group of owners.
                             Limited Liability Company: business owners are not personally liable for the company's debts or liabilities
                             Unlimited Liability Company: business owners are personally liable for any loss the business makes "/>
                        </label>
                        <b-form-select aria-placeholder="Select business type." id = corp_type :options="corp_types"> </b-form-select>
                        
                    </div>
                    
                    <div class="shares-div "> 
                        <div class = "business-form-item"> 
                            <label for = ""> Number of Shares 
                                <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="Standard: 10000"/>
                            </label>
                            <b-form-input  id = ""></b-form-input>
                        </div>
                        <div class="business-form-item">
                            <label for = ""> Per value 
                                <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="Cost per share"/>
                            </label>
                            <b-form-input  id = ""></b-form-input>
                        </div>
                    </div>
                        <div class="business-form-item">
                            <label for="industry"> Industry
                                <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="e.g Technology / Finance"/>
                            </label>
                            <b-form-input id = "industry"></b-form-input>
                        </div>

                       <button @click="AboutComp" type="button" class="btn bus-btn ">Next</button>
            </div>


        </div>
    </div>
    
</template>


<script > 
export default{
  components: {  },
    name: 'BusinessDetails', 
    layout: 'DashboardLayout',
    head(){
          return{
              title: 'About the Corporation'
          }
        },
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
            /* margin-left: 20rem; */
        }

        
    }
    /* Large devices (laptops/desktops, 992px and up) */
    @media only screen and (min-width: 992px) {
        
    }
    /* Extra large devices (large laptops and desktops, 1200px and up) */
    @media only screen and (min-width: 1200px) {
        
    }
   

   
</style>