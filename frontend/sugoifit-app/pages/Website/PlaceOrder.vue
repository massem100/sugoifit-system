<template>
<<<<<<< HEAD
    <div class="wrapper">
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
=======
    <div class="d-flex flex-column justify-content-center m-2">
        <h1 class="m-3 ml-4">Shopping Cart </h1>
        <div class="d-flex">
            <div class=" w-50">
                <b-col class="">
                    <b-col class="card d-flex flex-row  w-80" 
                           v-for="product in products" 
                           :key="product.id" >
                        <b-row class="card-image d-flex flex-row m-2 align-items-center"> 
                            <img style="width: 100px; height:100px;" 
                                 class ="bg-white" 
                                 :src="product.img" 
                            />
                        </b-row>
                        <b-col class="card-text d-flex flex-column text-black 
                                      text-left align-items-start justify-content-center ">
                            <b-row class=""> 
                                <span class="text-left m-2"> Quantity: </span>
                                <b-form-input class="m-2" 
                                              :style="[{width: '2rem'}, {height: '2rem'}]" 
                                              :value="product.quantity"
                                              :name="form.quantity"> </b-form-input>
                            </b-row>
                            <b-row class=""> 
                                <span class="text-left m-2"> Size: </span>
                                <b-form-input class="m-2 justify-content-end" 
                                              :style="[{width: '10rem'}, {height: '2rem'}]" 
                                              :value="product.size"
                                              :name="form.size"> </b-form-input>
                            </b-row>
                            <b-row class=""> 
                                <span class="text-left m-2"> Colour: </span>
                                <b-form-input class="m-2" 
                                              :style="[{width: '4rem'}, {height: '2rem'}]" 
                                              :value="product.colour"
                                              :name="form.color"> </b-form-input>
                                <div :style= "[{'Background-color': e5e5e5 }]"> </div>
                            </b-row>
                           
                            <span class=""> Price: {{product.tprice}} </span>
                        </b-col>
                    </b-col>
                </b-col>
>>>>>>> main
            </div>

            <div class="ml-5">
                <div class="">
                    <div class="">
                        <div class="" >
                            <h2>Cost Breakdown</h2>
                         
                                <b-row class="h4 w-100 "> 
                                    <b-col class=" w-100 ">
                                        <p class="m-2 h3">Item Cost:    </p>
                                        <p class="m-2 h3" style="width: 14rem;">Delivery Cost/Pick up:  </p>
                                       <hr
                                        class="my-3"
                                        style="
                                            border: 0;
                                            border-top: 1px solid rgba(0, 0, 0, 0.1);
                                            min-width: 80%;
                                            overflow: visible;
                                            box-sizing: content-box;
                                            height: 0;
                                        "
                                        />
                                        <p class="m-2 h2 font-weight-bold ">Total:  </p> 
                                    
                                    </b-col>
                                    <b-col> 
                                        <p class="m-2 h3 ml-3">${{ tprice }} </p>
                                        <p class="m-2 h3 ml-3">${{ deliver }} </p>
                                        <hr
                                            class="my-3"
                                            style="
                                            border: 0;
                                            border-top: 1px solid rgba(0, 0, 0, 0.1);
                                            min-width: 80%;
                                            overflow: visible;
                                            box-sizing: content-box;
                                            height: 0;
                                            "
                                        />
                                        <p class="h2 m-2 ml-3" :v-text="orderTotal"> </p>

                                    </b-col>
                                    
                                </b-row>
                          
                            
                        </div>
                        <!--<div class="right-btn">
                            <button id="checkout-btn" type="submit">Checkout</button>
                        </div>-->
                    </div>

                    <!-- customer info form -->
                    <div class="d-flex flex-column align-items-center mt-5 pt-5">
                        <b-col class="d-flex flex-column align-items-center">
                            <h3>You're Almost Done</h3>
                            <p>Please fill out the form below.</p>
                            
                            <b-form id="orderForm" method="POST" @submit.prevent="custOrder" enctype="multipart/form-data">
                                <b-row> 
                                    <div class="business-form-item m-2">
                                    <label for="fname"> First Name </label>
                                    <b-form-input placeholder= "" name="fname" id = "fname" required></b-form-input>
                                </div>
                                
                                <div class = "business-form-item m-2"> 
                                    <label for="lname"> Last Name </label>
                                    <b-form-input placeholder="" name="lname" id="lname"></b-form-input>
                                </div>


                                </b-row>
                                
                                <b-row>
                                    <div class="business-form-item m-2">
                                        <label for="trn">TRN</label>
                                        <b-form-input placeholder= "" name="trn" id="trn"></b-form-input>
                                    </div>
                                    <div class="business-form-item m-2">
                                        <label for="phone_num">Phone Number</label>
                                        <b-form-input placeholder="" name="phone_num" id="phone_num"></b-form-input>
                                    </div>

                                </b-row>
                        
                                <div class="business-form-item">
                                    <label for="email">Email Address</label>
                                    <b-form-input placeholder="" name="email" id="email"></b-form-input>
                                </div>
                                 <div class="business-form-item">
                                    <label for="address">Address</label>
                                    <b-form-input placeholder="" name="address" id="address"></b-form-input>
                                </div>

                            
                                <div class="d-flex flex-row justify-content-center ">
                                    <button type="submit" class="btn btn-lg   bg-secondary m-2 order-submit"> Submit Order </button>
                                </div>
                            </b-form>
                           
                        </b-col>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</template>

<script>
<<<<<<< HEAD
export default {
    name: 'PlaceOrder',
    layout: 'website',
    head(){
          return{
              title: 'Shopping Cart'
          }
        },
=======


export default {
    name: 'placeorder',
    layout:'WebsiteLayout',
    components: {},
    head:{
        title: 'Business Name Checkout'
    },
>>>>>>> main
    data() {
        return{
            products: [],
            deliver: '',
            tprice: '',
            tcost: '',                           
            form: {
                'quantity': '', 
                'size': '', 
                'color': '', 
                'price': '', 
              

            }
        }
    },
    computed: {
        orderTotal(tprice, quantity) {
            if (tprice && quantity){
                parseInt(this.form.tprice.trim())* parseInt(this.form.quantity.trim());
            }
            
        }
    },
    async created() {
        const response = await this.$axios.get('/api/checkout-products');
        const data = await response.data;
        if (data){
            this.products = data.lst;
            this.tcost = data.total_cost;
            this.deliver = data.delivery_price;
            this.tprice = data.total_price;
        }else{
            console.log('Data not found')
        }
        
    },
    methods: {
        custOrder: function () {
           let self = this;
            let orderForm = document.getElementById("orderForm");
            let form_data = new FormData(orderForm);
            form_data.append("tcost",self.tcost);

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
.card-text{
    font: 400 1rem "Poppins";
}
</style>
