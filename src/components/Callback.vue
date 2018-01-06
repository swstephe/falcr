<template>
  <section class="hero is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-6 is-offset-3">
            <figure class="image is-128x128 is-centered">
              <img src="../assets/loading.svg" alt="loading...">
            </figure>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  import store from '../store'
  import router from '../router'

  export default {
    name: "callback",
    mounted () {
      store.dispatch('handleAuthentication')
      router.replace('/')
    }
  }
</script>
