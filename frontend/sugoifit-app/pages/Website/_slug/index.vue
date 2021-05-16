<template>
    <div class="">
       
        <div class="d-flex flex-column ml-5 ">
           <!-- Updated Hero -->
              <div class="d-flex flex-row "
                    style="max-width: 100vw;
                            height: 60vh;"
                >
                <div class="d-flex flex-column justify-content-center w-50 ">
                    <div class=" mt-4 pt-3">
                        <h1 class = "font-weight-bold "> <strong>Slice Bread? Better. Clothes! </strong> </h1>
                        <p class= "w-75"> Young aspiring entrepreneur, spreading love and peace through style
                            is a free image placeholder service for web designers, serving billions and billions of images each year.
                        </p>
                    </div>
                    <b-row class="ml-1"> 
                        <div class="btn btn-lg bg-primary my-4 text-white w-25">Place an Order</div>
                        <div class="btn btn-lg border border-primary my-4  w-25">Submit Payment</div>
                    </b-row>
                  
                </div>
                <div class="d-flex flex-row justify-content-end w-50 ">
                    <img class=" " src="~/assets/uploads/products/boutique.jpg" alt="Picture">
                </div>
            </div>
             
            <!-- <wrapper-draggable @change="changed"  tag="div"  class="container">
                <div   class=".some-item">
                    <h2>Item 1</h2>
                </div>
                <div  class=".some-item">
                    <h2>Item 2</h2>
                </div>
                <div  class=".some-item">
                    <h2>Item 3</h2>
                </div>

            </wrapper-draggable> -->
            
            <!-- <draggable v-model="somelist" tag="ul" >
                <li v-for="item in somelist" :key="item.id">
                    {{ item.data }}
                </li>
            </draggable>  -->
            <!-- Updated Product Section -->
            <b-col class="mt-5 pt-3 ">
                <b-row>
                    <h2 class = "w-25" >Shop Products</h2>
                   
                 </b-row>
                <ul id="products-div" class="row mt-4 list-unstyled"> 
                    
                    <li v-for="product in products" :key="product.prodID" 
                        class="d-flex flex-column align-items-center m-2 p-1"
                    >
                        <img class="product" :src=" 'http://localhost:8080/static/uploads/' + product.image"  alt=""> 
                        <h4 class="mt-3">{{product.prodName}}</h4>
                        <!-- <h6 class="text-center" :style="[{font: `300 0.75rem 'Poppins'`}, {width: '14rem'}]">{{product.desc}}</h6> -->
                        <h3>${{product.unit_price}}</h3>
                        <button @click="AddToCart(product.prodID)" class="btn mt-0  bg-secondary">Add to Cart</button>
                    </li>

            </ul>
             <b-pagination class="d-flex flex-row justify-content-center border-radius-0" 
                                  v-model="currentPage" 
                                  :total-rows="totalRows" 
                                  :per-page="perPage" 
                                  aria-controls="products-div"></b-pagination>
            </b-col>
         
            <!-- receipt section -->
            <b-row class="ml-0 mb-4 mt-2 pt-4 ">
                <div class="d-flex flex-row align-items-center justify-content-start ml-0 w-50 ">
                    <img style="position: absolute;
                                left:0;" 
                         class=" receipt-img" 
                         src="~/assets/uploads/products/boutique2.jpg" 
                         alt="Picture">
                </div>
                <div class="d-flex flex-column m-3  ">
                    <div class="mb-2 text-center">
                        <h3 > Welcome to my Boutique </h3>
                        <p> Young aspiring entrepreneur, spreading love and peace through style</p>
                    </div>
                    <div class="d-flex flex-column align-items-center ">
                        <b-form id="receipt-upload" class="form-style" @submit.prevent="SubmitPayment" method="POST" enctype="multipart/form-data">
                             <validation-provider v-slot="{ errors }" rules="required" name="order_no" >
                                <label for="order_no">Order Number</label>
                                <b-form-input class="my-2"
                                              v-model="form_fields.order_no" 
                                              type="text"
                                              id="order_no" 
                                              name="order_no"
                                              placeholder="e.g. 1010183632"
                                            :state="getValidationState(errors)">
                                </b-form-input>
                                <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
                            </validation-provider>

                             <validation-provider v-slot="{ errors }" rules="required" name="asset name" >
                                <label for="cust_name">Customer Name</label>
                                <b-form-input class="my-2"
                                              v-model="form_fields.cust_name" 
                                              type="text"
                                              id="cust_name" 
                                              name="cust_name"
                                              placeholder="e.g. Jane Doe"
                                            :state="getValidationState(errors)">
                                </b-form-input>
                                <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
                            </validation-provider>
                            <validation-provider rules="required|image" ref="provider" v-slot="{errors }">
                            
                                <label for="file_upload">Upload Proof of Payment</label>
                                <b-form-file
                                    class="my-2"
                                    v-model="form_fields.file_upload"
                                    id="file_upload"
                                    name="file_upload"
                                    placeholder="Choose a file or drop it here..."
                                    drop-placeholder="Drop file here..."
                                    @change="handleFileChange"
                                    ></b-form-file>
                                <b-form-invalid-feedback> {{ errors[0] }}</b-form-invalid-feedback>
                          </validation-provider>
                          <div class="d-flex flex-row text-white justify-content-center">
                            <button type="submit" class="btn btn-lg w-25 btn-primary"> 
                               Submit
                           </button>
                          </div>
                          
                           
                        </b-form>
                    </div>
                </div>
                
            </b-row>
            <!-- contact section -->
             <div id="contact">
                <h2>Contact us!</h2>
                <p>Contact us today, and get reply with in 24 hours!</p>

                <form id="contact-us" @submit.prevent="SendEmail" method="POST">
                    <fieldset>
                        <label for="name">Full Name</label>
                        <input placeholder="" type="text" tabindex="1" required >
                    </fieldset>
                    <fieldset>
                        <label for="mail">Email Address</label>
                        <input placeholder="" type="email" tabindex="2" required>
                    </fieldset>
                    <fieldset>
                        <label for="num">Phone Number</label>
                        <input placeholder="" type="tel" tabindex="3" required>
                    </fieldset>
                    <fieldset>
                        <label for="message">Message</label>
                        <textarea placeholder="" tabindex="5" required></textarea>
                    </fieldset>
                    <fieldset>
                        <button name="submit" type="submit" id="contact-submit" data-submit="...Sending">Submit</button>
                    </fieldset>
                </form>
    
            </div> 
     
        </div>
    </div>
