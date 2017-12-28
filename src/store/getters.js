export const is_active = state => {
  return state.login_active
}

export const getLoggedIn = state => {
  return state.token ? true : false
}

export const getQuote = state => {
  return state.quote
}

export const getToken = state => {
  return state.token
}