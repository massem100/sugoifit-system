<template>
  <div class="container">

    <!--- Navigation -->
    <div class="flex-item">
      <div class="header">
        <a class="logo" href="#"> <i class="fas fa-leaf"></i>Monique's Boutique</a>
        
        <div class="header-right">
          <a class="nav-link" href="#">All Products</a>
          <a class="nav-link" href="#"> FAQ </a>
          <a class="nav-link" href="#">Contact</a>
          <a class="nav-link" href="/placeorder">Place an Order </a>
          <a class="nav-link" href="#"><i class="fas-fa-shopping-bag"></i> </a>
        </div>
      </div>
    </div>

    <!-- Main section
    <div class="flex-item">
      <home> </home>
    </div> -->

    <!-- Place Order -->
    <div class="flex-item">
      <place-order></place-order>
    </div>  


    

  </div>
</template>

<script>
import Home from './Home.vue'
import PlaceOrder from './PlaceOrder.vue'
export default {
  components: { 
    Home,
    PlaceOrder
  },
  name: 'Website',
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
