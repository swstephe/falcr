import * as types from './mutation-types'
import * as quotes from '../../../services/quotes'

export const getQuote = ({ commit }) => {
  return new Promise((resolve, reject) => {
    commit(types.QUOTES_GET_REQUEST)
    quotes.getQuote(quote => {
      commit(types.QUOTES_GET_SUCCESS, { quote })
      return resolve()
    })
  })
}