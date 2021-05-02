<template>
    <b-button 
              class="text-primary m-0"
              @click="goBack"
              variant="gray"
              :style="{fontSize: '1.5rem'}"
              shadow-none
              >
            <font-awesome-icon :icon="['fas','chevron-left']"> </font-awesome-icon>
    </b-button>
</template>

<script>
export default {
    name:'back-button',
    methods:{
        goBack(){
            this.$router.go(-1);
        }
    }
    
}
</script>
<style scoped>
    .btn-index{
        z-index:2;
    }
</style>