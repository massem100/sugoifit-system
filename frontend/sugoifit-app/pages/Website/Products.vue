<template>
    <div class="wrapper">
        <v-col>
            <div class="header">
                <WebsiteHeader />
            </div>
            
            <v-container fluid >
                <v-row >
                    <h2 class="text-center">Our Products</h2>
                    <v-col  class="col-4" :md="6" :sm="8">
                        <v-card class="d-flex flex-row mb-6" flat tile >
                            <v-card v-for="item in products" :key="item.id" class="pa-2" flat tile>

                            <v-img :src='require("~/assets/uploads/boutique.jpg")' aspect-ratio="1" class="grey lighten-2 " max-height="184" max-width="100%"></v-img>
                                <v-card-text class="text--primary text-center">
                                    <div class="title">{{ item.name }}</div>
                                    <p>${{ item.price }}</p>
                                </v-card-text>

                            </v-card>
                        </v-card>
                        <!--<b-card-group deck>
                            <b-card  v-for="item in products" :key="item.id">
                                <b-list-group>
                                    <b-list-group-item href="#">
                                        <v-img :src='require("~/assets/uploads/boutique.jpg")'></v-img>
                                    </b-list-group-item>
                                    <b-list-group-item href="#">{{ item.name }}</b-list-group-item>
                                    <b-list-group-item href="#">{{ item.price }}</b-list-group-item>
                                </b-list-group>

                                <p class="card-text mt-2">
                                Description: Quis magna Lorem anim amet ipsum do mollit sit cillum voluptate ex nulla tempor. 
                                </p>
                            </b-card>
                        </b-card-group>-->
                    </v-col>
                </v-row>
            </v-container>
            

        </v-col>
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
            products: []
        }
    },
    async created() {
        const response = await fetch('http://localhost:8080/api/products');
        const data = await response.json();
        this.products = data;
        console.log(this.products);
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
