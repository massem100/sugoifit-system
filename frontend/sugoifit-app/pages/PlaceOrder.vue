<template>
    <div class="wrapper">
        <div class="header">
            <WebsiteHeader />
        </div>
        <div class="container">
            <div class="left">
                <div class="column">
                    <div class="card" v-for="card in cards" :card="card" :key="card">
                        
                        <div class="card-image"> 
                            <img :src="card.img" alt="Image">
                        </div>
                        <div class="card-text">
                            <p class="quantity">Quantity: {{ card.quantity }} </p>
                            <p class="size">Size: {{card.size}} </p>
                            <p class="colour">Colour: {{card.colour}} </p>
                            <p class="price">Price: {{card.price}} </p>
                        </div>
                
                    </div>
                </div>
            </div>

            <div class="right">
                <div class="column">
                    <div class="top">
                        <div class="right-text"  v-for="card in cards" :card="card" :key="card">
                            <h3>Cost Breakdown</h3>
                            <p>Item Cost: {{card.price}} + {{card.price}} </p>
                            <p>Delivery Cost/Pick up: JMD 500.00</p>
                            <p>Total Cost: JMD 2500.99</p>
                        </div>
                        <div class="right-btn">
                            <button id="checkout-btn" type="submit">Checkout</button>
                        </div>
                    </div>

                    <!-- customer info form -->
                    <div class="bottom">
                        <div class="form">
                            <h3>You're Almost Done</h3>
                            <p>Please fill out the form below.</p>
                            <form id="order" action="" method="post">
                                <fieldset>
                                    <label for="fname">First Name</label>
                                    <input placeholder="" type="text" tabindex="1" required autofocus>
                                </fieldset>
                                <fieldset>
                                    <label for="lname">Last Name</label>
                                    <input placeholder="" type="text" tabindex="2" required>
                                </fieldset>
                                <fieldset>
                                    <label for="address">Address</label>
                                    <input placeholder="" type="text" tabindex="3" required>
                                </fieldset>
                                <fieldset>
                                    <label for="num">Phone Number</label>
                                    <input placeholder="" type="tel" tabindex="4" required>
                                </fieldset>
                                <fieldset>
                                    <label for="trn">TRN</label>
                                    <input placeholder="" type="trn" tabindex="5" required>
                                </fieldset>
                                <fieldset>
                                    <button name="submit" type="submit" id="order-submit" data-submit="...Sending">Submit</button>
                                </fieldset>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="bottom">
            
        </div>
        
    </div>
</template>

<script>
import WebsiteHeader from '../components/WebsiteHeader';
export default {
    name: 'PlaceOrder',
    components: {
        WebsiteHeader
    },
    methods: {
        priceTotal: () => {
            for card in cards 
            console.log('working');
        }
    },
    data() {
        return {
            cards: [
                { 
                    id: 1,
                    img: "~/assets/uploads/products/skirt1.jpg",
                    name: 'skirt',
                    quantity: '1',
                    size: 'L',
                    colour: 'black',
                    price: "$500" 
                },
                { 
                    id: 2,
                    img: "~/assets/uploads/products/pants3.jpg",
                    name: 'dress',
                    quantity: '1',
                    size: 'medium',
                    colour: 'white',
                    price: '$600' 
                },
                { 
                    id: 3,
                    img: "~/assets/uploads/products/top1.jpg",
                    name: 'top',
                    quantity: '1',
                    size: 'medium',
                    colour: 'white',
                    price: '$600' 
                }
            ]
        }
  }
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


/*  left side of webpage*/

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

/* Right side of the page */
.right .column {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.top{
    flex: 1 1 300px;
    width: 100%;
    line-height: 2em;
    margin: 0 auto;
    overflow: hidden;
    z-index: 0;
}

#checkout-btn{
    height: 3em;
    width: 170px;
    border-radius: 15px;
    color: white;
    font-size: 15px;
    background-color: rgb(46, 158, 102);
}

.bottom{
    flex: 1 1 200px;
}

fieldset{
    padding: 10px 5px;
}
label{
  display:block;
  margin:1em 0 .2em;
}
input{
  display:block;
  width:100%;
  padding:.3em;
  font-size:20px;
  border: none;
  background-color: rgba(119, 255, 187, 0.705);
  border-radius: 20px;
  resize:vertical;
}
 
#order-submit{
   height: 3em;
    width: 170px;
    border-radius: 15px;
    color: white;
    font-size: 15px;
    background-color: rgb(46, 158, 102);
}
</style>
