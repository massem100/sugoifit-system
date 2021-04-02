<template>
  <div class="d-flex flex-row">
    <!-- Quick Actions -->
    <div class="ml-5">
      <h3 class="m-2">Add Transaction</h3>
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
