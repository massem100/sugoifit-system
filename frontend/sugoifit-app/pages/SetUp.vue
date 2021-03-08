<template>
   <div id="entirePage">
       <div id="logo">
                <h2>SugoiFit</h2>
        </div>
        <div id="leftColumn">
            
            <div id="photoHolder">
                <div id="circle">
                    

                </div>
                <p style="left:55px;">Add Photo</p>

            </div>
        </div>

        <div id="middleColumn">
            <form> 
                <div style="float:left;">
                    <label for="bName">Business Name</label>
                    <input type="text" name="bName" id="bus_Name">
                </div>
                <br>
                <div style="float:left;">
                    <label for="telNum">Telephone</label>
                    <input type="tel" name="telephone" id="telNum">
                </div>
                <br>
                <div style="float:left;">
                    <label for="email">E-Mail</label>
                    <input type="email" name="email" id="email">
                </div>
                <br>
                <div>
                    <button id="continueBtn" type="button">Continue</button>
                </div>

            </form>
        </div>
        <div id="rightColumn">
            <div style="float:left;">
                <label for="city">City</label>
                <input type="text" name="city" id="city">
            </div>
            <br>
            <div style="float:left;">
                <label for="parish">Parish</label>
                <input type="text" name="parish" id="parish">
            </div>
            <br>
            <div style="float:left;">
                <label for="country">Country</label>
                <input type="text" name="country" id="country">
            </div>
            <br>
            <div style="float:left;">
                <label for="zip">Zip</label>
                <input type="number" name="zip" id="zip">
            </div>

        </div>
        <div  id="displayMsg">
                    <p style="font-size: 24px">Managing your business, has never been
                        this easy. </p>
                    <p style="font-weight:normal">Let’s get you set up.  Enter your 
                        information below to make invoicing your clients a breeze.</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SetUp',
    data(){
        return{

        }
    }
    
}
</script>

<style scoped>
    @media(min-width: 768px){
        #entirePage{
            display:grid;
            align-items:center;
            justify-content: center;
            grid-template-rows: auto;
            column-gap: 2%;
            grid-template-columns: 500px 500px 500px 300px;
            grid-template-areas: 
            ". displayMsg displayMsg ."
            "leftColumn middleColumn rightColumn .";

        }
    }
    
    input[type=text], input[type=password],input[type=number],input[type=email],input[type=tel] {
        align-content: center;
        width: 500px;
        height: 45px;
        left: 392px;
        top: 171px;
        border: none;
        background: #DFFBFF;
        border-radius: 15px;
        /*display:block;*/
        
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
    #continueBtn{
        background-color: #4DC4D4;
        color: white;
        padding: 14px 20px;
        margin: 10px 0;
        border: none;
        cursor: pointer;
        border-radius: 10px;
        height: 45px;
    }

    #leftColumn{
        grid-area: leftColumn;
        padding-left: 40%;
        display: flex;
        flex: column;
        align-items: center;
    }
    #rightColumn{
        grid-area: rightColumn;
        padding-top:10px;
        padding-right: 10px;
        padding-left: 10px;
    }
    #displayMsg{
        grid-area: displayMsg;
        padding-top: 10%;
        padding-bottom: 10px;
    }
    #middleColumn{
        grid-area: middleColumn;
        padding-top:10px;
        padding-right: 10px;
    }

    #circle{
        width: 120px;
        height: 120px;
        left: 55px;
        top: 162px;
        background: #F0F0F0;
        border-radius: 50%;

    }

</style>