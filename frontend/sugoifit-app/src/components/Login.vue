<template>
    
    <div id="entirePage">
        <div id="header">
            <br>
            <h2> SugoiFit Login </h2>
        </div>
         <div class = 'main-area'>
                <form>
                    <br>
                    <br><br>
                    Email:<br>
                    <input type="text" name="email" id="email">
                    <br><br>
                    Password:<br>
                    <input type="text" name="password" id="password">
                </form>

            </div>

            
            <div id="square2">

            </div>
            <div id="square1">

            </div>
            
            

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
</template>

<script>
export default {
    name: 'Login',
    data(){

    }
}
</script>

<style scoped>

    input[type=text], input[type=password] {
        align-content: left;
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
        height: 268px;
        left: 134px;
        top: 84px;

        background: #DFFBFF;
    }

    #square1{
        position: absolute;
        width: 196px;
        height: 268px;
        left: 36px;
        top: 120px;

        background: #7CC3CD;
    }

</style>