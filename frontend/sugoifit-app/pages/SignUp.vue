<template>
    <div id="entirePage">
        <div id="logo">
                <h2>SugoiFit</h2>
        </div>
        <div id="leftColumn">
            
            <div id="logoHolder">
                <div id="square1">

                </div>
                <div id="square2">

                </div>

            </div>
        </div>

        <div id="rightColumn">
            <h4> Sign Up </h4>
            <p>Welcome to SugoiFit! Fill out the form to Sign Up.</p>
            <form> 
                <div style="float:left;">
                    <label for="firstname">First Name</label>
                    <input type="text" name="firstname" id="firstname">
                </div>
                <br>
                <div style="float:left;">
                    <label for="lastname">Last Name</label>
                    <input type="text" name="lastname" id="lastname">
                </div>
                <br>
                <div style="float:left;">
                    <label for="b_name">Business Name</label>
                    <input type="text" name="b_name" id="b_name">
                </div>
                <br>
                <div style="float:left;">
                    <label for="email">E-Mail</label>
                    <input type="email" name="email" id="email">
                </div>
                <br>
                <div style="float:left;">
                    <label for="password">Password</label>
                    <input type="password" name="password" id="password">
                </div>
                <br>
                <div style="float:left;">
                    <label for="password2">Confirm Password</label>
                    <input type="password" name="password" id="password2">
                </div>
                <br>
                <div style="float:left;">
                    <label for="revenue">Revenue</label>
                    <input type="number" name="revenue" id="revenue" pattern="^\d*(\.\d{0,2})?$">
                </div>
            

                <div id="disclaimer">
                    <p><small>This information will not be saved but used only
                    to determine the scale of your business </small> </p>
                </div>

                <div  id="msgBox">
                    <p> {Display error messages here} </p>
                </div>

                <div>
                    <button id="submitBtn" type="button">Sign Up</button>
                </div>

                <div> 
                    <a href=""> Dont have an account? Sign up your business! </a>
                </div>
            </form>

            
        </div>
    </div>
    
</template>

<script>
export default {
    name: 'SignUp',
    data(){
        return{

        }
    }
    
}
</script>

<style scoped>
    @media(min-width: 768px){
        #entirePage{
            display:flex;
            align-items:center;
            justify-content: center;
        }
    }
    
    input[type=text], input[type=password],input[type=number],input[type=email] {
        align-content: center;
        width: 500px;
        height: 45px;
        left: 392px;
        top: 171px;
        border: none;
        background: #DFFBFF;
        border-radius: 15px;
        display:block;
        
    }

    label{
        display:block;
    }

    #submitBtn{
        background-color: #4DC4D4;
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        cursor: pointer;
        width: 35%;
        border-radius: 10px;
    }

    #logo{
        position: absolute;
        top: 5%;
        left:5%;
        
    }

    h2{
      font-family: fantasy; 
      color: black; 
    }
    h4{
      font-family: fantasy; 
      color: black; 
    }


    #square2{
        position: absolute;
        width: 216px;
        height: 300px;
        left: 134px;
        top: 70px;

        background: #DFFBFF;
    }

    #square1{
        position: absolute;
        width: 216px;
        height: 300px;
        
        left: 36px;
        top: 120px;

        background: #7CC3CD;
    }

    #leftColumn{
        flex: 5%;
        padding-left: 15%;
        padding-bottom: 30%;
        align-items: flex-start;
        position: relative;
        left: 10%;
        top: 0%; 
        
    
    }

    #rightColumn{
        padding-top: 5%;
        padding-right: 35%;
        
        
    }

</style>