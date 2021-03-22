<template>
    <div id="mainArea"> 
        <side-bar/>
        
        <div class="d-flex flex-row align-items-center settings_bar ml-auto ">
            <h6 class="d-flex ">Jane S.</h6>
            <img class="m-2" id="top-user-icon" src="~assets/uploads/Profile_icon.svg" alt="">
            <img class="m-2" src="~assets/uploads/settings.svg" alt="">
        </div>
        <div class ="time_box ml-auto"> 
            <p>7:00 PM</p>
            <p>EST</p>
            <p>12:00 AM</p>
            <p>LONDON</p>
        </div> 
        <div> 
            <div id="title">
                <h5> 
                Manage Products
                </h5>
                <p> Mange your products here </p>
            </div>

            <div id="formData"> 
                <div>
                    <label for="searchBox">Search</label>
                    <input type="text" name="SearchBox" id="searchBox">
                    <button class="buttons" type="button">Search</button>
                
                </div>

                <div>
                    <label for="prodName"> Product Name </label>
                    <input type="text" name="ProductName" id="prodName">
                </div>
                <div>
                    <label for="qtyinstock"> Quantity In Stock </label>
                    <input type="number" name="QtyInStock" id="qtyinstock">
                </div>
                <div>
                    <label for="unitPrice"> Unit Price </label>
                    <input type="number" name="UnitPrice" id="unitPrice">
                </div>
                <div>
                    <label for="threshold"> Threshold </label>
                    <input type="number" name="threshold" id="threshold" min="0" step="1">
                </div>
                <div>
                    <label for="tax"> Tax </label>
                    <input type="number" name="tax" id="tax" min="0" step="0.01">
                </div>
                <div> 
                    <textarea rows= "3" cols="40" name = "description">
                        Enter descripton here...
                    </textarea>
                </div>
                
            
            </div>
            <div id="crudBtn"> 
                    <button class="buttons" type="button">Update</button>
                    <button class="buttons" type="button">Delete</button>
                    <button class="buttons" type="button">Cancel</button>
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
    #mainArea{
        display:flex;
    
    }

    input[type=text],input[type=number]{
        align-content: center;
        width: 100px;
        height: 40px;
        left: 392px;
        top: 171px;
        border: none;
        background: #DFFBFF;
        border-radius: 15px;
        
        
    }

    #title{
        grid-area: title;
        padding-left: 50%;
        padding-top: 25%;
        padding-bottom: 15%;
    }

    #crudBtn{
        grid-area: crudBtn;
        padding-left:50%;
        display:block;
    }

    #formData{
        grid-area: formData;
        align-items: center;
        grid-template-columns: 150px 250px 250px 150px;
        grid-template-rows: auto;
        grid-template-areas:
        " . title title ."
        " . formData formData ."
        " . formData formData crudBtn";
        padding-left: 50%;
    }
   
    #prodName, #searchBox{
        align-content: center;
        width: 300px;
        height: 40px;
        left: 392px;
        top: 171px;
        border: none;
        background: #DFFBFF;
        border-radius: 15px;
    }

    .buttons{
        background-color: #4DC4D4;
        color: white;
        border-radius: 80px;
        justify-content: center;
        align-items: center;
        text-align: center;
        width: 7rem;
        height: 2rem;
    }

</style>