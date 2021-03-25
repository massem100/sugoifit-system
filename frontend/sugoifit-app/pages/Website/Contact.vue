<template>
    <div class="wrapper">
        
        <div class="header">
            <WebsiteHeader />
        </div>
        <div class="conatainer">
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
import WebsiteHeader from '../../components/WebsiteHeader';
export default {
    name: 'Contact',
    components: {
        WebsiteHeader
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
.contact{
    margin: 3em;
    position: relative;
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
