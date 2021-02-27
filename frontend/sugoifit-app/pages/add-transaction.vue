<template>
<div class ="d-flex flex-row">
    <side-bar></side-bar>
 <!-- Quick Actions -->
 <div class ="ml-5">
     <div class="d-flex" style="justify-start">
          <h3 class="ml-3 mt-2">Add Transaction</h3>
        </div>
      <div class=" d-flex flex-row p-2 text-center">
        <button class="btnStyle" @click="addTransaction">
          <div class="d-flex flex-column quick_actions box">
            <img src="" alt="" /><i class="fas fa-plus"></i
            ><span>Add Asset</span>
          </div>
        </button>
        <button class="btnStyle">
          <div class="d-flex flex-column quick_actions box">
            <img src="" alt="" /><i class="fas fa-plus"></i
            ><span> Add Liabillity</span>
          </div>
        </button>
        <button class="btnStyle">
          <div class="d-flex flex-column quick_actions box">
            <img src="" alt="" /><i class="fas fa-plus"></i
            ><span> Add Expense</span>
          </div>
        </button>
        <button class="btnStyle">
          <div class="d-flex flex-column quick_actions box">
            <img src="" alt="" /><i class="fas fa-plus"></i
            ><span>Add Purchases</span>
          </div>
        </button>
        <button class="btnStyle">
          <div class="d-flex flex-column quick_actions box">
            <img src="" alt="" /><i class="fas fa-plus"></i
            ><span> Add Sales</span>
          </div>
        </button>
        <button class="btnStyle">
          <div class="d-flex flex-column quick_actions box">
            <img src="" alt="" /><i class="fas fa-plus"></i
            ><span> Add Equity</span>
          </div>
        </button>
      </div>
  <div class="d-flex flex-column mt-1" style="align-items: flex-start">
    <div class="row">
      <div class="col d-flex flex-column ml-3" style="align-items: flex-start">
        <p class="text_start text-secondary">Asset Name</p>
        <input
          type="text"
          id="fname"
          name="fname"
          class="form-control rounded"
          v-model="assetName"
        /><br /><br />
      </div>
    </div>
    <div class="row">
      <div class="col d-flex flex-column ml-3" style="align-items: flex-start">
        <p class="text-secondary">Asset Type</p>
        <input
          type="text"
          id="at"
          name="at"
          class="form-control rounded"
          v-model="assetType"
        /><br /><br />
      </div>
    </div>
    <div class="row">
      <div class="col d-flex flex-column ml-3" style="align-items: flex-start">
        <p class="text-secondary">Depperciation Method</p>
        <input
          type="text"
          id="dm"
          name="dm"
          class="form-control rounded"
          v-model="depreciationMethod"
        /><br /><br />
      </div>
    </div>
      <div class="row">
      <div class="col d-flex flex-column ml-3" style="align-items: flex-start">
        <p class="text-secondary">Expected Lifespan</p>
        <input
          type="text"
          id="es"
          name="es"
          class="form-control rounded"
          v-model="el"
        /><br /><br />
      </div>
    </div>
  </div>
 </div>

  </div>
</template>

<script>
import SideBar from '/components/SideBar.vue';
//import SideBar from './SideBar.vue'
export default {
  components: { SideBar },
  // components: { SideBar },
  name: "add-transaction",
  methods:{
    addTransaction: ()=>{
      console.log('working');
    }
  },
  data() {
    return {
      assetName: "",
      assetType: "",
      depreciationMethod: "",
      el:""
    };
  },
};
</script>



<style >
.box {
  width: 130px;
  height: 120px;
  text-align: center;
  font-size: 30px;
}
.btnStyle {
  padding: 0;
  border: none;
  background: none;
  cursor: pointer;
}
</style>