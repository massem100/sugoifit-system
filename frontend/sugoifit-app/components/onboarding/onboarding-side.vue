<template>
    <div class=" side-nav-on"> 
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
        display:grid;
        grid-template-rows: 1fr 1fr 1fr;
        margin: 20px;
        width: 24rem; 
        height: 100vh;
        padding:25px;
        text-transform: uppercase;
        border-right: 1px solid rgba(112,112, 0.05);
    }
</style>