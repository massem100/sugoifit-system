<template>
  <div>
    <a class="prev" @click="prev" href="#">&#10094; Previous</a>
    <a class="next" @click="next" href="#">&#10095; Next</a>
    <transition-group name="fade" tag="div">
      <div v-for="i in [currentIndex] " :key="i">
        <img :src="currentImg" />
      </div>
    </transition-group>
    
  </div>
</template>

<script>
export default {
    name: "Slider",
  data() {
    return {
      images: [
        "https://glaminati.com/wp-content/uploads/2017/02/tp-popular-casual-outfits-1.jpg",
        "https://ae01.alicdn.com/kf/HTB1SzJtcO0TMKJjSZFNq6y_1FXaj/New-Fashion-Casual-Men-Shirt-Long-Sleeve-Europe-Style-Slim-Fit-Shirt-Men-High-Quality-Cotton.jpg_Q90.jpg_.webp",
        "https://image.made-in-china.com/44f3j00ETzQpGfrdgRF/Fashion-Clothes-Orange-Chiffon-Dress-Hollow-Waist-Daily-Wear-Ladies-Dress-Bandage-Dress-Short-Dresses.jpg",
        "https://cdn.cliqueinc.com/posts/80160/casual-wear-1-80160-1580145811977-image.700x0c.jpg"
      ],
      timer: null,
      currentIndex: 0
    };
  },

  mounted: function() {
    this.startSlide();
  },

  methods: {
    startSlide: function() {
      this.timer = setInterval(this.next, 9000);
    },

    next: function() {
      this.currentIndex += 1;
    },
    prev: function() {
      this.currentIndex -= 1;
    }
  },

  computed: {
    currentImg: function() {
      return this.images[Math.abs(this.currentIndex) % this.images.length];
    }
  }
};
</script>
<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: all 0.9s ease;
    overflow: hidden;
    visibility: visible;
    position: relative;
    opacity: 1;
}
.fade-enter,
.fade-leave-to {
  visibility: hidden;
  opacity: 0;
}

img {
  height:700px;
  width:100%;
  position: center;
}

.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 60%;
  padding: 6em;
  color: rgb(26, 119, 88);
  font-weight: bold;
  font-size: 18px;
  transition: 0.7s ease;
  border-radius: 0 4px 4px 0;
  text-decoration: none;
  user-select: text;
}

.next {
  right: 0;
}

.prev {
  left: 0;
}

.prev:hover, .next:hover {
  background-color: white;
}
</style>