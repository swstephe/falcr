import * as auth0 from 'auth0-js'

export default new auth0.WebAuth({
  domain: 'ariftek.auth0.com',
  clientID: 'NjYo5Wd169t0G4IPLspKBgQtjJif1cd0',
  redirectUri: 'http://localhost:8080/callback',
  audience: 'https://ariftek.auth0.com/userinfo',
  responseType: 'token id_token',
  scope: 'openid email'
})
