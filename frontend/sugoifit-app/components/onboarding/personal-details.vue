<template>
  <b-container>
    <div class="about-business-form-div">
      <b-form action="" class="about-business-form">
        <div class="about-business-form-item">

          <label for="comp-name" class="font-weight-bold">Your Name</label>
          <div class="name-container d-flex flex-row">

            <b-form-input
              class="mr-2 w-80"
              id="comp_name"
              name="comp_name"
            >
            </b-form-input>
          </div>
        </div>

        <div class="shares-div ">
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
          <label for="" class="font-weight-bold"> Home Address</label>
          <b-form-input
            placeholder="1234 Plaza Square, Place, Jamaica, JMDCN10"
            class="bus-address"
            id="bus_address"
            name="bus_address"
          >
          </b-form-input>
        </div>
        <div class="about-business-form-item">
          <label for="industry" class="font-weight-bold"> Yor Bio</label>
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
        name: "personal-details",
        data () {
        return {
        }
    },
    }
</script>

<style scoped>

</style>
