<template>
  <div class="modal" :class="{'is-active': is_active}">
    <div class="modal-background"></div>
    <div class="modal-content">
      <div class="box">
        <form @submit.prevent>
          <div class="field">
            <label class="label" for="email">Email:</label>
            <div class="control">
              <input class="input" id="email" name="email" type="email" v-model="email"/>
            </div>
          </div>
          <div class="field">
            <label class="label" for="password">Password:</label>
            <div class="control">
              <input class="input" id="password" name="password" type="password" v-model="password"/>
            </div>
          </div>
          <a class="button is-block is-info is-large" @click='login(email, password)'>Log in</a>
        </form>
      </div>
    </div>
    <button class="modal-close is-large" aria-label="close" @click='hide_login'></button>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'login',
  data () {
    return {
      email: '',
      password: ''
    }
  },
  computed: {
    ...mapGetters([
      'is_active'
    ]),
  },
  methods: {
    ...mapActions([
      'login',
      'hide_login'
    ])
  }
}
</script>
