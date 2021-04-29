<template>
           <div class="products-page m-2 ">
            <b-tabs content-class="mt-3" fill>
                <b-tab title="Add New Product" active>
                    <div class="sys-head w-100  ">
                            <div class="mr-auto head-title">
                                <h5> Manage Products</h5>
                                <p> Mange your products here </p>
                            </div>

                    </div>

                    <div class="products-main">


                        <div class="formData">
                            <div class="prod-item">
                                <b-label for="prodName"> Product Name </b-label>
                                <b-form-input type="text" name="ProductName" class="prodName"></b-form-input>
                            </div>
                            <div class="prod-item">
                                <b-label for="qtyinstock"> Quantity In Stock </b-label>
                                <b-form-input type="number" name="QtyInStock" class="qtyinstock"></b-form-input>
                            </div>
                            <div class="prod-item">
                                <b-label for="unitPrice"> Unit Price </b-label>
                                <b-form-input type="number" name="UnitPrice" class="unitPrice"></b-form-input>
                            </div>
                            <div class="prod-item">
                                <b-label for="threshold"> Threshold </b-label>
                                <b-form-input type="number" name="threshold" class="threshold" min="0" step="1"></b-form-input>
                            </div>
                            <div class="prod-item">
                                <b-label for="tax"> Tax </b-label>
                                <b-form-input type="number" name="tax" class="tax" min="0" step="0.01"></b-form-input>
                            </div>
                            <div class="prod-item">
                                <textarea rows= "3" cols="40" name = "description">
                                    Enter descripton here...
                                </textarea>
                            </div>


                        </div>
                        <div class="crudBtn">
                                <button class="buttons" type="button">Update</button>
                                <button class="buttons" type="button">Delete</button>
                                <button class="buttons" type="button">Cancel</button>
                        </div>

                    </div>
                </b-tab>
                <b-tab title="Second"><p>I'm the second tab</p></b-tab>
                <b-tab title="Very, very long title">
                    <p>I'm the tab with the very, very long title</p>
                    <div class = "bg-primary"> Click </div>
                </b-tab>

            </b-tabs>

        </div>
</template>

<script>
export default {
    name: 'ManageProducts',
    layout: 'DashboardLayout',
    data(){
        return{

        }
    }

}
</script>


<style scoped>

</style>
