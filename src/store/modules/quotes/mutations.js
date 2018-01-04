import * as types from './mutation-types'

export default {
  [types.QUOTES_GET_REQUEST] (state) {
    state.isRequesting = true
  },

  [types.QUOTES_GET_FAILURE] (state, {error}) {
    state.error = error
    state.isRequesting = false
  },

  [types.QUOTES_GET_SUCCESS] (state, {quote}) {
    state.quote = quote
    state.error = null
    state.isRequesting = false
  }
}