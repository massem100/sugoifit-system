<template>
    <div class="wrapper">
        
        <div class="header">
            <WebsiteHeader />
        </div>
        <div class="items">
            {{ content }}
        </div>

        <div class="container">

        </div>
        
    </div>
</template>

<script>
import WebsiteHeader from '../../components/WebsiteHeader';
export default {
    name: 'Products',
    components: {
        WebsiteHeader
    },
    data() {
        return {
            content: null
        }
    },
    async created() {
        const response = await fetch('http://localhost:8080/api/items');
        const data = await response.json();
        this.content = data.content;
        console.log(this.content);
    },
}
</script>

<style scoped>
.wrapper{
    margin: 2em;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.container{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-content: center;
}
</style>
