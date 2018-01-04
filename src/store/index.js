import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

import auth0 from './modules/auth0'
import quotes from './modules/quotes'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    auth0,
    quotes
  },
  plugins: [
    createPersistedState({
      paths: [
        'auth0.accessToken',
        'auth0.idToken',
        'auth0.user',
        'auth0.expiresAt'
      ]
    })
  ]
})

export default store