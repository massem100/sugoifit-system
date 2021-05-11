<template>
  <div>
    <base-alert v-if="alert.message"
                    :class="`alert ${alert.type}`"
                    style="
                           height: 3.5rem; 
                           width:100%;
                           z-index:1;" 
                      fade
                    @dismiss-count-down="countDownChanged"
                    :show="dismissCountDown"
                    dismissible
                     ><strong>Success:</strong> {{alert.message}}
      </base-alert>

      <nuxt />

  </div>
</template>

<script>
  export default {
    data() {
      return {
        isLoading: true,
        dismissSecs: 5,
        dismissCountDown: 0,
        showDismissibleAlert: false
      }
    },
    computed: {
        alert () {
            return this.$store.state.alert
        }
    },
  watch: {
        $route (to, from){
            // clear alert on location change
            this.$store.dispatch('alert/clear');
        }
  },
  methods: {
    countDownChanged(dismissCountDown) {
        this.dismissCountDown = dismissCountDown
      },
      showAlert() {
        this.dismissCountDown = this.dismissSecs
      }
  },
    mounted() {
      this.$nextTick(function() {
        this.isLoading = false
      });
    }
  }
</script>
