import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import theme from '~/plugins/theme'
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'

Vue.use(Vuetify, {
  iconfont: 'mdi',
  treeShake: true,
    customVariables: ['~/assets/style/variables.scss'],
  theme
});
