<template>
  <div class="container">
    <nav class="navbar is-white">
      <div class="navbar-brand">
        <a href="/" class="navbar-item brand-text">Falcr</a>
      </div>
      <div v-if="isLoggedIn" class="navbar-menu">
        <div class="navbar-end">
          <a href="#" class="navbar-item" @click="logout()">Log Out</a>
        </div>
      </div>
    </nav>
    <quote></quote>
    <login></login>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  import Quote from './components/Quote'
  import Login from './components/Login'

  export default {
    name: 'app',
    computed: {
      ...mapGetters([
        'isLoggedIn'
      ])
    },
    methods: {
      ...mapActions([
        'logout'
      ])
    },
    components: {
      'quote': Quote,
      'login': Login
    }
  }
</script>