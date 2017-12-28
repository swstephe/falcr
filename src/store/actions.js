import * as api from '../api'
import * as types from './mutation-types'

export const quote = ({ commit }, token) => {
  api.quote(token, quote => {
    commit(types.QUOTE, { quote })
  })
}

export const login = ({ commit }, email, password) => {
  api.login(email, password, token => {
    commit(types.LOGIN, { token })
  })
}

export const show_login = ({ commit }) => {
  commit(types.SHOW_LOGIN)
}

export const hide_login = ({ commit }) => {
  commit(types.HIDE_LOGIN)
}