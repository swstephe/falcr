import Vue from 'vue'
import App from './App.vue'
import store from './store'

new Vue({
  el: '#app',
  data: {
    login_active: false
  },
  store,
  render: h => h(App)
})
