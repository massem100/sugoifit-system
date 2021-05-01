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
                            <p id="tprice">Item Cost: ${{ tprice }} </p>
                            <p>Delivery Cost/Pick up: ${{ deliver }}</p>
                            <p id="tcost">Total Cost: ${{ tcost }}</p>
                        </div>
                        <!--<div class="right-btn">
                            <button id="checkout-btn" type="submit">Checkout</button>
                        </div>-->
                    </div>

                    <!-- customer info form -->
                    <div class="bottom">
                        <div class="order-form-div">
                            <h3>You're Almost Done</h3>
                            <p>Please fill out the form below.</p>
                            
                            <b-form id="orderForm" method="POST" @submit.prevent="custOrder" enctype="multipart/form-data">
                                <input type="hidden" name="_token" :value="token">

                                <div class="business-form-item">
                                    <label for="fname"> First Name </label>
                                    <b-form-input placeholder= "" name="fname" id = "fname" required></b-form-input>
                                </div>
                                
                                <div class = "business-form-item"> 
                                    <label for="lname"> Last Name </label>
                                    <b-form-input placeholder="" name="lname" id="lname"></b-form-input>
                                </div>

                                <div class="business-form-item">
                                    <label for="trn">TRN</label>
                                    <b-form-input placeholder= "" name="trn" id="trn"></b-form-input>
                                </div>
                                
                                <div class="business-form-item">
                                    <label for="address">Address</label>
                                    <b-form-input placeholder="" name="address" id="address"></b-form-input>
                                </div>

                                <div class="business-form-item">
                                    <label for="phone_num">Phone Number</label>
                                    <b-form-input placeholder="" name="phone_num" id="phone_num"></b-form-input>
                                </div>

                                <div class="business-form-item">
                                    <label for="email">Email Address</label>
                                    <b-form-input placeholder="" name="email" id="email"></b-form-input>
                                </div>

                                <div class="business-form-item">
                                    <button type="submit" class="order-submit"> Order </button>
                                </div>
                            </b-form>
                           
                        </div>
                    </div>
                </div>
            </div>
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
            tprice: '',
            tcost: '',
            token: ''
        }
    },
    async created() {
        const response = await fetch('http://localhost:8080/api/checkout-products');
        const data = await response.json();
        this.cards = data.lst;
        this.tcost = data.total_cost;
        this.deliver = data.delivery_price;
        this.tprice = data.total_price;
    },
    methods: {
        custOrder: function () {
           let self = this;
            let orderForm = document.getElementById("orderForm");
            let form_data = new FormData(orderForm);
            form_data.append("tcost",this.tcost);

            let PATH_API = 'placeorder';
                this.$axios.post(`/api/${PATH_API}`, form_data, {
                  headers: {
                  'contentType': 'application/json',
                }
              })
              .then( jsonResponse =>{
                return jsonResponse.json();
              })
              .then( jsonResponse =>{
                console.log(jsonResponse);
              })
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
 
.order-submit{
    height: 2em;
    width: 120px;
    border-radius: 15px;
    color: white;
    font-size: 15px;
    margin:1em 0 .2em;
    background-color: rgb(46, 158, 102);
}
</style>
