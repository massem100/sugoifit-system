<template>
  <v-app>
    <core-filter />

    <core-toolbar />

    <core-drawer />

    <core-view />
  </v-app>
</template>

<script>
  import coreFilter from '~/components/core/AppFilter';
  import coreToolbar from '~/components/core/AppToolbar';
  import coreDrawer from '~/components/core/AppDrawer';
  import coreView from '~/components/core/AppView';

  export default {
    components: {
      coreFilter,
      coreToolbar,
      coreDrawer,
      coreView
    }
  }
</script>

<style lang="scss">
  /* Remove in 1.2 */
  .v-datatable thead th.column.sortable i {
    vertical-align: unset;
  }

  * {
  box-sizing: border-box;
}

html, body {
  margin: 0;
  padding: 0;
}

body, input, button, select, textarea {
  font: 400 1rem "Poppins", sans-serif;
  color: #222222;
}

a {
  text-decoration: none;
}

ul, ol {
  margin: 0 0 1rem;
  padding: 0 0 1rem;
  box-sizing: border-box;
}

v-app{
  font-family: "Poppins";
  font: 400 1rem "Poppins";
}
</style>
