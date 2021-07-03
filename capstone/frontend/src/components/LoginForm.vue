<template>
  <div class="login-form">
    <!-- <b-form-group :label="userType" label-align="left">
      <b-form-input></b-form-input>
    </b-form-group>
    <b-form-group label="Password" label-align="left">
      <b-form-input></b-form-input>
    </b-form-group> -->
    <div @click="cancel">Cancel</div>
    <br />
    <b-form @submit.prevent="onSubmit">
      <b-form-group id="input-group-1" label="Username:" label-for="input-1">
        <b-form-input id="input-1" placeholder="Enter username" v-model="username" required></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Your Password:" label-for="input-2">
        <b-form-input type="password" id="input-2" placeholder="Enter password" required v-model="password"></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>

    <form class="text-left">
      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Email address</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
      </div>
      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Password</label>
        <input type="password" class="form-control" id="exampleInputPassword1" />
      </div>
      <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1" />
        <label class="form-check-label" for="exampleCheck1">Check me out</label>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import Cookies from 'js-cookie'

export default {
  name: 'LoginForm',
  props: {
    user: {
      type: String
    }
  },
  data() {
    return {
      show: true,
      username: null,
      password: null
    }
  },
  computed: {
    userType() {
      return this.user.charAt(0).toUpperCase() + this.user.slice(1) + ' ID'
    }
  },
  mounted() {
    this.getCSRFToken()
  },
  methods: {
    cancel() {
      this.$emit('cancel', false)
    },
    async getCSRFToken() {
      const token = await axios.get('http://localhost:8000/api/csrf')
      console.log('Result of axios call:', token)
      Cookies.set('csrftoken', token.data.token)
    },
    async onSubmit() {
      const csrftoken = Cookies.get('csrftoken')
      console.log(csrftoken)
      fetch('http://localhost:8000/api/login', {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        body: JSON.stringify({
          username: this.username,
          password: this.password
        })
      })
        .then((response) => response.json())
        .then((data) => console.log(data))
        .catch((error) => console.log(error))
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
