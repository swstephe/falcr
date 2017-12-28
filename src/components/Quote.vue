<template>
  <section class="quote">
    <div class="column is-8 is-offset-2">
      <div v-if="!getLoggedIn" class="card">
        <div class="card-content">
          <p class="title">You are not logged in</p>
          <p class="subtitle">Please log in to view quotes</p>
        </div>
      </div>
      <div v-else class="card">
        <div class="card-content">
          <p class="title">{{ getQuote.quote }}</p>
          <p class="subtitle">{{ getQuote.author }}</p>
        </div>
        <button class="is-primary" @click='get_quote'>Get Another Quote</button>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'quote',
  computed: mapGetters([
    'getLoggedIn',
    'getQuote',
    'getToken'
  ]),
  methods: {
    ...mapActions([
      'quote'
    ]),
    get_quote () {
      this.quote(this.getToken)
    }
  }
}
</script>
