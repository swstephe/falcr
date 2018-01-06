import * as auth0 from 'auth0-js'

export default new auth0.WebAuth({
  domain: 'ariftek.auth0.com',
  clientID: 'H6L6IkdiJsZSVMkn7FljrjaAr11dIVLh',
  redirectUri: 'http://localhost:8080/callback',
  audience: 'https://falcr.ariftek.com/',
  responseType: 'token id_token',
  scope: 'openid email'
})
