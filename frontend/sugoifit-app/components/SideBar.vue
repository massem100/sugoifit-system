<template>
    <div>
      <nav class ="side-navbar">
          <!-- <img :src="navSVG" alt=""> -->
          <div class ="d-flex flex-row justify-content-start ml-4">
            <img class = "nav_icon" src="~/assets/uploads/align-left.png" alt="">
            <h4 class = "nav_logo"> SugoiFit <span>Dashboard</span></h4>
          </div>
          <div class="d-flex flex-row">
          <div class="profile mt-3 mb-4 ">
                <h6 id = "profile_name"> Jane S.</h6>
                <h6  id= "profile_ID"> ID 1234567</h6>
                <h6 id ="role"> Role: Business Owner</h6>     
          </div>
          <img class ="" id = "profile-icon" src="~/assets/uploads/Profile_icon.png" alt="">
         
          </div>
          <!-- <span class="heading">Main</span> -->
            <ul class="list-unstyled">
                <li class="active"><NuxtLink to="/" ><img class= "home-icon" src = "">Dashboard </NuxtLink></li>
                <li class ="d-flex flex-row align-items-center"><NuxtLink to="manageproducts">Manage Products </NuxtLink></li>
                <li class ="d-flex flex-row align-items-center"><NuxtLink to="">Manage Sales </NuxtLink><i class="fas fa-angle-down fa-lg ml-auto mr-4"></i></li>
                <li class ="d-flex flex-row align-items-center"><NuxtLink to="financial_stmt">Manage Financial Statements </NuxtLink><i class="fas fa-angle-down fa-lg ml-auto mr-4"></i></li>
                <li class ="d-flex flex-row align-items-center"><NuxtLink to="">View Reports </NuxtLink><i class="fas fa-angle-down fa-lg ml-auto mr-4"></i></li>
                <li class ="d-flex flex-row align-items-center"><NuxtLink to="">Manage Roles </NuxtLink><i class="fas fa-angle-down fa-lg ml-auto mr-4"></i></li>
            
            </ul>

      </nav>
    </div>
</template>

<script>
export default {
    name: 'SideBar',
    data() {
        return {
            
        }
    }
}
</script>


<style scoped>
</style>