import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../components/Home.vue'
import Callback from '../components/Callback.vue'

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/callback',
      name: 'Callback',
      component: Callback
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})