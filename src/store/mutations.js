import Vue from 'vue'
import * as types from './mutation-types'

export default {
  [types.QUOTE] (state, { quote }) {
    state.quote = quote
  },
  [types.LOGIN] (state, { token }) {
    state.token = token
  },
  [types.SHOW_LOGIN] (state) {
    state.login_active = true
  },
  [types.HIDE_LOGIN] (state) {
    state.login_active = false
  }
}
