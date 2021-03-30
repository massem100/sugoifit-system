<template>
 <header class="header ">
        <nav class="navbar">
                       
            <div class="container-fluid">
                <div class="navbar-holder d-flex align-items-center justify-content-between">
                    <!-- Navbar Header-->
                    <div class="navbar-header">
                         <img src = "~assets/uploads/reg_nav.svg" class = "ml-5 nav-icon" @click = "SideToggle" >
                          <font-awesome-icon icon="['fas','fa-bars']" v-b-toggle.sidebar-1></font-awesome-icon>
                         <!-- <a id="toggle-btn" href="#" class="menu-btn active"><span></span><span></span><span></span></a> -->
                        <!-- Navbar Brand -->
                        <a href="" class="navbar-brand d-none d-sm-inline-block">
                        <!-- <div class="test brand-text d-none d-lg-inline-block"><span>MyBook </span><strong>Social</strong></div>    -->
                        <h5 class = "text-white"> SugoiFit Financials</h5>
                        </a>
                        <!-- Toggle Button-->
                        <!-- <a id="toggle-btn" href="#" class="menu-btn active"><span></span><span></span><span></span></a>     -->
                        <!-- <img class = "nav_icon" src="~/assets/uploads/align-left.png" alt=""> -->
                    </div>
                    
                   
                        <div class="d-flex flex-row align-items-center settings_bar ml-auto  bg-danger">
                        <h6 class="d-flex ">Jane S.</h6>
                        <img class="m-1" id="top-user-icon" src="~assets/uploads/Profile_icon.svg" alt="">
                        <img class="m-1" src="~assets/uploads/settings.svg" alt="">
                        </div>
                </div>
            </div>
        </nav>
    </header>
</template>
<script>
export default {
    name: "NavHeader",
    data(){ 
        return{

        }
    }, 
    methods:{
        SideToggle: function(){
            let stoggle  = document.getElementsByClassName('nav-icon')[0];
            stoggle.setAttribute('v-b-toggle.sidebar-1');
          
          
    }
    

    }

    
}
</script>


<style scoped>
    header{
        /* background-color: blue; */
    }
    .navbar{
        background-color: #7CC3CD;
    }

    .nav-icon{
        width: 1.5rem; 
        height: 1.5rem;
        /* pointer-events: none; */
    
    }
</style>