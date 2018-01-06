import axios from 'axios'
import store from '../store'

export function getQuote (cb) {
  let token = store.state.auth0.idToken
  axios.get('/quote', {headers: { Authorization: "Bearer " + token}})
  .then(response => { cb(response.data) })
  .catch(error => { console.error(error)})
}

