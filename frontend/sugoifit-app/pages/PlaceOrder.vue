<template>
    <div class="container">
        <div class="header">
            <WebsiteHeader />
        </div>
        <div class="top">
            <div class="left">
                <div class="column">
                    <div class="card">
                        <div class="card-image">
                            <img src="~/assets/uploads/products/skirt1.jpg" alt="Picture" style="width:50%">
                        </div>
                        <div class="card-text">
                            <p class="quantity">Quantity:</p>
                            <p class="size">Size:</p>
                            <p class="colour">Colour:</p>
                            <p class="price">Price:</p>
                        </div>
                    </div>
                </div>
                <div class="column">
                    <div class="card">
                        <div class="card-image">
                            <img src="~/assets/uploads/products/pants3.jpg" alt="Picture" style="width:50%">
                        </div>
                        <div class="card-text">
                            <p class="quantity">Quantity:</p>
                            <p class="size">Size:</p>
                            <p class="colour">Colour:</p>
                            <p class="price">Price:</p>
                        </div>
                    </div>
                </div>
                <div class="column">
                    <div class="card">
                        <div class="card-image">
                            <img src="~/assets/uploads/products/top1.jpg" alt="Picture" style="width:50%">
                        </div>
                        <div class="card-text">
                            <p class="quantity">Quantity:</p>
                            <p class="size">Size:</p>
                            <p class="colour">Colour:</p>
                            <p class="price">Price:</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="right">
                <div class="column">
                    <div class="right-text">
                        <h2>Cost Breakdown</h2>
                        <p>Item Cost: JMD 2000.99</p>
                        <p>Delivery Cost/Pick up: JMD 500.00</p>
                        <p>Total Cost: JMD 2500.99</p>
                    </div>
                    <div class="right-btn">
                        <button id="checkout-btn" type="submit">Checkout</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="bottom">
            <div class="bottom-left">
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
            <div class=bottom-right>
                <img src="~/assets/uploads/products/boutique.jpg" alt="Picture">
            </div>
        </div>
        
    </div>
</template>

<script>
import WebsiteHeader from '../components/WebsiteHeader';
export default {
    name: 'PlaceOrder',
    components: {
        WebsiteHeader
    }
}
</script>

<style scoped>
.container{
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.top{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 5em;
}
.right{
    line-height: 3em;
}
#checkout-btn{
    height: 50px;
    width: 170px;
    border-radius: 15px;
    color: white;
    font-size: 20px;
    background-color: rgb(46, 158, 102);
}
.column {
    width: 100%;
    display: flex;
    flex-direction: column;
    margin: 0 auto;
    border-radius: 5px;
    overflow: hidden;
    z-index: 0;
}
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
.bottom{
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    margin: 3em;
}
.bottom-right{
    flex: 1 1 auto;
}
.bottom-right > img{
    width: 300px;
    height: 300px;
    box-shadow: 3rem -20px rgb(46, 158, 102);
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
  width:50%;
  padding:.3em;
  font-size:20px;
  border: none;
  background-color: rgba(119, 255, 187, 0.705);
  border-radius: 20px;
  resize:vertical;
}
 
#order-submit{
    border-radius: 15px;
    color: white;
    font-size: 20px;
    background-color: rgb(46, 158, 102);
    height: 50px;
    width: 170px;
    align-content: right;
}
</style>
