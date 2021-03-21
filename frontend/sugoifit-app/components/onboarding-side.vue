<template>
    <div class="side-nav-on"> 
        <!-- The inner divs will be triggered by a v-if to toggle active class/display -->
        <div class="w-100">
            <!-- I want to make the sidebar dynamic so when its time to change
             the company type instead of the list its illustration or words -->
            <div class="sugoifit-name">
                <img class = "logo" src="~assets/uploads/logo.png" alt="">
                <h5 class = ""> SugoiFIt App</h5>
            </div>

            <ul class = "list-nav d-flex flex-column"> 
                    <!-- <img class = "checked" src="~assets/uploads/checked.svg" alt=""> -->
                <li><span>1</span>Company Type </li>
                <li><span>2</span>Business Details </li>
                <li><span>3</span>Business Location </li>
                <li><span>4</span> Team </li>
                <li><span>5</span> Personal Details</li>
            </ul>

            <div class = "onboard-footer">

            </div>
              
        </div>
        
    </div>
</template>

<script>
export default {
    name: 'onboardingSide'
}
</script>

<style scoped>
 
    .side-nav-on{
        display:grid;
        grid-template-areas: "tophead"
                                "list";
        margin: 20px;
        min-width: 18rem; 
        min-height: 100vh;
        /* padding:25px; */
        /* border-right: 1px solid rgba(112,112, 0.05); */
        background-color: rgb(79, 201, 218,0.5);
        
    }

    .list-nav{
        margin: 5px;
    
        padding: 10px;
        list-style-type: none;
        /* background-color: blueviolet; */
        grid-area: list;
        height: 80vh;
        /* color:white; */
    }
    .list-nav li{
        margin: 4px;
        padding: 5px;
        font: 400 1rem "Poppins";
        /* text-transform: uppercase; */
        color:rgb(43, 42, 42);
    }
    .list-nav li span{
        margin: 7px 10px;
        height: 25px;
        width: 25px;
        text-align: center;
        display: flex;
        /* align-items: center; */
        border-radius: 50%;
        display: inline-block;
        border: 2px solid #e6f3f3;
        color: #ffffff;

    }
    .logo{
        margin:10px;
        width: 24px; 
        height: 24px;
    }
    .sugoifit-name{
        margin:5px;
        display: flex;
        flex-direction: row ;
        align-items: center;
        /* background-color: violet; */
        grid-area: tophead;
        height:10vh;
        vertical-align: middle;
        color: white;
    }

    .sugoifit-name h4{
        
        
    }

    .checked{
        width:24px; 
        height:24px;
        margin: 5px;

    }

    .onboard-footer{
        position:absolute;
        top: 20rem;
        left:10rem;
        background: url(~assets/uploads/onboard-footer.svg);
        width: 20rem;
        /* height: 100%;
        /* z-index: 1; */
    }
    
    /* Extra small devices (phones, 600px and down) */
@media only screen and (max-width: 600px) {
    .color-bg{
        /* background-color: green; */
    }
    

}

/* Small devices (portrait tablets and large phones, 600px and up) */
@media only screen and (min-width: 600px) {
    .color-bg{
        /* background-color: purple; */
    }
   
}

/* Medium devices (landscape tablets, 768px and up) */
@media only screen and (min-width: 768px) {
    .color-bg{
        /* background-color: yellow; */
    }
   }

/* Large devices (laptops/desktops, 992px and up) */
@media only screen and (min-width: 992px) {
    .color-bg{
        /* background-color: red; */
    }
    .side-nav-on{
        min-width: 18rem;
        
    }
}

/* Extra large devices (large laptops and desktops, 1200px and up) */
@media only screen and (min-width: 1200px) {
    .color-bg{
        /* background-color: blue; */
    }
    
}
</style>