<template>

<div class = "wrapper bg-white "> 
    <b-nav class="m-4 mr-5 p-2">
        <b-nav-item class = "h3" active>Monique Boutique</b-nav-item>
        <b-row class="ml-lg-auto">
            <b-nav-item active>Products</b-nav-item>
            <!-- <b-nav-item>FAQ</b-nav-item> -->
            <b-nav-item>Contact</b-nav-item>
            
            <b-nav-item>
                <nuxt-link class="btnStyle pop-link" :to="{name:'website-placeorder'}">Shopping Cart</nuxt-link>
            </b-nav-item>
            <!-- <b-nav-item disabled>Disabled</b-nav-item> -->
            
         </b-row>
  </b-nav>
  <div class="nuxt-wrapper"> 
         <nuxt />
  </div>
 
  <footer class= "footer bg-primary">
      <h4 class="ml-4 mb-0 text-white"> Monique Boutique 2021</h4>
  </footer>
</div>

</template>
    

<script>
export default {
    
    
}
</script>

<style scoped>
.wrapper {
    min-height: 100%;
    display: flex;
    flex-direction: column;
    
}
.nuxt-wrapper{
    width:100%;
    min-height: 100vh;
}
 
    .side-nav-on{
        position:fixed;
        display:grid;
        grid-template-areas: "tophead"
                                "list";
        margin: 20px;
        min-width: 18rem; 
        /* min-height: 200%; */
        /* padding:25px; */
        /* border-right: 1px solid rgba(112,112, 0.05); */
        background-color: #A7E4EC;
        
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
 

/* Large devices (laptops/desktops, 992px and up) */
@media only screen and (min-width: 992px) {
    .color-bg{
        /* background-color: red; */
    }
    .side-nav-on{
        min-width: 18rem;
        
    }
}

</style>