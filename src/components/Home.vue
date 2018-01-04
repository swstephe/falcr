<template>
  <div>
    <div>Home</div>
    <div>
      <span v-if="isAuthenticated">You are logged in as <em>{{ user.email }}</em></span>
      <span v-else>You are not logged in</span>
    </div>

  </div>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'home',
    computed: {
      ...mapGetters([
        'isAuthenticated',
        'user'
      ])
    }
  }
</script>
