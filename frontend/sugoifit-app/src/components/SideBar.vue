<template>
    <div>
      <nav class ="side-navbar">
          <!-- <img :src="navSVG" alt=""> -->
          <img src="src/assets/align-left.png" alt="">
          <h4 class = "nav_logo"> SugoiFit <span>Dashboard</span></h4>
          
          <div class="profile">
              <h6> Jane S.</h6>
              <h6> ID 1234567</h6>
              <h6> Role: <span>Business Owner</span></h6>

          </div>

          <span class="heading">Main</span>
            <ul class="list-unstyled">
                <li class="active"><a href=""><img class= "home-icon" src = ""><i class="icon-home"></i>Dashboard </a></li>
                <li><a href=""><img class="home-icon" src=""><i class="icon-grid"></i>My Profile </a></li>
            
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