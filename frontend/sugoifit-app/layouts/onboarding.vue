<template>
  <div>
      <b-row class="d-flex flex-row"> 
        <onboarding-side  class = "side-bar h-100 m-0"></onboarding-side>
      <nuxt />
      </b-row>
  </div>
</template>

<script>
import OnboardingSide from '/components/onboarding-side.vue'
  export default {
    components: { 
      OnboardingSide
    },
    data() {
      return {
        isLoading: true
      }
    },
    mounted() {
      this.$nextTick(function() {
        this.isLoading = false
      });
    }
  }
</script>
