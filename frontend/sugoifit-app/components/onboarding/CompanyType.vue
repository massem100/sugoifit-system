<template>
    <div class="">
        <h2 class="font-bold m-4">Choose the type of business</h2>
        <p class="m-4">Choose the option that best describes your business.</p>
        <div class = "d-flex flex-row">
            <div class="d-flex flex-column">
                
                <div class = "company-options">
                    <div class="d-flex flex-column">
                        <img class = "icon-placeholder"  src="~/assets/uploads/Profile_icon.png" alt="">
                    </div>
                    <div class="d-flex flex-column">
                        <h5>Sole Proprietor</h5>
                        <h6> You are the sole owner of the business.</h6>
                    </div>
                    <!-- <font-awesome-icon :icon= "[fas, fa-user-tie]" /> -->
                    
                </div>
                <div class = "company-options">
                    <div class="d-flex flex-column">
                        <img class = "icon-placeholder"  src="~/assets/uploads/Profile_icon.png" alt="">
                    </div>
                    <div class="d-flex flex-column">
                        <h5>Partnership</h5>
                        <h6> The business is owned by more than one person</h6>
                    </div>
                </div>
            </div>
            <div class="d-flex flex-column">
                <div class = "company-options">
                    <div class="d-flex flex-column">
                        <img class = "icon-placeholder"  src="~/assets/uploads/Profile_icon.png" alt="">
                    </div>
                    <div class="d-flex flex-column">
                        <h5>Private Company</h5>
                        <h6> Privately incorporated, owned by individuals</h6>
                    </div>
                </div>
                <div class = "company-options">
                    <div class="d-flex flex-column">
                        <img class = "icon-placeholder"  src="~/assets/uploads/Profile_icon.png" alt="">
                    </div>
                    <div class="d-flex flex-column">
                        <h5>Public Company</h5>
                        <h6>The business is owned by stakeholders</h6>
                    </div>
                </div>
                
            </div>
        </div>  
    </div>
</template>

<script>
export default {
    
}
</script>


<style scoped>
    .company-options{
        display: flex;
        flex-direction: row;
        margin: 16px;
        background-color: white;
        border: 2px solid #f3f2f2;
        width: 20rem;
        height: 6rem; 
        border-radius: 20px;
        align-items: center;
        justify-content: center ;
        font: 0.5rem 'Poppins';
    }

    .company-options div{
        margin: 10px;
    }

    .company-options h6{
        font-size: 12px;
    }
    .icon-placeholder{
        width: 3rem; 
        height: 3rem;
    }
</style>