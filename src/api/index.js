import axios from 'axios'

export function login (email, password, cb) {
  console.log("email/password")
  console.log(email)
  console.log(password)
  console.log(cb)
  axios.post('/login', {email: email, password: password})
  .then(response => { cb(response.data.token) })
  .catch(error => { console.error(error)})
}

export function quote (token, cb) {
  axios.get('/quote', {headers: { Authorization: "Bearer " + token}})
  .then(response => { cb(response.data) })
  .catch(error => { console.error(error)})
}

