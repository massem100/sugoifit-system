<template>
  <div>
      <validation-observer
        ref="observer"
        v-slot="{handleSubmit}"
      >
        <b-form @submit.stop.prevent="handleSubmit()" enctype="multipart/form-data">
          <b-row class="align-items-center">
            <b-col class="mb-2" md="2" sm="12">
              <div class="text-center">
                <b-img-lazy :src="avatar" alt="" width="100" height="100" style="border-radius: 50%"></b-img-lazy>
              </div>

            </b-col>
            <b-col class="mb-2 c-box" md="6" sm="12">
              <div class="d-flex justify-content-between">
                <label class="mb-0">Upload New Image</label>
                <div class="text-danger text-right cursor-pointer" @click="removeImage">Remove</div>
              </div>

              <b-form-file @change="uploadAvatar"
                           accept="image/*"
                           id="uploadImage"
                           ref="file-input"
              >
              </b-form-file>
            </b-col>
          </b-row>
          <b-row class="mt-4 mx-lg-4 align-items-center mh-lg">
            <b-col md="3">
              <label class="text-info font-weight-bold">User ID</label>
            </b-col>
            <b-col md="9" class="font-weight-bold">
              COMP001
            </b-col>
          </b-row>
          <b-row class=" mx-lg-4 align-items-center mh-lg">
            <b-col md="3">
              <label class="text-info font-weight-bold">User Role</label>
            </b-col>
            <b-col md="9" class="font-weight-bold">
              Buisness Owner
            </b-col>
          </b-row>
          <b-row class=" mx-lg-4 align-items-center mh-lg">
            <b-col md="3">
              <label class="text-info font-weight-bold">User Name</label>
            </b-col>
            <b-col md="9" class="c-box">
              <validation-provider
                v-slot="{ errors }"
                rules="required"
                name="user name"
              >
                <b-form-input v-model="form.user_name"
                              type="text"
                              required
                              :state="getValidationState(errors)">
                </b-form-input>
                <b-form-invalid-feedback>
                  {{ errors[0] }}
                </b-form-invalid-feedback>
              </validation-provider>
            </b-col>
          </b-row>
          <b-row class=" mx-lg-4 align-items-center mh-lg">
            <b-col md="3">
              <label class="text-info font-weight-bold">User Email</label>
            </b-col>
            <b-col md="9" class="c-box">
              <validation-provider
                v-slot="{ errors }"
                rules="required|email"
                name="user email"
              >
                <b-form-input v-model="form.user_email"
                              type="email"
                              required
                              :state="getValidationState(errors)">
                </b-form-input>
                <b-form-invalid-feedback>
                  {{ errors[0] }}
                </b-form-invalid-feedback>
              </validation-provider>
            </b-col>
          </b-row>
          <b-row class=" mx-lg-4 align-items-center mh-lg">
            <b-col md="3">
              <label class="text-info font-weight-bold">User Address</label>
            </b-col>
            <b-col md="9" class="c-box">
              <b-form-textarea v-model="form.user_address"
                               rows="3"
              >
              </b-form-textarea>
            </b-col>
          </b-row>
          <b-row class=" mx-lg-4 align-items-center mh-lg">
            <b-col md="3">
              <label class="text-info font-weight-bold">User Telephone</label>
            </b-col>
            <b-col md="9" class="c-box">
              <b-form-input v-model="form.user_phone"
              >
              </b-form-input>
            </b-col>
          </b-row>
          <b-row class="mt-3">
            <b-col cols="12" class="text-right my-2">
              <b-button type="submit"  variant="info">Save</b-button>
              <b-button type="reset" variant="danger" @click="resetForm()">Reset</b-button>
            </b-col>
          </b-row>
        </b-form>
      </validation-observer>
  </div>
</template>

<script>
    import {ValidationObserver, ValidationProvider} from "vee-validate";

    export default {
        name:'profile-create',
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data() {
            return {
                avatar: require('~/assets/uploads/Profile_icon.png'),
                form: {}
            }
        },
        methods: {
            getValidationState(errors) {
                return errors.length > 0 ? false : null;
            },
            handleSubmit() {

            },
            uploadAvatar(input) {
                if (input) {
                    let reader = new FileReader();
                    reader.onload = e => {
                        this.avatar = e.target.result;
                    }
                    reader.readAsDataURL(input.target.files[0]);
                }

            },
            resetForm() {
                this.form = {};
                this.$nextTick(() => {
                    this.$refs.observer.reset();
                });

            },
            removeImage(){
                this.avatar= require('~/assets/uploads/Profile_icon.png');
                 this.$refs['file-input'].reset()
            }
        }
    }
</script>

<style scoped>

</style>
