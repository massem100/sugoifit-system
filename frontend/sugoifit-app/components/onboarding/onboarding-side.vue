<template>
    <div class="bg-primary side-nav-on"> 
        <!-- The inner divs will be triggered by a v-if to toggle active class/display -->
        <div> 

        </div>
        <div>
            <!-- I want to make the sidebar dynamic so when its time to change
             the company type instead of the list its illustration or words -->
            <h2> SugoiFIt App</h2>

            <ul> 
                <li>Company Type </li>
                <li>State </li>
                <li>Business Details </li>
                <li> Team </li>
                <li> Personal Details</li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    name: 'onboardingSide'
}
</script>

<style scoped>
 .side-nav-on{
     margin: 0; 
     width: 24rem; 
     height: 100vh;
 }
</style>