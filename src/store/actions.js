import * as api from '../api'
import * as types from './mutation-types'

export const login = ({ state, commit, rootState }, creds) => {
  commit(types.LOGIN)
  api.login(creds, token => {
    localStorage.setItem("token", token)
    commit(types.LOGIN_SUCCESS)
    getQuote({ commit })
  })
}

export const logout = ({ commit }) => {
  localStorage.removeItem("token")
  commit(types.LOGOUT)
}

export const getQuote = ({ commit }) => {
  api.getQuote(quote => {
    commit(types.QUOTE, { quote })
  })
}

