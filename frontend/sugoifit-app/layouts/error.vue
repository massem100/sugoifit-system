<template>
  <div>
    <h1 v-if="error.statusCode === 404">
        404 - Page not found. return to <NuxtLink :to="{name:'index'}">Home page</NuxtLink></h1>
    <h1 v-else>An error occurred</h1>
  </div>
</template>

<script>
  export default {
    props: ['error']
  }
</script>