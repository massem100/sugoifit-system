<template>
    <div class="m-0 d-flex flex-row">
        <onboarding-side class = "m-0"></onboarding-side>
        <company-type></company-type>

    </div>
</template>


<script>
import CompanyType from '../components/onboarding/CompanyType.vue'
import OnboardingSide from '../components/onboarding/onboarding-side.vue'
export default {
  components: { CompanyType, OnboardingSide },
    name: 'on-boarding',
}
</script>