</template>

<script>
import {ValidationObserver, ValidationProvider} from "vee-validate";
import WrapperDraggable from '../../../components/wrapper-draggable.vue';


export default {
    name: 'Website',
    layout: 'WebsiteLayout',
    components: {
        ValidationObserver, 
        ValidationProvider,
        WrapperDraggable,
     
    }, 
    head:{
        title: `Business Name Website`
    },
    data(){
        return{ 
            cart_confirm: '', 
            text: 'Shop Products',
            anotherlist: ['first', 'second'],
            somelist: [
                {
                    id: 1, 
                    data: 'sfkhg;fgh;eg'
                },
                {
                    id: 2, 
                    data: 'check'
                }
            ],
            currentPage: 1,
            perPage: 8,
            form: {
                    date: new Date().toISOString(),
                
                },
            form_fields: {
                order_no:'',
                cust_name: '',
                file_uplaod:'', 
            },
            sections:[
                1,1,1
            ],
            products: [],
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
                    self.products = res;
            
            }else{
                console.log('Data not found')
            }
            });

    
    },
    computed: {
        ProductList() {
            const items = this.products;
            return items.slice(
                (this.currentPage - 1) * this.perPage,
                this.currentPage * this.perPage,);
        },
        totalRows () {
            return this.products.length;
        },

    }, 
    
    methods:{
        changed(event){
            const element = event.moved.element;      
            const oldIndex = event.moved.oldIndex;
            const newIndex = event.moved.newIndex;
            console.log(`Old index ${oldIndex}`);
            console.log(`New index ${newIndex}`);
            element.id
            let moved_element = document.getElementById(element.id);
            moved_element.id = newIndex;

            let other = document.getElementById(oldIndex);
            other.id = oldIndex;
            // this.history.push(`${element.name} is moved from position ${oldIndex} to ${newIndex}`);
          

        },
        getValidationState(errors) {
                return errors.length > 0 ? false : null;
            },

        onSubmit() {
            alert(JSON.stringify(this.form))
        },
        resetForm() {
            this.form = {};
            this.$nextTick(() => {
                this.$refs.observer.reset();
            });

        },
        async handleFileChange(e) {
        const { valid } = await this.$refs.provider.validate(e);

        if (valid) {
            // TODO: Upload the file
            console.log('Uploaded the file...');
        }
        },
        AddToCart(product_id){
            let self = this; 
            var cart = localStorage.getItem('cart');

            // Checks if cart exists else create new object
            cart = cart ? JSON.parse(cart) : {};
            // console.log( 'initial cart', cart )

            // check if key exists
            let hasKey = cart.hasOwnProperty("Product"+product_id);
            // console.log(product_id,hasKey);

            if (hasKey){
                this.cart_confirm = 'Product already in cart';
                console.log('Product in cart');
                
            }else{
                // Add new Product to the cart 
                cart[`Product${product_id}`] = product_id;
                
                // Save back to localStorage
                localStorage.setItem('cart', JSON.stringify(cart));

                // console.log('Updated String Cart', cart);
                this.cart_confirm = 'Product already in cart';
                console.log('Product added to cart.');                
            }
        }, 

        SubmitPayment: function () {
            let self = this;
            let paymentForm = document.getElementById("receipt-upload");
            let form_data = new FormData(paymentForm);
            let PATH_API = 'proof-payment';
                this.$axios.post(`/api/${PATH_API}`, form_data, {
                  headers: {
                  'contentType': 'application/json',
                }
              })
              .then( jsonResponse =>{
                return jsonResponse.data;
              })
              .then( jsonResponse =>{
                console.log(jsonResponse);
                self.alert_message = jsonResponse.message;
              })
            }, 

        SendEmail: function () {
            let self = this;
            let contactForm = document.getElementById("contact-us");
            let form_data = new FormData(contactForm);
            let PATH_API = 'website/contact';
                this.$axios.post(`/api/${PATH_API}`, form_data, {
                  headers: {
                  'contentType': 'application/json',
                }
              })
              .then( jsonResponse =>{
                return jsonResponse.data;
              })
              .then( jsonResponse =>{
                console.log(jsonResponse);
                self.alert_message = jsonResponse.message;
              })
            }, 
    }
}

</script>


<style scoped>
.wrapper{
    margin: 2em;
}

.product{
    width: 18rem;
    height: 18rem;
}
.form-style{
    display:flex;
    flex-direction: column;
    justify-content: center;
    width: 24rem;
}
b-form-input{
    width: 2rem;
}
</style>