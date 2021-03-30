<template>
    <div class="mainArea m-0"> 
        <side-bar class="side-bar m-0 h-100"></side-bar>

        <div class="products-page ">
            <div class="sys-head w-100  ">
                 <div class="mr-auto head-title">
                    <h5> Manage Products</h5>
                    <p> Mange your products here </p>
                </div>
                <div class="head-misc d-flex flex-column">
                    <div class="d-flex flex-row  bg-secondary">
                        <h6 class=" ">Jane S.</h6>
                        <img class="top-user-icon m-2" src="~assets/uploads/Profile_icon.svg" alt="">
                        <img class="m-2" src="~assets/uploads/settings.svg" alt="">
                    </div>
                    <div class ="time_box"> 
                        <p>7:00 PM</p>
                        <p>EST</p>
                        <p>12:00 AM</p>
                        <p>LONDON</p>
                    </div> 
                </div>
            </div>
           <div class ="product-card">
                <h5> Product Overview</h5>ur
                <p class="prod-p">Lorem ipsum dolor sit amet,  iste at facilis eos architecto 
                    alias perferendis veritatis dolor ut cupiditate repellat reiciendis maxime,
                     ipsam voluptatibus blanditiis quibusdam.  Lorem ipsum dolor, sititaque ab 
                     obcaecati modi saepe minus necessitatibus?</p>
            </div>
            <div class = "products-main">
               
            <div>
            <b-tabs content-class="mt-3">
                <b-tab title="All Products" active><p>I'm the first tab</p></b-tab>
                <b-tab title="Active"><p>I'm the second tab</p></b-tab>
                <b-tab title="Disabled" disabled><p>I'm a disabled tab!</p></b-tab>
            </b-tabs>
            </div>
         </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ManageProducts',
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
</style>