import * as types from './mutation-types'
import auth0 from '../../../services/auth0'

export const login = ({ state, commit }, options) => {
  return new Promise((resolve, reject) => {
    commit(types.AUTH0_LOGIN_REQUEST)
    auth0.authorize(options, (err, result) => {
      if (err) {
        commit(types.AUTH0_LOGIN_FAILURE, {
          error: {
            error: err.details.error,
            message: err.details.error_description
          }
        })
        return reject(err)
      }
      commit(types.AUTH0_LOGIN_SUCCESS, result)
      return resolve()
    })
  })
}

export const logout = ({ commit }) => {
  return new Promise((resolve, reject) => {
    commit(types.AUTH0_LOGOUT)
    return resolve()
  })
}

export const handleAuthentication = ({ state, commit, dispatch }) => {
  return new Promise((resolve, reject) => {
    auth0.parseHash((err, authResult) => {
      if (authResult && authResult.accessToken && authResult.idToken) {
        commit(types.AUTH0_LOGIN_SUCCESS, {authResult, user: {email: authResult.idTokenPayload.email}})
        dispatch('getQuote', null, {root: true})
        return resolve()
      } else if (err) {
        commit(types.AUTH0_LOGIN_FAILURE, {
          error: {
            error: err.error,
            message: err.error_description
          }
        })
        return reject(err.error)
      }
    })
  })
}

export const refreshToken = ({ state, commit }) => {
  return new Promise((resolve, reject) => {
    commit(types.AUTH0_REFRESH_TOKEN_REQUEST)
    auth0.refreshToken(state.refreshToken, (err, result) => {
      if (err) {
        console.error(err)
        commit(types.AUTH0_REFRESH_TOKEN_FAILURE, {
          error: {
            error: err.details.error,
            message: err.details.error_description
          }
        })
      }
      commit(types.AUTH0_REFRESH_TOKEN_SUCCESS, result)
      return resolve()
    })
  })
}
