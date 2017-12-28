<template>
    <div class="page">
        <h1>Falcr</h1>
        <div class="metanav">
            <a v-if="logged_in" href="/login">log in</a>
            <a v-else href="/logout">log out</a>
        </div>
        <entries></entries>
    </div>
</template>

<script>
    import Entries from './components/Entries'

    export default {
        name: "app",
        data () {
            return {
                'logged_in': true
            }
        },
        components: {
            'entries': Entries
        }
    }
</script>

<style scoped>
.page {
    margin: 2em auto;
    width: 35em;
    border: 5px solid #ccc;
    padding: 0.8em;
    background: white;
}
.metanav {
    text-align: right;
    font-size: 0.8em;
    padding: 0.3em;
    margin-bottom: 1em;
    background: #fafafa;
}
</style>