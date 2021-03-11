<template>
    <div class="container">
        <div class="header">
            <WebsiteHeader />
        </div>
        
        <!-- welcome section -->
        <div class="welcome">
            <div class="welcome-left">
                <div class="text">
                    <h3> Welcome to my Boutique </h3>
                    <p> Young aspiring entrepreneur, spreading love and peace through style</p>
                </div>
                <div class="btn">
                    <button type="submit" class="submitbtn"> Place and Order</button>
                </div>
            </div>
            <div class="welcome-right">
                <img src="~/assets/uploads/products/boutique.jpg" alt="Picture">
            </div>
        </div>

        <!-- product section -->
        <div class="products">
            <Slider />
        </div>
        

        <!-- receipt section -->
        <div class="receipt">
            <div class="receipt-left">
                <img class=" receipt-img" src="~/assets/uploads/products/boutique2.jpg" alt="Picture">
            </div>
            <div class="receipt-right">
                <div class="receipt-text">
                    <h3> Welcome to my Boutique </h3>
                    <p> Young aspiring entrepreneur, spreading love and peace through style</p>
                </div>
                <div class="form">
                    <form id="receipt-upload" action="" method="post">
                        <fieldset>
                            <input placeholder="Order No." type="text" tabindex="1" required autofocus>
                        </fieldset>
                        <fieldset>
                            <input placeholder="Customer Name" type="email" tabindex="2" required>
                        </fieldset>
                        <fieldset>
                            <input placeholder="Upload File" type="tel" tabindex="3" required>
                        </fieldset>
                        <fieldset>
                            <button name="submit" type="submit" id="receipt-submit" data-submit="...Sending">Submit</button>
                        </fieldset>
                    </form>
                </div>
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
</template>

<script>
import Slider from '../components/ImageSlider';
import WebsiteHeader from '../components/WebsiteHeader';
export default {
    name: 'Website',
    components: {
        WebsiteHeader,
        Slider
    }
    
}
</script>

<style scoped>

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


.products{
    margin: 3em;
    display: grid;
    grid-template-columns: auto auto auto auto;
    grid-gap: 10px 20px;
}
.box{
    width: 40%;
    min-height: 120px;
    max-height: auto;
    float: left;
    margin: 3px;
    padding: 3px;
    font-size: 10px;
    text-align: center;
}
.box > img{
    max-width: 100%;
    height: auto;
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
#receipt-submit{
    height: 50px;
    width: 150px;
    border-radius: 15px;
    color: white;
    font-size: 20px;
    background-color: rgb(46, 158, 102);
}
.contact{
    margin: 3em;
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
    border-radius: 15px;
    color: white;
    font-size: 20px;
    background-color: rgb(46, 158, 102);
    padding: 15px;
}
</style>