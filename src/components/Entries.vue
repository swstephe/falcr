<template>
    <div>
        <p>{{ entries }}</p>
        <form @submit.prevent="addEntry({title: new_entry.title, text: new_entry.text})" action="#" method="post" class="add-entry">
            <dl>
                <dt>Title:</dt>
                <dd><input v-model="new_entry.title" type="text" size="30" name="title"></dd>
                <dt>Text:</dt>
                <dd><textarea v-model="new_entry.text" name="text" cols="40" rows="5"></textarea></dd>
                <dd><button type="submit">Share</button></dd>
            </dl>
        </form>
        <ul class="entries">
            <li v-for="entry in entries">
                <h2>{{ entry.title }}</h2>
                {{ entry.text }}
            </li>
            <li v-if="!entries">
                <em>Unbelievable.  No entries here so far</em>
            </li>
        </ul>
    </div>
</template>

<script>
    import { mapGetters, mapActions } from 'vuex'

    export default {
        name: "entries",
        data () {
            return {
                new_entry: {
                    title: 'title',
                    text: 'text'
                }
            }
        },
        computed: mapGetters({
            entries: 'getEntries'
        }),
        methods: mapActions([
            'addEntry'
        ]),
        created () {
            this.$store.dispatch('getEntries')
        }
    }
</script>

<style scoped>
.entries {
    list-style: none;
    margin: 0;
    padding: 0;
}
.entries li {
    margin: 0.8em 1.2em;
}
.entries li h2 {
    margin-left: -1em;
}
.add-entry {
    font-size: 0.9em;
    border-bottom: 1px solid #ccc;
}
.add-entry dl {
    font-weight: bold;
}
</style>