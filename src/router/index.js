import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'

import Home from '../components/Home.vue'
import Callback from '../components/Callback.vue'

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/home',
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
      redirect: '/home'
    }
  ]
})

export default router
