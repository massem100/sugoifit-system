<template>

    <div class="wrapper">
        
        <div class="d-flex flex-column justify-content-center m-2">
            <h1 class="m-3 ml-4">Shopping Cart </h1>
            <b-col class="d-flex" >
                <div class="d-flex w-50">
                    <b-col class="">
                        <b-col class="card d-flex flex-row  w-80" v-for="product in products"  :key="product.prodID">
                            
                            <b-row class="card-image d-flex flex-row m-2 align-items-center"> 
                                <img style="width: 150px; height:150px;" 
                                    class ="bg-white " 
                                    :src=" 'http://localhost:8080/static/uploads/' + product.image" 
                                />
                            </b-row>
                            <b-col class="card-text d-flex flex-column text-black text-left align-items-start justify-content-start ">
                                <h4 class="mt-3" v-text="product.prodName"></h4>
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
                                                :name="form.color"> </b-form-input>
                                    <div :style= "[{'Background-color': '#e5e5e5' }]"> </div>
                                </b-row>
                            
                                <span class=""> Price: {{product.unit_price}} </span>
                            </b-col>
                            
                        </b-col>
                    </b-col>

                </div>

                <div class="ml-5">
                    <div class="">
                        <div class="">
                            <div class=""  >
                                <h2>Cost Breakdown</h2>
                            
                                    <b-row class="h4 w-100 "> 
                                        <b-col class=" w-100 ">
                                            <p class="m-2 h3" >Item Cost: {{ orderTotal }} </p>
                                            <p class="m-2 h3" style="width: 14rem;">Delivery Cost/Pick up:</p>
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
                                            <!-- <p class="m-2 h3 ml-3">${{ product.unit_price }} </p> -->
                                            <!-- <p class="m-2 h3 ml-3">${{ product.deliver }} </p> -->
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
                                            <p class="h2 m-2 ml-3" >Total  </p>

                                        </b-col>
                                        
                                    </b-row>
                            </div>
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
            </b-col>
        
        </div>
    
    </div>
</template>

<script>

export default {
    name: 'placeorder',
    layout:'WebsiteLayout',
    components: {},
    head:{
        title: 'Business Name Checkout'
    },

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
        // let self = this
        orderTotal: function(price, quantity) {
            if (price && quantity){
                return parseInt(this.form.price.trim())* parseInt(this.form.quantity.trim());
            }
            
        }
    },
    mounted() {
        let self=this;
        const busID = localStorage.getItem('busID');
        this.$axios.get(`/api/${busID}/products`
            ).then(res =>{
                return res.data;
            }).then(res =>{
                if (res){
                    let cart = localStorage.getItem('cart');
                    console.log('initial cart', cart);

                    // Checks if cart exists else create new object
                    cart = cart ? JSON.parse(cart) : {};
                    res.forEach(function(item, index){
                        if (cart[`Product${item.prodID}`]){
                            self.products.push({'prodID': item.prodID,
                                                'prodName': item.prodName, 
                                                'unit_price': item.unit_price,
                                                'image': item.image
                                                });
                        }
                    });
                localStorage.setItem('cart', JSON.stringify(cart));
            }else{
                console.log('Data not found')
            }
            });

    
        
        
    },
    methods: {
        custOrder: function () {
            let self = this;
            let busID = localStorage.getItem('busID');
            let cart = localStorage.getItem('cart');
            let orderForm = document.getElementById("orderForm");
            let form_data = new FormData(orderForm);
            form_data.append("tcost",self.tcost);
            form_data.append("products", products)
            console.log(products);
            let PATH_API = busID+'placeorder';
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
