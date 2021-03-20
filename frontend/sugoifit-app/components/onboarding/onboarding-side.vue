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

                <li><span><img class = "checked" src="~assets/uploads/checked.svg" alt=""></span>Company Type </li>
                <li><span><img class = "checked" src="~assets/uploads/checked.svg" alt=""></span>State </li>
                <li><span><img class = "checked" src="~assets/uploads/checked.svg" alt=""></span>Business Details </li>
                <li><span><img class = "checked" src="~assets/uploads/checked.svg" alt=""></span> Team </li>
                <li><span><img class = "checked" src="~assets/uploads/checked.svg" alt=""></span> Personal Details</li>
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
        width: 20rem; 
        height: 100vh;
        /* padding:25px; */
        /* border-right: 1px solid rgba(112,112, 0.05); */
        background-color: #F0F0F0;
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
        margin: 5px;
        padding:10px;
        font: 400 1rem "Poppins";
        text-transform: uppercase;
    }
    .list-nav li span{
        margin:5px;
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
</style>