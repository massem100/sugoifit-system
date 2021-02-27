<template>
    <div class="container">
        <div class="header">
            <WebsiteHeader />
        </div>

        <div class="left">
            <div class="column">
                <div class="card">
                    <div class="card-image">
                        <img src="~/assets/uploads/products/skirt1.jpg" alt="Picture" style="width:50%">
                    </div>
                    <div class="card-text">
                        <p class="quantity">Quantity:</p>
                        <p class="size">Size:</p>
                        <p class="colour">Colour:</p>
                        <p class="price">Price:</p>
                    </div>
                </div>
            </div>
            <div class="column">
                <div class="card">
                    <div class="card-image">
                        <img src="~/assets/uploads/products/pants3.jpg" alt="Picture" style="width:50%">
                    </div>
                    <div class="card-text">
                        <p class="quantity">Quantity:</p>
                        <p class="size">Size:</p>
                        <p class="colour">Colour:</p>
                        <p class="price">Price:</p>
                    </div>
                </div>
            </div>
            <div class="column">
                <div class="card">
                    <div class="card-image">
                        <img src="~/assets/uploads/products/top1.jpg" alt="Picture" style="width:50%">
                    </div>
                    <div class="card-text">
                        <p class="quantity">Quantity:</p>
                        <p class="size">Size:</p>
                        <p class="colour">Colour:</p>
                        <p class="price">Price:</p>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</template>

<script>
import WebsiteHeader from '../components/WebsiteHeader';
export default {
    name: 'PlaceOrder',
    components: {
        WebsiteHeader
    }
}
</script>

<style scoped>

.column {
    width: 25%;
    display: flex;
    flex-direction: column;
    margin: 0 auto;
    border-radius: 5px;
    overflow: hidden;
    z-index: 0;
}
.card {
    border: none;
    position: relative;
    z-index: 0;
    height: 200px;
    display: flex;
    flex-direction: row;
}
.card-image {
    border-right: solid 1px rgb(196, 193, 193);
    height: 200px;
    width: 200px;
}
.card-text {
    padding: 1rem;
    position: relative;
}
</style>
