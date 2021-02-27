<template>
    
    <div class="entirePage">
        <h2 id='logo'>SugoiFit</h2>
        <div  class='sidebar'>
            

            <div id="square1">

            </div>
            <div id="square2">

            </div>
        </div>
        
        <div class='main-area'>
                <div id="header">
                    <br>
                    <h2> Login </h2>
                    <br>
                </div>
                <div> 
                    <p>Welcome back, enter your username and password</p>
                </div>

                <form>
                    <br>
                    <br><br>
                    Email:<br>
                    <input type="text" name="email" id="email">
                    <br><br>
                    Password:<br>
                    <input type="text" name="password" id="password">
                </form>
                <div  id="msgBox">
                    <p> {Display error messages here} </p>
                </div>

                <div>
                    <button class="submit" id="submit" type="button">Submit</button>
                </div>

                <div> 
                    <a href=""> Dont have an account? Sign up your business! </a>
                </div>

        </div>   
    </div>
</template>

<script>
export default {
    name: 'Login',
    data(){
        return{

        }

    }
}
</script>

<style scoped>

    input[type=text], input[type=password] {
        align-content: center;
        width: 500px;
        height: 45px;
        left: 392px;
        top: 171px;
        border: none;
        background: #DFFBFF;
        border-radius: 15px;
        
    }

    
    button {
    background-color: #4DC4D4;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 12%;
    border-radius: 10px;
    
    }

    #msgBox{
        padding-top: 3%;
    }

    h2{
      font-family: fantasy; 
      color: black; 
    }

    #square2{
        position: absolute;
        width: 196px;
        height: 280px;
        left: 134px;
        top: 70px;

        background: #DFFBFF;
    }

    #square1{
        position: absolute;
        width: 196px;
        height: 280px;
        
        left: 36px;
        top: 120px;

        background: #7CC3CD;
    }

    @media(min-width: 768px){
        .entirePage{
            display:flex;
            align-items:center;
            justify-content: center;
            position: fixed;
            top: 0;
            left: 0;
            bottom: 0;
            right: 0;
            overflow: auto;
        
        }
    }

    .sidebar{
        flex: 1;
        padding-left: 15%;
        padding-bottom: 30%;
        align-items: flex-start;
        position: relative;
        left: 10%;
        top: 0%;
    
    }

    .main-area{
        flex: 3;
        padding-right: 20%;
    }

    #logo{
        position: absolute;
        top: 10%;
        left: 14%
    }
    
</style>