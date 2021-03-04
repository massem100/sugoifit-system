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
                        <h6>Cost Breakdown</h6>
                        <p>Item Cost: JMD 2000.99</p>
                        <p>Delivery Cost/Pick up: JMD 500.00</p>
                        <p>Total Cost: JMD 2500.99</p>
                    </div>
                    <div class="right-btn">
                        <button type="submit">Checkout</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="bottom">
            <div class="column">
                <h6>Your Almost Done</h6>
                <p>Please fill out the form below.</p>
                <form id="contact" action="" method="post">
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
                    <textarea placeholder="" tabindex="5" required></textarea>
                </fieldset>
                <fieldset>
                    <button name="submit" type="submit" id="order-submit" data-submit="...Sending">Submit</button>
                </fieldset>
            </form>
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
    justify-content: flex-start;
    margin: 3em;
}
.column {
    width: 25%;
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
.contact{
    margin: 3em;
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
#order-submit{
    border-radius: 15px;
    color: white;
    font-size: 20px;
    background-color: rgb(46, 158, 102);
    padding: 15px;
}
</style>
