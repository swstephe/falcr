<template>
  <div class="container">
    <nav class="navbar is-white">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item brand-text">Auth</router-link>
      </div>
      <div class="navbar-menu">
        <div class="navbar-start">
          <router-link to="/quote" class="navbar-item">Quote</router-link>
        </div>
        <div class="navbar-end">
          <a @click='login' class="navbar-item">Log In</a>
          <a @click='logout' class="navbar-item">Log Out</a>
        </div>
      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'app',
  computed: {
    ...mapGetters([
      'isAuthenticated'
    ])
  },
  methods: {
    ...mapActions([
      'login',
      'logout'
    ])
  }
}
</script>
