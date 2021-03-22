<template>
    <div class = "fin-page m-0"> 
        <side-bar > </side-bar>

        <b-table :items = "stmtData"> </b-table>

    </div>
</template>


<script> 
import SideBar from '../../components/SideBar.vue'
export default {
  components: { SideBar }, 
    name: 'IncomeStmt',
    data(){ 
        return { 
            stmtData:  [
                    { name: 32, '$': 'Cyndi', '$': 400.00 },
                    { age: 27, first_name: 'Havij' },
                    { age: 42, first_name: 'Robert' }
                    ]

            
        }
    } 
}
</script>

<style scoped>
    .fin-page{
        display: flex;
        flex-direction: row; 
        font: 400 1rem "Roboto";
    }
</style>