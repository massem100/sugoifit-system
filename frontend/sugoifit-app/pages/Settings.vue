<template>
  <b-container>
      <div>

        <!-- Quick Actions-->
        <b-tabs content-class="mt-3">
          <b-tab title="Your Profile" active>
            <p>I'm the first tab</p>
            <EditProfile />
          </b-tab>
          <b-tab title="Your Company">
            <p>I'm the second tab</p>
            <EditCompany />
          </b-tab>
          <b-tab title="Your Website">
            <p>I'm the second tab</p>
            <EditWebsite />
          </b-tab>
        </b-tabs>
      </div>

    </b-container>
</template>

<script>
import EditCompany from '../../sugoifit-app/components/settings/editcompany';
import EditProfile from '../../sugoifit-app/components/settings/editprofile';
import EditWebsite from '../../sugoifit-app/components/settings/editwebsite';
export default {
    name: "Settings",
    layout: 'DashboardLayout'
};
</script>

<style scoped>

</style>