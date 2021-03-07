<template>
  <div class="d-flex flex-row">
    <side-bar></side-bar>
    <!-- Quick Actions -->
    <div class="ml-5">
      <top-bar/>
      <h3 class="m-2">Add Transaction</h3>
      <transaction-top/>
    </div>
  </div>
</template>

<script>
    export default {
        name: "add-transaction",
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
