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
                <li class="active"><a href=""><img class= "home-icon" src = "">Dashboard </a></li>
                <li class ="d-flex flex-row align-items-center"><a href="">Manage Products </a></li>
                <li class ="d-flex flex-row align-items-center"><a href="">Manage S                ales </a><i class="fas fa-angle-down fa-lg ml-auto mr-4"></i></li>
                <li class ="d-flex flex-row align-items-center"><a href="">Manage Financial Statements </a><i class="fas fa-angle-down fa-lg ml-auto mr-4"></i></li>
                <li class ="d-flex flex-row align-items-center"><a href="">View Reports </a><i class="fas fa-angle-down fa-lg ml-auto mr-4"></i></li>
                <li class ="d-flex flex-row align-items-center"><a href="">Manage Roles </a><i class="fas fa-angle-down fa-lg ml-auto mr-4"></i></li>
            
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