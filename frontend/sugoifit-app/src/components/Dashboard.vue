<template>
    <div class= "d-flex flex-row ">
        <!-- Side Bar Component -->
        <side-bar>Check</side-bar>
       

        <!-- Overview -->
        <div class = "d-flex flex-column  w-100">
            <div class="d-flex flex-row ml-auto">
                <h6>Jane S.</h6>
                <img src="" alt="">
            </div>
           <div class = "d-flex flex-row">
            <div class = ""> 
                <!-- Welcome + Msg -->
                <h5 class =""> Welcome Back, <span> Jane</span> </h5>
                <p class="">Lorem ipsum dolor sit amet consectetur adi</p>
            </div>
            <div class ="d-flex flex-row ml-auto p-3 m-4"> 
                <div class ="d-flex flex-column ">
                    <p class="time pr-2">7:00 PM</p>
                    <p class="time_zone">EST</p>
                </div>
                <div class ="d-flex flex-column p-3">
                    <p class="">12:00 AM</p>
                    <p class="">LONDON</p>
                </div>            
            </div>
        </div>
            

        

            <!-- Quick Actions -->
            <div class="d-flex flex-row p-2 text-center">
                <div class = "d-flex flex-column quick_actions"><img src="" alt=""><i class="fas fa-plus"></i><span>Add Transaction</span></div>
                <div class = "d-flex flex-column quick_actions"><img src="" alt=""><i class="fas fa-plus"></i><span> Place Order</span></div>
                <div class = "d-flex flex-column quick_actions"><img src="" alt=""><i class="fas fa-plus"></i><span> Create Invoice</span></div>

            </div>
        </div>
    </div>
</template>

<script>
import SideBar from './SideBar.vue'
import Login from './Login'

export default {
    components: { SideBar, Login},
    name: 'Dashboard',

}
</script>