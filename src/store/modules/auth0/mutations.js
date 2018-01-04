import * as types from './mutation-types'

export default {
  [types.AUTH0_LOGIN_REQUEST] (state) {
    state.isAuthenticating = true
  },

  [types.AUTH0_LOGIN_FAILURE] (state, {error}) {
    state.error = error
    state.isAuthenticating = false
  },

  [types.AUTH0_LOGIN_SUCCESS] (state, { authResult, user }) {
    state.idToken = authResult.idToken
    state.accessToken = authResult.accessToken
    state.expiresAt = authResult.expiresIn*1000 + new Date().getTime()
    state.refreshToken = authResult.refreshToken
    state.user = user
    state.error = null
    state.isAuthenticating = false
  },

  [types.AUTH0_LOGOUT] (state) {
    state.idToken = null
    state.accessToken = null
    state.expiresAt = 0
    state.refreshToken = null
    state.user = null
    state.error = null
  },

  [types.AUTH0_REFRESH_TOKEN_FAILURE] (state, {error}) {
    state.error = error
  },

  [types.AUTH0_REFRESH_TOKEN_SUCCESS] (state, {id_token}) {
    state.idToken = id_token
  },

  [types.AUTH0_GET_PROFILE_REQUEST] (state) {
    // 
  },

  [types.AUTH0_GET_PROFILE_FAILURE] (state, {error}) {
    state.error = error
  },

  [types.AUTH0_GET_PROFILE_SUCCESS] (state, {profile}) {
    state.profile = profile
    state.error = null
  }
}