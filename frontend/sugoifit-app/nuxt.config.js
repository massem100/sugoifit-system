// import VuetifyLoaderPlugin from 'vuetify-loader/lib/plugin'
import authRoutes from './middleware/authRoutes'
import pkg from './package'
// const pkg = require("./package");
export default {
  ssr: false,
  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'SugoiFit Financials',
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {hid: 'description', name: 'description', content: ''},
    ],
    link: [
      {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'},
      {rel: 'preconnect', href: 'https://fonts.gstatic.com' }, 
      {rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap'},
      

    ]

  },

  src: 'static/js/app.js',

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@fortawesome/fontawesome-svg-core/styles.css',
    'static/scss/website.css',
    '~assets/style/app.css',
    "assets/css/nucleo/css/nucleo.css",
    "assets/sass/argon.scss",
    "~assets/css/style.css"

  ],
  router: {
    middleware: ['csrf','authHeader', 'authRoutes'],
    // prefetchLinks: false,
  },
  
  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    {src: '~/plugins/vee-validate', ssr: false},
    {src: '~/plugins/axios'},
    {src: '~/plugins/dashboard/dashboard-plugin'},
    {src: '~/plugins/chartist', mode: 'client'},
    {src: '~/plugins/vue-ellipse-progress', ssr: false},
    {src: '~/plugins/fontawesome.js', ssr: false},
    {src: '~/plugins/addService.js', ssr: false},
    { src: '~/plugins/jquery.min.js', ssr: false },
    { src: '~plugins/vuedraggable.js',ssr:false }
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint,
    '@nuxtjs/fontawesome', 
    
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',

  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    [
      'nuxt-fontawesome', {
        imports: [
         {
           set: '@fortawesome/free-solid-svg-icons',
           icons: ['fas']
         },
         {
           set:'@fortawesome/free-brands-svg-icons',
           icons: ['fab']
         }
       ]
      }
],
        ['@nuxtjs/proxy']
  ],
  proxy:{
    '/api': { target: 'http://localhost:8080/api', pathRewrite: {'^/api': ''} }
  },
  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    proxy: true,
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en',
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
   /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
    }
   }
}

