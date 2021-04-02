<template>

        <div class="products-page">
            <div class="sys-head w-100  ">
                 <div class="mr-auto head-title">
                    <h5> Manage Products</h5>
                    <p> Mange your products here </p>
                </div>       
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
   
    .products-page{
        margin-left: 2rem;
        width:100vw;
        grid-template-areas: "syshead syshead"
                             "product-main";
    }

    
    
</style>