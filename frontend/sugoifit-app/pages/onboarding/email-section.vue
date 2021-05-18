<template>

     <div class=" d-flex flex-column w-100" >
          <b-row class="d-flex flex-row align-items-center">
            <back-button class=" ml-2"></back-button>
            <div class = "d-flex flex-column justify-content-center mt-4">
                        <h4 class ="mb-4">Set up your Business Profile.</h4>
                        <p class="email-text mb-5"> Managing your business has never been this easy. <br>
                            Enter your business email address to continue. 
                        </p>
            </div>     
        </b-row>
         
        <div class="email-form-section h-25 d-flex flex-row">
            
            <div class = "d-flex ml-4">
            
                <label class ="" for="email">Email Address</label>
                <input type="text" name ="email" class="form-control" >
            
                <div @click ="ChangeComp" class="get-started btn btn-sm ">Get Started <span></span></div>
            </div>
    <div  class="company-type-section bg-danger" >
     
        <div class = "company-heading">
            <h5 class="">Choose the type of business</h5>
            <p class="">Choose the option that best describes your business.</p>
        </div>
        <div class="type-categories">
            
            <div class="type-item">
                <img class = "type-icon" src="~assets/uploads/checked.svg" alt="">
                <h6> Sole Trader </h6>
                <p> A business owned and operated by one individual.</p>
            </div>
            <div class="type-item">
                <img class = "type-icon" src="~assets/uploads/checked.svg" alt="">
                <h6>Partnership</h6>
                <p>An unincorporated business owned by two or more persons.</p>
            </div>
            <div class="type-item">
                <img class = "type-icon" src="~assets/uploads/checked.svg" alt="">
                <h6>Company</h6>
                <p>A business that is incorporated. Please select type of incorporation, private or public.</p>
            </div>
            <div class ="d-flex flex-row justify-content-center ">
            <div  class="type-btn-n btn btn-lg">

                    <h6> Next</h6>
            </div>
        </div>
                         
    </div>
    

    
</div>
        </div>

    </div>
   
</template>



<script>
import BackButton from '../../components/argon-core/BackButton.vue';

export default {
    components: { BackButton },
    layout: 'DashboardLayout',
    name: 'emailsection', 
    head(){
          return{
              title: 'Business Profile'
          }
        },
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
    
    .email-heading{
        margin: 20px 20px 20px 20px;

        font : 400 1rem "Poppins";
    }

    .email-heading h4{ 
        font: 600 1.6rem "Poppins";
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
   
    
    .company-type-section{
        display: flex;
        flex-direction: column;
        justify-content: center;
        /* align-items: center; */
        min-height:100vh;
    }
  
    .company-type-section p{
        font:400 1rem "Poppins";
    }

    .company-heading h4{ 
        font: 600 1.6rem "Poppins";
    }
    .type-categories{
        display: grid;
        grid-template-rows: 1fr 1fr 1fr;
        
    }

    .type-item{
        display: grid;
        grid-template-areas: "icon type-name " 
                            "icon text ";
        margin: 0.5rem 1rem;
        width:25rem;
        height: 7.6rem;
        background-color: #ffffff;
        border-radius:20px;
        /* padding: 15px; */
     
        box-shadow: 0 2px 2px 0 rgba(107, 104, 104, 0.15), 0 6px 20px 0 rgba(119, 114, 114, 0.15);
    }

    .type-item h6{
        color: #387780;
        font: 600  1rem "Poppins";
        grid-area: type-name;
    }

    .type-item p{
           font: 400 0.91rem "Poppins";
           grid-area: text;
    }

    .type-icon{
        display: flex;
        justify-content: center;
        align-items: center;
        margin:  0.5rem;
        width: 2rem; 
        height: 4rem;
        grid-area: icon;
        /* background-color: #387780; */
    }

    .type-btn-n{
        margin-top: 1rem;
        display:flex; 
        flex-direction: row;
        justify-content: center;
        width: 8rem;
        height: 2.8rem;   
        background-color: #E5E5E5;
        box-shadow: 0 2px 2px 0 rgba(107, 104, 104, 0.15), 0 6px 20px 0 rgba(119, 114, 114, 0.15);
        
        font: 600 1rem "Poppins";
        vertical-align: middle;
        color: rgb(41, 41, 41);


    }

    .type-btn-n h6{
        padding: 6px;
        display: flex;
        align-items:center;
        justify-content: center;
        vertical-align: middle;
    }
</style>