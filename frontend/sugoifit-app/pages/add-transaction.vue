<template>
  <div>
    <!-- Quick Actions -->
    <div class="mx-3">
      <h3 class="m-2">Transactions </h3>
      <p class = "m-2 "> Transactions are used to automatically generate your financials. Keep track of your daily transactions.</p>
      <p class = "m-2">  </p>
      <transaction-top/>
    </div>
  </div>
</template>

<script>
    export default {
        name: "add-transaction",
        layout: 'dashboard',
        methods: {
            addTransaction: () => {
                console.log('working');
            }
        },
        data() {
            return {
                assetName: "",
                assetType: "",
                depreciationMethod: "",
                el: ""
            };
        },
    };
</script>


<style>
  .box {
    width: 130px;
    height: 120px;
    text-align: center;
    font-size: 30px;
  }


</style>
