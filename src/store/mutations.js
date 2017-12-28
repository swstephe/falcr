import Vue from 'vue'
import * as types from './mutation-types'

export default {
    [types.GET_ENTRIES] (state, { entries }) {
        console.log("entries")
        console.log(entries)
        entries.forEach(entry => {
            addEntry(state, entry)
        })
    },
    [types.ADD_ENTRY] (state, { entry }) {
        addEntry(state, entry)
    }
}

function addEntry (state, entry) {
    console.log("mutations.addEntry")
    console.log(entry)
    state.entries.push(entry)
}