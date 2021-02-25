<template>
    <div class="container">
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
                <img src="../assets/products/boutique.jpg" alt="Picture">
                <div class="image-shadow"></div>
            </div>
        </div>

        <!-- product section -->
        <div class="products">
            <div class="column">
                <div class="box">
                    <img src="../assets/products/skirt1.jpg" alt="Picture" style="width:100%">
                    <h6>Skirt</h6>
                    <p class="price">$19.99</p>
                </div>
            </div>
            <div class="box">
                <img src="../assets/products/skirt2.jpg" alt="Picture" style="width:100%">
                <h6>Skirt</h6>
                <p class="price">$19.99</p>
            </div>
            <div class="box">
                <img src="../assets/products/skirt3.jpg" alt="Picture" style="width:100%">
                <h6>Skirt</h6>
                <p class="price">$19.99</p>
            </div>
            <div class="box">
                <img src="../assets/products/top5.jpg" alt="Picture" style="width:100%">
                <h6>Top</h6>
                <p class="price">$19.99</p>
            </div>
            <div class="box">
                <img src="../assets/products/top3.jpg" alt="Picture" style="width:100%">
                <h6>Top</h6>
                <p class="price">$19.99</p>
            </div>
            <div class="box">
                <img src="../assets/products/top1.jpg" alt="Picture" style="width:100%">
                <h6>Top</h6>
                <p class="price">$19.99</p>
            </div>
            <div class="box">
                <img src="../assets/products/dress5.jpg" alt="Picture" style="width:100%">
                <h6>Dress</h6>
                <p class="price">$19.99</p>
            </div>
            <div class="box">
                <img src="../assets/products/dress3.jpg" alt="Picture" style="width:100%">
                <h6>Dress</h6>
                <p class="price">$19.99</p>
            </div>
            <div class="box">
                <img src="../assets/products/dress1.jpg" alt="Picture" style="width:100%">
                <h6>Dress</h6>
                <p class="price">$19.99</p>
            </div>
            <div class="box">
                <img src="../assets/products/pants3.jpg" alt="Picture" style="width:100%">
                <h6>Pants</h6>
                <p class="price">$19.99</p>
            </div>
            <div class="box">
                <img src="../assets/products/pants4.jpg" alt="Picture" style="width:100%">
                <h6>Pants</h6>
                <p class="price">$19.99</p>
            </div>
            <div class="box">
                <img src="../assets/products/pants2.jpg" alt="Picture" style="width:100%">
                <h6>Pants</h6>
                <p class="price">$19.99</p>
            </div>
        </div>

        <!-- receipt section -->
        <div class="receipt">
            <div class="receipt-left">
                <img src="../assets/products/boutique2.jpg" alt="Picture">
                <div class="image-shadow2"></div>
            </div>
            <div class="left">
                <div class="text">
                    <h3> Welcome to my Boutique </h3>
                    <p> Young aspiring entrepreneur, spreading love and peace through style</p>
                </div>
                <div class="form">
                    <form id="contact" action="" method="post">
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
                    <label for=""></label>
                    <input placeholder="" type="url" tabindex="4" required>
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
export default {
    name: 'Home',
    data() {
        return {
            
        }
    }
}
</script>

<style scoped>
.container{
  display: flex;
  flex-direction: column;
}
.welcome{
    display: flex;
    justify-content: flex-start;
}
.welcome-left{
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
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
    content: "";
    display: table;
    clear: both;
}
.column {
    float: left;
    width: 25%;
    padding: 0 10px;
}
.box{
    width: 300px;
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
    justify-content: flex-start;
}
.receipt-left{
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
}
.receipt-right > img{
    width: 300px;
    height: 300px;
    box-shadow: 3rem 20px rgb(46, 158, 102);
}
.receipt-right{
    flex: 1 1 auto;
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