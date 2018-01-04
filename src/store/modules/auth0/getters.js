export const isAuthenticated = (state) => {
  if (typeof state.idToken !== 'string') {
    return false
  }
  return new Date().getTime() < state.expiresAt
}

export const user = (state) => {
  return state.user
}

export const refreshToken = (state) => {
  return state.refreshToken
}