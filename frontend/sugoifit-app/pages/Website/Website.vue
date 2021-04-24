<template>
    <div class="wrapper">

        <div class="header">
            <WebsiteHeader />
        </div>

        <div class="container">
            <!-- welcome section -->
            <div class="welcome">
                <div class="welcome-left">
                    <div class="text">
                        
                        <h2> Welcome to my Boutique </h2>
                        <h4> Young aspiring entrepreneur, spreading love and peace through style</h4>
                    </div>
                    <div class="btn">
                        <button type="submit" class="submitbtn"> Place an Order</button>
                    </div>
                </div>
                <div class="welcome-right">
                    <img src="~/assets/uploads/boutique.jpg" alt="Picture">
                </div>
            </div>

            <!-- product section -->
            <div class="products">
                <Slider />
            </div>
            

            <!-- receipt section -->
            
            <div class="receipt">
                <div class="receipt-left">
                    <img class=" receipt-img" src="~/assets/uploads/boutique2.jpg" alt="Picture">
                </div>
                <div class="receipt-right">
                    <PaymentReceipt />
                </div>
                
            </div>
            <!-- contact section -->
            <div class="contact">
                <h2>Contact us!</h2>
                <p>Contact us today, and get reply with in 24 hours!</p>

                <form id="contact" action="" method="post">
                    <fieldset>
                        <label for="name">Full Name</label>
                        <input placeholder="" type="text" tabindex="1" required autofocus>
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
import PaymentReceipt from '../../components/receiptForm';
import Slider from '../../components/ImageSlider';
import WebsiteHeader from '../../components/WebsiteHeader';
export default {
    name: 'Website',
    components: {
        WebsiteHeader,
        Slider,
        PaymentReceipt
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
.welcome{
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    margin: 3em;
}
.welcome-left{
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    align-items: baseline;
    line-height: 3em;
}
.welcome-right{
    flex: 1 1 auto;
}
.submitbtn{
    border-radius: 15px;
    color: white;
    font-size: 20px;
    border: none;
    background-color: rgb(46, 158, 102);
    padding: 15px;
}
.welcome-right > img{
    width: 300px;
    height: 300px;
    box-shadow: 3rem -20px rgb(46, 158, 102);
}

.receipt{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 3em;
}
.receipt-left{
    line-height: 3em;
}
.receipt-img{
    width: 400px;
    height: 400px;
    box-shadow: -3em -20px rgb(46, 158, 102);
}
.contact{
    margin: 3em;
    position: center;
}
fieldset{
    padding: 10px 5px;
}
label{
  display:block;
  margin:1em 0 .2em;
}
input, textarea{
  display:block;
  width:75%;
  padding:.3em;
  font-size:20px;
  border: none;
  background-color: rgba(119, 255, 187, 0.705);
  border-radius: 20px;
  resize:vertical;
}
textarea{
  min-height:180px;
}
form{
    align-items: center;
}
#contact-submit{
    height: 3em;
    width: 170px;
    border-radius: 15px;
    color: white;
    font-size: 15px;
    background-color: rgb(46, 158, 102);
}
</style>