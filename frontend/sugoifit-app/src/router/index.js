import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/Dashboard'
import Add_Transaction from '@/components/Add_Transaction'
import Login from '@/components/Login'
import Website from '@/components/Website'
import PlaceOrder from '@/components/PlaceOrder'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/transaction',
      name: 'Add_Transaction',
      component: Add_Transaction
    },
    {
      path: '/website',
      name: 'Website',
      component: Website
    },
    {
      path: '/placeorder',
      name: 'PlaceOrder',
      component: PlaceOrder
    }
  ],
  mode: 'history',
});
     
 