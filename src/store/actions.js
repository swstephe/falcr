import * as api from '../api'
import * as types from './mutation-types'

export const getEntries = ({ commit }) => {
    api.getEntries(entries => {
        commit(types.GET_ENTRIES, {
            entries
        })
    })
}

export const addEntry = ({ commit }, payload) => {
    console.log("addEntry:payload:")
    console.log(commit)
    console.log(payload)
    api.addEntry(payload, entry => {
        commit(types.ADD_ENTRY, { entry })
    })
}