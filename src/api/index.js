import axios from 'axios'

export function getEntries (cb) {
    axios.get('/entries')
    .then(response => {
        console.log("api.get.response")
        console.log(response)
        cb(response.data.entries)
    })
    .catch(error => { console.log(error) })
}

export function addEntry ({ title, text}, cb) {
    console.log("title=" + title)
    console.log("text=" + text)
    axios.post('/entries', {title: title, text: text})
    .then(response => {
        console.log("api.post.response")
        console.log(response)
        cb({id: response.data.id, title: title, text: text})
    })
    .catch(error => { console.log(error) })
}