<template>
  <div class="container">
    <form class="text-left" @submit.prevent="submitForm">
      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Email address</label>
        <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="email" />
        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
      </div>
      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Password</label>
        <input type="password" class="form-control" id="exampleInputPassword1" v-model="password" />
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
// import LoginForm from './LoginForm.vue'
/* eslint-disable dot-notation */
import axios from 'axios'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'LoginPage',
  components: {
    // LoginForm
  },
  data() {
    return {
      tabs: ['doctor', 'patient'],
      form: false,
      user: '',
      email: '',
      password: '',
      errors: []
    }
  },
  computed: {
    ...mapState(['currentUser'])
  },
  methods: {
    ...mapActions(['setToken', 'removeToken', 'setCurrentUser']),
    changeTab(index) {
      this.user = this.tabs[index]
      this.form = true
    },
    cancel(payload) {
      this.form = payload
      console.log('Payload is ', payload)
    },
    async submitForm () {
      console.log('Form was submitted')
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('token')

      console.log(this.email)
      const formData = {
        username: this.email,
        password: this.password
      }
      try {
        const response = await axios.post(process.env.VUE_APP_API_URL + '/token/login', formData)
        const token = response.data.auth_token
        this.setToken(token)
        axios.defaults.headers.common['Authorization'] = 'Token ' + token
        localStorage.setItem('token', token)
        // console.log(axios.defaults.headers.common)
        localStorage.setItem('isAuthenticated', 'true')
        // console.log('Redirect to ', this.$route)
        const user = await axios.get(process.env.VUE_APP_API_URL + '/users/me')
        // const user = await axios.get(process.env.VUE_APP_API_URL + '/users/me', {
        //   headers: {
        //     Authorization: 'Token ' + token
        //   }
        // })
        if (user.data && user.data.isDoctor) {
          // console.log(user.data)
          this.setCurrentUser(user.data)
          localStorage.setItem('currentUser', JSON.stringify(user.data))
          const toPath = this.$route.query.to || '/'
          this.$router.push(toPath)
        } else {
          console.log('This id does not belong to a doctor')
        }
        // }
      } catch (error) {
        if (error.response) {
          for (const property in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`)
          }
        } else {
          this.errors.push('Something went wrong. Please try again')

          console.log(JSON.stringify(error))
        }
      }
      // } else {
      // console.log('User is not a doctor')
      // }
      // await axios.post(process.env.VUE_APP_API_URL + '/token/login', formData).then((response) => {
      //   const token = response.data.auth_token
      //   this.setToken(token)
      //   axios.defaults.headers.common['Authorization'] = 'Token ' + token
      //   localStorage.setItem('token', token)
      //   localStorage.setItem('isAuthenticated', 'true')
      //   console.log('Redirect to ', this.$route)
      //   const toPath = this.$route.query.to || '/'
      //   this.$router.push(toPath)
      // })
      //   .catch(error => {
      //     if (error.response) {
      //       for (const property in error.response.data) {
      //         this.errors.push(`${property}: ${error.response.data[property]}`)
      //       }
      //     } else {
      //       this.errors.push('Something went wrong. Please try again')

      //       console.log(JSON.stringify(error))
      //     }
      //   })
    }
  }
}
</script>

<style>
.login-img-container {
  position: relative;
}

.login-img {
  width: 100%;
}

.doctor-img-text,
.patient-img-text {
  position: absolute;

  bottom: 0;
  left: 10px;
  /* color: white; */
  /* text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.7); */
}
</style>
