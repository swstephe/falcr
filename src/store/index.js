import Vue from 'vue'
import Vuex from 'vuex'
import * as actions from './actions'
import * as getters from './getters'
import mutations from './mutations'

Vue.use(Vuex)

const state = {
  login_active: false,
  quote: {quote: '', author: ''},
  token: undefined
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})