<template>
    <div class= "container"> 
        <h1> ABC Analysis </h1>
        <hr>
        <table class= "content-table">
          <thead>
            <tr>
              <th scope="col"> Product </th>
              <th scope="col"> Consumption Value </th>
              <th scope="col"> Status </th>
              <th scope="col"> Date Updated </th>
              <th scope="col"> Grade </th>

            </tr>
          </thead>

            <tbody>
                <tr v-for="product in products" :key="product.prodID">
                    
                    <td> {{product.prodID}} </td>
                    <td> {{product.con_val}} </td>
                    <td> {{product.stock}} </td>
                    <td> {{product.dateAdded}} </td>
                    <td> {{product.grade}} </td>
                    
                </tr>
            </tbody>
        </table>
    </div>
</template>

 <script>
 import BackButton from '../components/argon-core/BackButton.vue';
 export default {
   components: { BackButton },
        name: "eversley",
        layout: 'DashboardLayout',
        methods: {
            test: () => {
                console.log('working');
            }
  },
  data() {
    return {
      products: [],
    };
  },
  methods: {
    getProducts() {
      const path = 'http://localhost:8080/api/classify';
      this.$axios.get(path)
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

    .content-table{
      border-collapse: collapse;
      margin: 25px 0;
      font-size: 0.9em;
      min-width: 400px;
      border-radius: 5px 5px 0 0;
      overflow: hidden;
      box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
    }

    .content-table thead tr{
      /* #009879 */
      background-color: #90D8E1; 
      color: #ffffff;
      text-align: left;
      font-weight: bold;
    }

    .content-table th{
      padding: 12px 15px;
    }
    .content-table td {
      padding: 12px 15px;
    }

    .content-table tbody tr{
      border-bottom: 1px solid #dddddd;
    }

    .content-table tbody tr:nth-of-type(even){
      background-color: #f3f3f3;
    }

    .content-table tbody tr:last-of-type{
      border-bottom: 2px solid #90D8E1;
    }

 </style>