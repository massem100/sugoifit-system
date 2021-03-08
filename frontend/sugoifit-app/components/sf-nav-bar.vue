<template>
    <nav class = "d-flex flex-row nav-bar bg-primary ">
        <div class="d-flex flex-row align-items-center">
            <h4 class ="">SugoiFit</h4>
            <div class ="d-flex flex-row">
                <div class="ml-auto"> 
                    <ul class ="nav-items-ul ">
                        <li class="nav-items-li ">Features</li>
                        <li class="nav-items-li">Who It's For</li>
                        <li class="nav-items-li">Resources</li>
                        <li class="nav-items-li">Pricing</li>
                    </ul>
                </div>
                <div class="d-flex flex-row align-items-center ">
                    <ul class="d-flex">
                        <li class="nav-items-li">(888) 543 0978 </li>
                        <li class="nav-items-li">Contact Us</li>
                        <li class="nav-items-li">TRY IT FREE</li>
                    </ul>
                    <div class="login-btn">Login</div>

                </div>
            </div>
        </div>

    </nav>
</template>

<script>
export default {
    name: 'NavBar',
    
}
</script>

<style scoped>

    .nav-bar{
        width: 100vh;
    }
    .nav-items-ul{
        display:flex;
        align-items: center;

    }
    .nav-items-li{
        display:flex;
        list-style: none;
        margin: 10px;
        text-align: center;
        justify-content:center;
        align-items:center;
    }
</style>