<template>
    <div class="wrapper">
        <div class="header">
            <WebsiteHeader />
        </div>
        <div class="container">
            <div class="left">
                <div class="column">
                    <div class="card" v-for="card in cards" :card="card" :key="card.id" >
                        
                        <div class="card-image"> 
                            <img :src="card.img" />
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
                        <div class="right-text" >
                            <h3>Cost Breakdown</h3>
                            <p>Item Cost: {{ tprice }} </p>
                            <p>Delivery Cost/Pick up: {{ deliver }}</p>
                            <p>Total Cost: {{ tcost }}</p>
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
                            <form id="orderForm" method="post" @submit.prevent="custOrder" enctype="multipart/form-data">
                                <input type="hidden" name="csrf_token" :value="token"/>
                                <fieldset>
                                    <label for="fname">First Name</label>
                                    <input placeholder="" type="text" tabindex="1" required autofocus>
                                </fieldset>

                                <fieldset>
                                    <label for="lname">Last Name</label>
                                    <input placeholder="" type="text" tabindex="2" required>
                                </fieldset>

                                <fieldset>
                                    <label for="trn">TRN</label>
                                    <input placeholder="" type="trn" tabindex="3" required>
                                </fieldset>

                                <fieldset>
                                    <label for="address">Address</label>
                                    <input placeholder="" type="text" tabindex="4" required>
                                </fieldset>

                                <fieldset>
                                    <label for="phone_num">Phone Number</label>
                                    <input placeholder="" type="tel" tabindex="5" required>
                                </fieldset>

                                <fieldset>
                                    <label for="email">Email Address</label>
                                    <input placeholder="" type="email" tabindex="6" required>
                                </fieldset>

                                <fieldset>
                                    <button  name="submit" class="Submit" id="order-submit">Submit</button>
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
import WebsiteHeader from '../../components/WebsiteHeader';
export default {
    name: 'PlaceOrder',
    components: {
        WebsiteHeader
    },
    data() {
        return{
            cards: null,
            deliver: '',
            token: '',
            tprice: '',
            tcost: ''
        }
    },
    async created() {
        const response = await fetch('http://localhost:8080/api/products');
        const data = await response.json();
        this.cards = data.cards;
        this.tcost = data.tcost;
        this.deliver = data.deliver;
        this.tprice = data.tprice;
    },
    methods: {
        custOrder: function () {
            let self = this;
            let orderForm = document.getElementById("orderForm");
            let form_data = new FormData(orderForm);

            fetch("http://localhost:8080/api/order", {
                method: "POST",
                body: form_data,
                headers: {
                    "Accept": "application/json",
                    "X-CSRFToken": token,
                },
                credentials: "same-origin",
            })
            .then( response => response.json() );
            
            console.log(response);
        },
        
            
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
img {
    padding: 2em;
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
