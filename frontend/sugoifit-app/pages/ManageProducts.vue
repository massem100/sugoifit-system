<template>
    <div class="mainArea m-0"> 
        <side-bar class="side-bar m-0 h-100"></side-bar>

        <div class="products-page ">
           
            <b-tabs content-class="mt-3" fill>
                <b-tab title="Add New Product" active>
                    <div class="sys-head w-100  ">
                            <div class="mr-auto head-title">
                                <h5> Manage Products</h5>
                                <p> Mange your products here </p>
                            </div>
                        
                    </div>
                    <!-- <div class ="product-card">
                            <h5> Product Overview</h5>ur
                            <p class="prod-p">Lorem ipsum dolor sit amet,  iste at facilis eos architecto 
                                alias perferendis veritatis dolor ut cupiditate repellat reiciendis maxime,
                                ipsam voluptatibus blanditiis quibusdam.  Lorem ipsum dolor, sititaque ab 
                                obcaecati modi saepe minus necessitatibus?</p>
                    </div> -->
                    <div class = "products-main">
                    

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
    </div>
</template>

<script>
export default {
    name: 'ManageProducts',
    layout: 'dashboard',
    data(){
        return{

        }
    }
    
}
</script>


<style scoped>
    .mainArea{
        display:flex;
        flex-direction: row;
        font: 400 1rem "Poppins";
        /* background-color: burlywood; */
        /* min-height:100vh; */
        
    
    }
    .products-page{
        margin-left: 20rem;
        /* margin:2rem; */
        /* display: flex;
        flex-direction: column; */
        /* background-color: rgb(172, 235, 172); */
        width:100vw;
        grid-template-areas: "syshead syshead"
                             "product-main";
    }

    
    .sys-head{
        display: flex;
        flex:row;
        /* background-color: rgb(117, 77, 155); */
        width:100%;
        grid-area: 'sys-head';
    }

    .products-main{
        margin: 2rem;
        width: 40rem;
        /* background-color: peachpuff; */
        grid-area: 'product-main';
    }

    .head-title{
        margin: 2rem;
    }
    .head-title h5{
        font: 600 1.8rem "Poppins";
        align-items: center;

    }

    .product-card{
        margin: 1rem 2rem;
        width: 60rem; 
        height: 15rem;
        padding: 2rem;
        display: flex;
        flex-direction: column;
        /* background: url('~assets/uploads/green-product-background.jpg'); */
        background-color: rgb(242, 251, 255);
        background-size: 60rem 15rem;
        border-radius: 20px;
    }
    .product-card h5 .prod-p{
        margin: 4rem;
    }

    .side-bar{
        position:fixed; 

    }

    .prod-item{
        margin: 1rem;
    }
</style>