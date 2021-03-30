<template>
<div class = "h-100"> 
   
    <b-sidebar id="sidebar-1"  title = "Sugoifit Dashboard" shadow>

      <b-nav class ="side-navbar">
          <div class ="d-flex flex-row justify-content-start ">
          
            <!-- <h4 class = "nav_logo"> SugoiFit <span>Dashboard</span></h4> -->
          </div>
          <div class="d-flex flex-row">
          <div class="profile mt-3 mb-4 ">
                <h6 id = "profile_name"> Jane S.</h6>
                <h6  id= "profile_ID"> ID 1234567</h6>
                <h6 id ="role"> Role: Business Owner</h6>     
          </div>
          <img class ="" id = "profile-icon" src="~/assets/uploads/Profile_icon.png" alt="">
         
          </div>
<<<<<<< HEAD
          <div class="d-flex flex-column">
          <b-nav-item class = "bg-secondary" active>
                    <NuxtLink to="/" ><img class= "home-icon" src = ""> </NuxtLink>Dashboard
          </b-nav-item>
=======
          <!-- <span class="heading">Main</span> -->
            <ul class="list-unstyled">
                <li class="active"><NuxtLink to="/" ><img class= "home-icon" src = "">Dashboard </NuxtLink></li>
                <li class ="d-flex flex-row align-items-center"><NuxtLink to="manageproducts">Manage Products </NuxtLink></li>
                <li class ="d-flex flex-row align-items-center"><NuxtLink to="">Manage Sales </NuxtLink><i class="fas fa-angle-down fa-lg ml-auto mr-4"></i></li>
                <li class ="d-flex flex-row align-items-center"><NuxtLink to="FinancialStmts/income-stmt">Manage Financial Statements </NuxtLink><i class="fas fa-angle-down fa-lg ml-auto mr-4"></i></li>
                <li class ="d-flex flex-row align-items-center"><NuxtLink to="">View Reports </NuxtLink><i class="fas fa-angle-down fa-lg ml-auto mr-4"></i></li>
                <li class ="d-flex flex-row align-items-center"><NuxtLink to="">Manage Roles </NuxtLink><i class="fas fa-angle-down fa-lg ml-auto mr-4"></i></li>
            
            </ul>
>>>>>>> origin/main

          <b-nav-item class ="d-flex flex-row align-items-center">            
            <NuxtLink :to="{name: 'ManageProducts'}"> </NuxtLink> Manage Products
          </b-nav-item>
                      <!-- <li class ="d-flex flex-row align-items-center"><NuxtLink :to="">Manage Sales </NuxtLink><i class="fas fa-angle-down fa-lg ml-auto mr-4"></i></li> -->
          <b-nav-item class ="d-flex flex-row align-items-center">
            <NuxtLink :to="{name: 'FinancialStmts-income-stmt'}"> </NuxtLink> Manage Financial Statements
          </b-nav-item>

          <b-nav-item class ="d-flex flex-row align-items-center">
            <NuxtLink to=""></NuxtLink> View Reports 
          </b-nav-item> 
          <b-nav-item class ="d-flex flex-row align-items-center">
            <NuxtLink to=""> </NuxtLink> Manage Roles
          </b-nav-item>
          </div>
            
        </b-nav>
    </b-sidebar>
    </div>
</template>

<script>
export default {
    name: 'SideBar',
    data() {
        return {
          side_vis: true, 
            
        }
    }
}
</script>


<style scoped>


</style>