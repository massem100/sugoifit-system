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

                    <label>Type of corporation</label>
                    <b-form-input class="w-25"> </b-form-input>
                </b-form>
            </div>


        </div>
    </div>
    
</template>


<script > 
import onboardingSide from '../../components/onboarding-side.vue'
export default{
  components: { onboardingSide },
    name: 'BusinessDetails'
}

</script>

<style scoped>
    .business-page{
        display: flex;
        flex-direction: row;
    }
</style>