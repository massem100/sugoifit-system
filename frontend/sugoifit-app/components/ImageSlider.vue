<template>
    <v-carousel
      cycle
      height="400"
      hide-delimiter-background
      show-arrows-on-hover
    >
      <v-carousel-item v-for="item in products" :key="item" >
        <v-sheet :color="colors[i]"  height="100%" >
          <v-row class="fill-height" align="center" justify="center">
           
            <div class="display-3">
              <img :src='require("~/assets/uploads/boutique.jpg")' alt="">
            </div>

          </v-row>
        </v-sheet>
      </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
    name: "Slider",
  data() {
    return {
      products: [],
      colors: [
          'indigo',
          'warning',
          'pink darken-2',
          'red lighten-1',
          'deep-purple accent-4',
        ],
        slides: [
          'First',
          'Second',
          'Third',
          'Fourth',
          'Fifth',
        ],
    };
  },

  async created() {
      const response = await fetch('http://localhost:8080/api/products');
      const data = await response.json();
      this.products = data;
      console.log(this.products);
  },
};
</script>
<style scoped>

</style>