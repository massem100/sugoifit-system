<template>
<div class = "company-type-page"> 
    <onboarding-side class="side-bar m-0 h-100" ></onboarding-side>
      <!--  COMPANY TYPE-->
                <div  class="company-type-section m-4" >
                    <div>
                        <h4 class=" m-4">Choose the type of business</h4>
                        <p class="m-4">Choose the option that best describes your business.</p>
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
                         <div class="type-btn-n btn btn-lg text-center">
                         <h6> Next</h6>

                     </div>
                    </div>
                    
                </div>
</div>
</template>


<script>
import onboardingSide from '../../components/onboarding-side.vue'

export default {
  components: { onboardingSide },
    
}
</script>

<style scoped>
    .side-bar{
        display: none;
    }
    .company-type-page{
        display: flex;
        flex-direction: row;
    }
    .company-type-section{
        display: flex;
        flex-direction: column;
    }
  
    .company-type-section p{
        font:400 1rem "Poppins";
    }

    .type-categories{
        display: grid;
        grid-template-rows: 1fr 1fr 1fr;
    }

    .type-item{
        display: grid;
        grid-template-areas: "icon type-name " 
                            "icon text ";
        margin: 16px;
        width:24rem;
        height: 7rem;
        background-color: #ffffff;
        border-radius:20px;
        padding: 15px;
     
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
        margin:  8px;
        width: 2rem; 
        height: 4rem;
        grid-area: icon;
        /* background-color: #387780; */
    }

    .type-btn-n{
        margin: 2rem;
        position: absolute;
        top: 35rem; 
        left: 8rem;


        width: 8rem;
        height: 2.8rem;        
        background-color: #E5E5E5;
        box-shadow: 0 2px 2px 0 rgba(107, 104, 104, 0.15), 0 6px 20px 0 rgba(119, 114, 114, 0.15);
        
        font: 600 1rem "Poppins";
        vertical-align: middle;
        color: rgb(41, 41, 41);

    }

    .type-btn-n h6{
        display: flex;
        align-items:center;
        justify-content: center;
    }
</style>