<template>
  <section class="quote">
    <div class="column is-8 is-offset-2">
      <div class="card">
        <div class="card-content">
          <p class="title">
            <span v-if="isAuthenticated">{{ quote.quote }}</span>
            <span v-else>You are not logged in</span>
          </p>
          <br>
          <p class="subtitle">
            <span v-if="isAuthenticated">&mdash; {{ quote.author }}</span>
            <span v-else>Please log in to view quotes</span>
          </p>
          <p>
            <span v-if="isAuthenticated">You are logged in as in as <em>{{ user.email }}</em></span>
          </p>
        </div>
        <footer class="card-footer">
          <button v-if="isAuthenticated" class="card-footer-item" @click='getQuote'>Get Another Quote</button>
        </footer>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'home',
  computed: mapGetters([
    'isAuthenticated',
    'user',
    'quote'
  ]),
  methods: {
    ...mapActions([
      'getQuote'
    ])
  },
  mounted () {
    if (this.isAuthenticated) {
      this.getQuote()
    }
  }
}
</script>
