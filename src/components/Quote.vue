<template>
  <section class="quote">
    <div class="column is-8 is-offset-2">
      <div class="card">
        <div class="card-content">
          <p class="title">
            <span v-if="isLoggedIn">{{ quote.quote }}</span>
            <span v-else>You are not logged in</span>
          </p>
          <br>
          <p class="subtitle">
            <span v-if="isLoggedIn">&mdash; {{ quote.author }}</span>
            <span v-else>Please log in to view quotes</span>
          </p>
        </div>
        <footer class="card-footer">
          <button v-if="isLoggedIn" class="card-footer-item" @click='getQuote'>Get Another Quote</button>
        </footer>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'quote',
  computed: mapGetters([
    'isLoggedIn',
    'quote'
  ]),
  methods: {
    ...mapActions([
      'getQuote'
    ])
  },
  created () {
    if (this.isLoggedIn) {
      this.getQuote()
    }
  }
}
</script>
