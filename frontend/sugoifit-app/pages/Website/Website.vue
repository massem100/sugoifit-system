<template>
    <div class="wrapper">

        <div class="container">
            <!-- welcome section -->
            <b-container class="mb-5">
                <b-row>
                    <b-col >
                        <h2>Welcome to my Boutique</h2>
                        <h4>Young aspiring entrepreneur, spreading love and peace through style.</h4>
                    </b-col>
                    <b-col >
                        <img class=" welcome-img" src="~/assets/uploads/boutique.jpg" alt="Picture">
                    </b-col>
                    
                </b-row>
            </b-container>
            

            <!-- product section -->
            <div class="products">
                <Slider />
            </div>
            

            <!-- receipt section-->
            <b-container class="mt-5">
                <b-row>
                    <b-col >
                        <img class=" receipt-img" src="~/assets/uploads/boutique2.jpg" alt="Picture">
                    </b-col>
                    <b-col >
                        <h2>Payment Receipt</h2>
                        <h4>Please upload proof of payment to start processing your order.</h4>
                        <CustomerForm buttonText="Upload" 
                                        :submitForm="uploadReceipt"
                                        hasTRN="true"
                                        hasInvoice="true"
                                        hasImage="true"
                        />
                    </b-col>
                </b-row>
            </b-container>


            <!-- contact section -->
            <b-container class="mt-5">
                <b-row>
                    <b-col>
                        <CustomerForm buttonText="Upload" 
                                        :submitForm="uploadReceipt"
                                        hasName="true"
                                        hasEmail="true"
                                        hasPhone="true"
                                        hasMessage="true"
                        />
                    </b-col>
                    <b-col >
                        <h2 class="text-center" >Contact us!</h2>
                        <h4>Contact us today, and get reply within 24 hours!</h4>
                        <b-col cols="12" >
                            <h4>{{items.address}}</h4>
                        </b-col>
                        <b-col cols="12" >
                            <h4>{{items.email}}</h4>
                        </b-col>
                        <b-col cols="12" >
                            <h4>{{items.phone}}</h4>
                        </b-col>
                    </b-col>
                </b-row>
            </b-container>
            
        </div>
    </div>
</template>

<script>
import CustomerForm from '../../components/CustomerForm';
import Slider from '../../components/ImageSlider';
export default {
    name: 'Website',
    layout: 'website',
    components: {
        Slider,
        CustomerForm
    },
    data() {
        return {
            items: {
                address:"Montego Bay, Jamaica",
                phone: "(876)971-1234",
                email: "monique.boutique@gmail.com"
            }
        }
    },
    methods: {
        uploadReceipt(form) {
            console.log(form);
        },
        getValidationState(errors) {
            return errors.length > 0 ? false : null;
        },
        
        uploadMessage() {
            let self = this;
            let customerForm = document.getElementById("customerForm");
            let form_data = new FormData(customerForm);
            /* ADD busID - form_data.append() */

            let PATH_API = 'contact';
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
}
.container{
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.welcome-img{
    width: 450px;
    height: 300px;
    box-shadow: 3rem -20px rgb(46, 158, 102);
}

.receipt-img{
    width: 500px;
    height: 400px;
    box-shadow: -3em -20px rgb(46, 158, 102);
}
</style>