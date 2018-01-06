import * as actions from './actions'
import * as getters from './getters'
import mutations from './mutations'

let prev_state = localStorage.getItem('vuex')
if (prev_state) {
  prev_state = JSON.parse(prev_state)
} else {
  prev_state = {
    auth0: {
      accessToken: null,
      expiresAt: 0,
      idToken: null,
      user: null,
      refreshToken: null
    }
  }
}

const state = {
  accessToken: prev_state.auth0.accessToken,
  error: null,
  expiresAt: prev_state.auth0.expiresAt,
  idToken: prev_state.auth0.idToken,
  isAuthenticating: false,
  user: prev_state.auth0.user,
  refreshToken: prev_state.auth0.refreshToken
}

export default {
  state,
  getters,
  actions,
  mutations
}