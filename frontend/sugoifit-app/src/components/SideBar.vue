<template>
    <div>
      <nav class ="side-navbar">
          <!-- <img :src="navSVG" alt=""> -->
          <div class ="d-flex flex-row justify-content-center">
            <img class = "nav_icon" src="static/uploads/align-left.png" alt="">
            <h4 class = "nav_logo"> SugoiFit <span>Dashboard</span></h4>
          </div>
          <div class="profile ">
                <h6 id = "profile_name"> Jane S.</h6>
                <h6  id= "profile_ID"> ID 1234567</h6>
                <img class ="" id = "profile-icon" :src="'/static/uploads/Profile_icon.png'" alt="">
                <h6 id ="role"> Role: Business Owner</h6>     
          </div>

          <span class="heading">Main</span>
            <ul class="list-unstyled">
                <li class="active"><a href=""><img class= "home-icon" src = ""><i class="icon-home"></i>Dashboard </a></li>
                <li><a href=""><img class="home-icon" src=""><i class="icon-grid"></i>Manage Products </a></li>
                <li><a href=""><img class="home-icon" src=""><i class="icon-grid"></i>Manage Sales </a></li>
                <li><a href=""><img class="home-icon" src=""><i class="icon-grid"></i>Manage Financial Statements </a></li>
                <li><a href=""><img class="home-icon" src=""><i class="icon-grid"></i> View Reports </a></li>
                <li><a href=""><img class="home-icon" src=""><i class="icon-grid"></i>Manage Roles </a></li>
            
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