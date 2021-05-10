<template>
  <div>

      <nuxt />

  </div>
</template>

<script>
  export default {
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
