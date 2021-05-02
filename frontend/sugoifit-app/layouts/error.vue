<template>
  <div class="bg-default">
    <div v-if="error.statusCode === 404" class="col-xl-5 col-lg-6 col-md-8 px-5">
              <h1 class="text-white">Ooops!</h1>
              <p class="text-lead text-white">Page not found. Don't worry though, we have plenty of other pages to explore</p>

              <nuxt-link to="/" class="font-weight-bold text-white mt-5">Back to dashboard</nuxt-link>
            </div>
            <div v-else>
              <h4 >An error occurred</h4>
            </div>
  </div>
</template>

<script>
export default {
  
}
</script>
