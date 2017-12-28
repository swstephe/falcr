<template>
  <div class="container">
    <nav class="navbar is-white">
      <div class="navbar-brand">
        <a href="/" class="navbar-item brand-text">Falcr</a>
      </div>
      <div class="navbar-menu">
        <div class="navbar-end">
          <a href='#' class="navbar-item" @click='show_login'>Log In</a>
        </div>
      </div>
    </nav>
    <quote></quote>
    <login></login>
  </div>
</template>

<script>
import Quote from './components/Quote'
import Login from './components/Login'

export default {
  name: 'app',
  data () {
    return {
      'logged_in': true
    }
  },
  methods: {
    show_login () {
      this.$store.dispatch('show_login')
    }
  },
  components: {
    'quote': Quote,
    'login': Login
  }
}
</script>