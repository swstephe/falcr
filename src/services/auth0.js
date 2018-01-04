import auth0 from 'auth0-js'

export default new auth0.WebAuth({
  domain: 'ariftek.auth0.com',
  clientID: '4N7SUHL1cO8KqRPe84T1OyKarQTH47pp',
  redirectUri: 'http://localhost:8085/callback',
  audience: 'https://ariftek.auth0.com/userinfo',
  responseType: 'token id_token',
  scope: 'openid email'
})
