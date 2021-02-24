<template>
    <div class="page-content d-flex align-items-stretch">
        <!-- Add a image of the user and their name to the top  -->
        <!-- Side Navbar -->
        <nav class="side-navbar ">           
            <div class="sidebar-header d-flex align-items-center">
                <div class="title">
                    <div class = "d-flex flex-row">
                        <img class = "mr-1" id="sidebar-image" src="">
                        <div>
                            <h1 class="h4">First name and last name</h1>
                            <p> username</p>
                            
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Sidebar Navigation Menus-->
            <span class="heading">Main</span>
            <ul class="list-unstyled">
                <li class="active"><a href="" >
                    <img class= "home-icon" src = ""><i class="icon-home"> </i>Dashboard </a></li>
                <!-- <li><a href="{{url_for('userprofile')}}"><img class="home-icon" src="/static/uploads/user.png"><i class="icon-grid"></i>My Profile </a></li>
                <li><a href="#friendsdropdown" aria-expanded="false" data-toggle="collapse"> <img class="home-icon" src="/static/uploads/friend.png"><i class="fa fa-bar-chart"></i>Find Friends</a>
                        <ul id="friendsdropdown" class="collapse list-unstyled ">
                            <li><a href="{{url_for('friends')}}"> My Friends</a></li>
                            <li><a href="{{url_for('searchfriends')}}">Search Friends</a></li>
                        </ul>
                </li>
                 -->
                </ul>
        </nav>
        </div>
</template>

<script>
export default {
    name: 'SideBar',
}
</script>


<style scoped>

</style>