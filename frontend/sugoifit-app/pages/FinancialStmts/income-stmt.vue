<template>
    <div class = "fin-page m-0 "> 
        <side-bar > </side-bar>

        <b-table :items = "stmt"> </b-table>
          <!-- <h6>{{stmt}}</h6> -->
          <!-- <h1>{{msg}}</h1> -->

    </div>
</template>


<script> 
// import axios from 'axios';
import SideBar from '../../components/SideBar.vue'
export default {
  components: { SideBar }, 
    name: 'IncomeStmt',
    data(){ 
        return { 
            msg: 'Checking', 
            stmt: [],
            stmtData:  [
                    { name: 32, '$': 'Cyndi', '$': 400.00 },
                    { age: 27, first_name: 'Havij' },
                    { age: 42, first_name: 'Robert' }
                    ]

            
        }
    }, 
    created: function() {
      let self = this;
      let path = 'printstmtdata';
             self.$axios.$get(`/api/printstmtdata`).then( jsonResponse =>{
              self.stmt = jsonResponse.response[0];
              console.log(jsonResponse);
            })
    },
    watch: {
      stmt: function(){

      }

    },
    methods: {
      
        ViewStmt: function (){
              let self = this;
              fetch("http://localhost:8080/api/printstmtdata",{
                  method: "GET", 
                  headers:{
                    "Accept": "application/json"
                  }, 
                  credentials: "same-origin",
              })
              .then(function (response){
                  return response.json();
              })
                .then(function(jsonResponse){
                  console.log(jsonResponse);
                  self.stmt = jsonResponse;
                })
                .catch( function(error){
                 // console.log(error);
              });
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