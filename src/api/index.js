import axios from 'axios'

export function login (creds, cb) {
  axios.post('/login', creds)
  .then(response => { cb(response.data.token) })
  .catch(error => { console.error(error)})
}

export function getQuote (cb) {
  let token = localStorage.getItem("token");
  axios.get('/quote', {headers: { Authorization: "Bearer " + token}})
  .then(response => { cb(response.data) })
  .catch(error => { console.error(error)})
}

