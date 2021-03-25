<template>
    <div class="d-flex flex-row ">
    <!-- Side Bar Component -->
        <side-bar class = "side-bar">Check</side-bar>

        <div class="dashboard-main">
        <!-- Overview -->
        <div class="d-flex flex-column w-100">
            <div class="d-flex flex-row align-items-center settings_bar ml-auto ">
              <img class="m-2" src="~assets/uploads/settings.svg" alt="" >
              <nuxt-link class="d-flex flex-column quick_actions" :to="{name:'your-profile'}">
                <img src="" alt=""><i class="fas fa-plus"></i><span>Your Profile</span>
              </nuxt-link>
              <nuxt-link class="d-flex flex-column quick_actions" :to="{name:'your-company'}">
                <img src="" alt=""><i class="fas fa-plus"></i><span>Your company</span>
              </nuxt-link>
              <nuxt-link class="d-flex flex-column quick_actions" :to="{name:'your-website'}">
                <img src="" alt=""><i class="fas fa-plus"></i><span>Your Website</span>
              </nuxt-link>
              <nuxt-link class="d-flex flex-column quick_actions" :to="{name:'user-management'}">
                <img src="" alt=""><i class="fas fa-plus"></i><span>User management</span>
              </nuxt-link>
            </div>

            <div class="d-flex flex-row">
                <div class="welcome-heading">
                    <h5 class=""> Welcome Back, <span> Jane</span></h5>
                    <p class="">Lorem ipsum dolor sit amet consectetur adi</p>
                </div> 
            </div>

        </div>
        
          <div class="quick_actions_div d-flex flex-row p-2 text-center">
              
              
            </div>

          </div>
        </div>


    </div>

</template>
<script>
export default {
    name: 'Settings',
}
</script>

<style scoped>

.side-bar{
    position: fixed;
}

.dashboard-main{
    margin-left: 20rem;
}
</style>