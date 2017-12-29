import * as types from './mutation-types'

export default {
  [types.LOGIN] (state) {
    state.pending = true;
  },
  [types.LOGIN_SUCCESS] (state) {
    state.isLoggedIn = true
    state.pending = false
  },
  [types.LOGOUT] (state) {
    state.isLoggedIn = false
  },
  [types.QUOTE] (state, { quote }) {
    state.quote = quote
  }
}
