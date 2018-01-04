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

export const handleAuthentication = ({ state, commit }) => {
  return new Promise((resolve, reject) => {
    auth0.parseHash((err, authResult) => {
      if (authResult && authResult.accessToken && authResult.idToken) {
        auth0.client.userInfo(authResult.accessToken, (err, user) => {
          console.log("userInfo")
          console.log(err)
          console.log(user)
          console.log(user.email)
          if (err) {
            user = null;
          }
          commit(types.AUTH0_LOGIN_SUCCESS, { authResult, user })
        })
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
    console.log("refreshToken request...")
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
      console.info(result)
      commit(types.AUTH0_REFRESH_TOKEN_SUCCESS, result)
      return resolve()
    })
  })
}

export const getUser = ({ state, commit, dispatch }) => {
  return new Promise((resolve, reject) => {
    if (state.user) {
      // Do not load profile if it already exists in state.
      return resolve()
    }
    commit(types.AUTH0_GET_PROFILE_REQUEST)
    auth0.getUser(state.idToken, (err, profile) => {
      if (err) {
        if (err.error == 401) {
          return dispatch(types.AUTH0_LOGOUT)
        }
        commit(types.AUTH0_GET_PROFILE_FAILURE, { error: err })
        return reject(err)
      }
      commit(types.AUTH0_GET_PROFILE_SUCCESS, { profile })
      return resolve()
    })
  })
}
