<template>
<div class = "company-type-page">
    <div  class="company-type-section" >
         
       <div class="d-flex flex-row"> 
            <back-button class="mt-4 ml-2"></back-button>
            <div class = "company-heading">
            <h4 class=" m-4">Choose the type of business</h4>
            <p class="m-4">Choose the option that best describes your business.</p>
        </div>
       </div>
       
        <div class="type-categories">
            
            <div class="type-item">
                <img class = "type-icon" src="~assets/uploads/checked.svg" alt="">
                <h6> Sole Trader 
                    <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="A business owned and operated by one individual."/>
                     <p> A business owned and operated by one individual.</p>
                </h6>
            </div>
            <div class="type-item">
                <img class = "type-icon" src="~assets/uploads/checked.svg" alt="">
                <h6>Partnership
                    <font-awesome-icon icon="info-circle" v-b-tooltip.hover title="An unincorporated business owned by two or more persons."/>
                     <p>An unincorporated business owned by two or more persons.</p>
                </h6>
            </div>
            <div class="type-item">
                <img class = "type-icon" src="~assets/uploads/checked.svg" alt="">
                <h6>Company
                    <font-awesome-icon icon="info-circle" v-b-tooltip.hover title=
                        "A business that is incorporated. Please select type of incorporation, private or public."/>
                         <p>A business that is incorporated. Please select type of incorporation, private or public.</p>
                </h6>
            </div>
            <div class ="d-flex flex-row justify-content-center ">
            <div @click = "BusDetail" class="type-btn-n btn btn-lg">

                    <h6> Next</h6>
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
name: 'company-type',
layout:'DashboardLayout',
head(){
        return{
            title: 'Company Type'
        }
    },
data (){
    return {}
}, 
methods: {
    BusDetail: function(){
        this.$router.push('business-details/corporation');
    }
}
    
}
</script>

<style scoped>
    .side-bar{
        display: none;
    }
    .company-type-page{
        max-height:100vh;
        display: flex;
        flex-direction: row;

    }
    .company-type-section{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
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