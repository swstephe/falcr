import * as actions from './actions'
import * as getters from './getters'
import mutations from './mutations'

const state = {
  error: null,
  isRequesting: false,
  quote: {quote: '', author: ''}
}

export default {
  state,
  getters,
  actions,
  mutations
}