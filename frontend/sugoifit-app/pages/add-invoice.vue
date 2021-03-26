<template>
  <div class="d-flex flex-row">
    <side-bar></side-bar>
    <!-- Quick Actions -->
    <div class="ml-5">
      <top-bar class="top-bar"/>
      <h3 class="m-2">Add Invoice</h3>
      <invoice-top/>
    </div>
    <!--
    <div class="invoice-layout">
        <form action="" name="invoice">
            <input type="image" placeholder="Logo">
            <label for="comp_name" name="comp_name" class="comp_name" > Monique's Botique</label>
            <label for="invoice_id" name="invoice_id" class="invoice_id"> Invoice ID: invoice0042 </label>
            <label for="comp_address" name="comp_address"> Shop #3. XYZ Plaza, Kingston 8, Kingston </label>

            <label for="bill_info" name="bill"> Bill to: </label>
            <input type="text" placeholder="customer_name">
            <input type="text" placeholder="customer_email">
            <input type="text" placeholder="telephone #">

            <label for="issue_date" > Date issued: March 14, 2021 </label>
            <input type="text" placeholder="issue_date">
            <label for="due_date" > Due Date: March 14, 2021 </label>
            <input type="text" placeholder="due_date">
            <label for="balance" > Balance Due: </label>
            <label for="balance" > $1,000.00 </label>

            <hr>

            <label for="item_desc" > Description </label>
            <label for="unit_price" > Unit Price </label>
            <label for="quantity" > Quantity </label>
            <label for="amount" > Amount </label>

            <input type="text" placeholder="item_desc">
            <input type="text" placeholder="unit_price">
            <input type="text" placeholder="quantity">
            <input type="text" placeholder="amount">

            <label for="sub_total" > SubTotal: </label>
            <label for="tax" > Tax: $10.00 </label>
            <label for="total" > Total:  </label>

            <label for="thanks" > Thank you for choosing Monique’s Botique.  </label>
            
            <button type="submit"> Save </button>
        </form>
    </div>
    -->

  </div>
</template>

<script>
    export default {
        name: "add-invoice",
        methods: {
            addInvoice: () => {
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
