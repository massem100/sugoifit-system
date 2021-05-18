<template>
  <b-container>
    <b-row>
      <b-col cols="12" class="mb-3">
        <label class="font-weight-bold">Email Address</label>
        <input type="text" name="email" class="form-control" style="max-width: 350px">
      </b-col>
      <b-col cols="12" class="mb-3">
        <label class="font-weight-bold">Business Type</label>
        <b-form-checkbox-group
          v-model="business_type"
          name="business_type"
          stacked
          class="ml-3"
        >
          <b-form-checkbox value="Sole Trader">Sole Trader (A business owned and operated by one individual)
          </b-form-checkbox>
          <b-form-checkbox value="Partnership">Partnership (An unincorporated business owned by two or more persons.)
          </b-form-checkbox>
          <b-form-checkbox value="Company">Company (A business that is incorporated. Please select type of
            incorporation, private or public.)
          </b-form-checkbox>
        </b-form-checkbox-group>
      </b-col>
      <b-col cols="12">
        <div class="business-form-div">
          <div class="business-form-item">
            <label for="corp_type" class="font-weight-bold">Type of corporation</label>
            <b-form-select aria-placeholder="Select business type." id=corp_type :options="corp_types"></b-form-select>

          </div>

          <div class="shares-div ">
            <div class="business-form-item">
              <label for="" class="font-weight-bold"> Number of Shares </label>
              <b-form-input placeholder="Standard: 10000" id=""></b-form-input>
            </div>
            <div class="business-form-item">
              <label for="" class="font-weight-bold"> Per value </label>
              <b-form-input placeholder="Cost per share" id=""></b-form-input>
            </div>
          </div>
          <div class="business-form-item">
            <label for="industry" class="font-weight-bold"> Industry</label>
            <b-form-input placeholder="e.g Technology / Finance"
                          id="industry"></b-form-input>
          </div>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
    export default {
        name: "business-setup",
        data() {
            return {
                business_type: [],
                corp_types: [
                {value : null, text: 'Please select your type of incorporation.'},
                {value : 'a', text: 'Private Company '},
                {value : 'b', text: 'Unlimited Liability Company'},
                {value : 'c', text: 'Limited Liability Company'},

            ],
            }
        }
    }
</script>

<style scoped>

</style>
