<template>
    <div class= "container"> 
        <h1> Manage Orders </h1>
        <hr>
        <table class= "content-table">
          <thead>
            <tr>
              <th scope="col"> Customer ID </th>
              <th scope="col"> Invoice ID </th>
              <th scope="col"> Order Num </th>
              <th scope="col"> Order Total </th>
              <th scope="col"> Date Ordered </th>
              <th scope="col"> Date Due </th>
              <th scope="col"> Status </th>
            </tr>
          </thead>

            <tbody>
                <tr v-for="result in results" :key="result.orderID">
              
                    <td> {{result.custID}} </td>
                    <td> {{result.invoiceID}} </td>
                    <td> {{result.orderID}} </td>
                    <td> {{result.orderTotal}} </td>
                    <td> {{result.date}} </td>
                    <td> {{result.dueDate}} </td>
                    <td> {{result.status}} </td>

                    <!-- <br>
                    <select name="status" id="action" onchange="this.form.submit()">
                      <option value="Pending">Pending</option>
                      <option value="Payment Received">Payment Received</option>
                      <option value="Processing">Processing</option>
                      <option value="On Hold">On Hold</option>
                      <option value="Shipped">Shipped</option>
                      <option value="Cancelled">Cancelled</option>
                      <option value="Failed">Failed</option>
                    </select>
                    <br>
                    <br> -->
                    
                </tr>
            </tbody>
        </table>
    </div>
</template>

 <script>
 import BackButton from '../components/argon-core/BackButton.vue';
 export default {
   components: { BackButton },
        name: "eversley2",
        layout: 'DashboardLayout',
        methods: {
            test: () => {
                console.log('working');
            }
  },
  data() {
    return {
      results: [],
    };
  },
  methods: {
    getResult() {
      const path = 'http://localhost:8080/api/manage-orders';
      this.$axios.get(path)
        .then((res) => {
          this.results = res.data.results;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getResult();
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

    #action{
      
    }

 </style>