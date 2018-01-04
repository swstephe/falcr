import * as types from './mutation-types'

export const getQuote = ({ commit }) => {
  return new Promise((resolve, reject) => {
    commit(types.QUOTES_GET_REQUEST)
    // api.getQuote(success, failure)
    commit(types.QUOTES_GET_SUCCESS, { quote: "A witty quote", author: "The Author" })
  })
}