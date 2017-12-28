export const getEntries = state => {
    return state.entries.map(({ id, title, text }) => {
        return {
            id: id,
            title: title,
            text: text
        }
    })
}