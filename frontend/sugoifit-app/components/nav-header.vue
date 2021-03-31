<template>

        <b-navbar class = "" toggleable="lg" type="light" >       
                <b-row class="">
                      <b-row class="mr-auto">
                         <b-img src = "~assets/uploads/reg_nav.svg" class = "ml-5 nav-icon" v-b-toggle.sidebar-1  ></b-img>
                         <font-awesome-icon :icon="['fas','fa-align-justify']" /> 
                         <b-link :to = "{name: 'index'}" class=""><b-navbar-brand class = "text-white"> SugoiFit Financials</b-navbar-brand></b-link>
                      </b-row>
                    
                        <b-row class="align-items-center justify-content-between ml-auto bg-info">
                            <h6 class="d-flex ">Jane S.</h6>
                            <img class="m-1" id="top-user-icon" src="~assets/uploads/Profile_icon.svg" alt="">
                            <img class="m-1" src="~assets/uploads/settings.svg" alt="">
                        </b-row>
                </b-row>
        </b-navbar>

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