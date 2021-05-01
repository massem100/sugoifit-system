<template>
    <div class= "container"> 
        <h1> Hello, Testing </h1>
        <hr>
        <table class= "product-list">
            <th scope="col"> Product ID </th>
            <th scope="col"> Consumption Value </th>
            <th scope="col"> Grade </th>

            <tbody>
                <tr v-for="(product,prodID) in products" :key="prodID">
                    
                    <td> {{product.prodID}} </td>
                    <td> {{product.con_val}} </td>
                    <td> {{product.grade}} </td>
        
                </tr>


            </tbody>

        </table>
    </div>
</template>

 <script>
 import axios from 'axios';
 export default {
  data() {
    return {
      products: [],
    };
  },
  methods: {
    getProducts() {
      const path = 'http://localhost:8080/api/classify';
      axios.get(path)
        .then((res) => {
          this.products = res.data.products;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getProducts();
  },
 };
 </script>

 <<style scoped>
    table,{
        border-collapse: separate;
        border-spacing: 0 15px;
    }
    th, td {
        width: 150px;
        text-align: center;
        border: 1px solid black;
        padding: 5px;
    }
 </style>