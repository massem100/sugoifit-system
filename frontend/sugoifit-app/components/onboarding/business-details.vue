<template>
  <b-container>
    <div class="about-business-form-div">
      <b-form action="" class="about-business-form">
        <div class="about-business-form-item">

          <label for="comp-name" class="font-weight-bold">Company Name</label>
          <div class="name-container d-flex flex-row">

            <b-form-input
              placeholder="E.g. Monique's Boutique"
              class="mr-2 w-80"
              id="comp_name"
              name="comp_name"
            >
            </b-form-input>
            <b-form-input
              placeholder="eg. Ltd."
              class="w-25"
              id="name_end"
              name="name_end"
            >
            </b-form-input>
          </div>
        </div>

        <div class="shares-div ">
          <div class="about-business-form-item">
            <label for="" class="font-weight-bold"> Product or Service </label>
            <b-form-select
              id=corp_type
              name="corp_type"
              :options="busNature"
            >
            </b-form-select>
          </div>
          <div class="about-business-form-item">
            <label for="" class="font-weight-bold"> Telephone </label>
            <b-form-input
              placeholder="(555)-XXX-XXXX"
              id="bus_tel"
              name="bus_tel"

            >
            </b-form-input>
          </div>

        </div>
        <div class="about-business-form-item">
          <label for="" class="font-weight-bold"> Business Address</label>
          <b-form-input
            placeholder="1234 Plaza Square, Place, Jamaica, JMDCN10"
            class="bus-address"
            id="bus_address"
            name="bus_address"
          >
          </b-form-input>
        </div>
        <div class="about-business-form-item">
          <label for="industry" class="font-weight-bold"> Business Description</label>
          <b-form-input
            placeholder="Write 2 or 3 sentences"
            class="bus-desc"
            id="industry"
            name="industry"
          >
          </b-form-input>
        </div>
      </b-form>
    </div>
  </b-container>
</template>

<script>
    export default {
        name: "business-details",
        data () {
        return {
            corp_types: [
                {value : null, text: 'Please select your type of incorporation.'},
                {value : 'a', text: 'Private Company '},
                {value : 'b', text: 'Unlimited Liability Company'},
                {value : 'c', text: 'Limited Liability Company'},

            ],
            busNature: [
                {value: null, text: 'Select Product-Based or Service-Based'},
                {value: 'a', text: 'Product-Based'},
                {value: 'b', text: 'Service-Based'},
            ]
        }
    },
    }
</script>

<style scoped>

</style>
