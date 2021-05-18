<template>
    <div class="">
        <div  class="">
            <img src="~/assets/uploads/onboard-img.svg" alt="" class="onboard-img ">
            <div class = "onboard-container d-flex flex-column  ">
                <p class="onboard-p">Click to begin setting up your business.</p>
                <nuxt-link :to="{name: 'onboarding-email-section'}">
                    <button  class="onboard-btn btn btn-sm justify-content-center">Get Started</button>
                </nuxt-link>
                
            </div>
        </div>
        
      
    </div>
   
</template>


<script>
export default {
  components: {
  
    },
    name: 'on-boarding',
    layout: 'DashboardLayout',
    head(){
          return{
              title: 'Onboarding'
          }
        },
    data(){
        return{
            secfocus: true,
            secfocusN: true, 
            form_toggle: true,

        }
}, 
methods: {
    
    }
}

</script>

<style scoped>
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
        margin-left: 10rem;
        width: 100vw;
        height:100vh;
    }
    .onboard-container{
        display:flex;

        z-index: 2;
    }
    .onboard-p{
        margin-top: 2rem;
        z-index: 2; 
        text-align: center;
        font: 400 0.8rem "Poppins"; 
    }

    .onboard-btn{
 
        display: flex;
        justify-content: center;
        align-items: center;
        width: 8rem; 
        height: 3rem;
        background-color: rgb(79, 201, 218,0.5);
        box-shadow: 0 2px 2px 0 rgba(107, 104, 104, 0.15), 0 6px 20px 0 rgba(119, 114, 114, 0.15);
    
    }
   .onboard-img{
       max-width: 100%;
       max-height: 100vh;
       /* background-color: brown; */
   }

</style>