import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/Dashboard'
import Add_Transaction from '@/components/Add_Transaction'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/transaction',
      name: 'Add_Transaction',
      component: Add_Transaction,
    }
    
  ]
})
