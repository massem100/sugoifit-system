<template>
    
    <b-col class="d-flex flex-column justify-content-center align-items-center w-100 h-100">
        <!-- <base-alert v-if= "alert.message" 
                    class = "mt-5 d-flex flex-row justify-content-center" 
                    :class="`alert ${alert.type}`"
                    style="width: 25rem; 
                           height: 3rem; " 
                    dismissible      
                    >{{alert.message}} 
        </base-alert>-->
        <b-col class="d-flex flex-column align-items-center justify-content-center mt-5 h-100 ">
            <h2 class ="text-center"> Login </h2>                
            <p class ="text-center"> Welcome back, enter your username and password</p>
            
            <b-form id = "LoginForm" 
                    class ="h-100  w-25 d-flex flex-column " 
                    @submit.prevent = "LoginUser" 
                    method ="POST">
             
            
                <label class =" form-label text-left" 
                       for ="email">Email:
                </label>
                <b-form-input class ="form-control mt-2" 
                              type="text" 
                              name="email" 
                              v-model="email"
                              id="email">
                </b-form-input>
            
                <label class ="form-label mt-4" 
                       for="password"> Password:</label> 
                <b-form-input class ="form-control mt-2" 
                              type="password" 
                              name="password" 
                              v-model="password"
                              id="password">
                </b-form-input>
            
                <b-col class =" align-items-center mt-2">
                    <!-- <div  id="msgBox">
                        <p> {{alert.message}} </p>
                    </div> -->
                    <button  style = "background-color: #7CC3CD;" 
                             class="d-flex flex-row justify-content-center btn submit text-white" 
                             id="submit"
                             type="submit"> 
                             Submit 
                    </button>
                    <p class ="login-text m-3">Dont have an account? 
                        <nuxt-link :to="{name:'auth-register'}">Sign up your business! </nuxt-link>
                    </p>
                </b-col>
            </b-form>
        
                
        </b-col> 
    
    
    </b-col>
</template>

<script>
import BaseAlert from '../../components/argon-core/BaseAlert.vue';
import Vuex from "vuex";
import store from '../../store'
import { mapGetters,  mapActions,  mapMutations} from 'vuex'



export default {
  components: {BaseAlert },
    name: 'auth-login',
    head(){
    return{
        title: 'Login'
    }
  },
  mounted(){

   },
    data(){
        return{
           token: '', 
           email: '',
           password: '',
           submitted: false,
        }
    }, 
    computed: {
        loggingIn () {
            return this.$store.state.authentication.status.loggingIn;
        },

        alert () {
            return this.$store.state.alert
        }
    },
    created () {
        // reset login status
        this.$store.dispatch('authentication/reset');
    },
    computed: {
        alert () {
            return this.$store.state.alert
        }
    },
    watch:{
        $route (to, from){
            // clear alert on location change
            this.$store.dispatch('alert/clear');
        }
    },
    methods: {
        // ...mapActions({
        //       alert_s:'alert/success'
        //   }),
        LoginUser: function(e) {
            this.submitted = true;
            let loginForm = document.getElementById("LoginForm");
            let form_data = new FormData(loginForm);
            form_data.append('form id', loginForm.getAttribute("id"));
            const { dispatch } = this.$store;
            try {
                 if (form_data) {
             
                    this.$store.dispatch('authentication/login', { form_data });
                    $nuxt.$router.push('/');
                    this.$store.dispatch('alert/clear');
                        
                        
                    
    
                }
            } catch (error) {
                console.log(error);
            }
           
        }
    }
   
}

</script>

<style scoped>

</style>
