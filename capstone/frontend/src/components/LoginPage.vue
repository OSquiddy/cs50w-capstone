<template>
  <div class="container-fluid">
    <form class="text-left" @submit.prevent="submitForm" id="form">
      <div class="form-header">
        <svg width="44" height="46" viewBox="0 0 44 46" fill="none" xmlns="http://www.w3.org/2000/svg" class="logo-svg">
            <rect x="14.5332" y="1" width="14.5329" height="43.5986" fill="#DB1111" />
            <rect y="15.533" width="43.5986" height="14.5329" fill="#DB1111" />
            <path d="M14.5327 29.7021L21.4358 1.36302" stroke="white" stroke-width="2" stroke-linecap="round" />
            <path d="M29.0653 30.0651L21.4355 1.36269" stroke="white" stroke-width="2" stroke-linecap="round" />
            <path d="M14.5327 15.8958L21.7991 44.2349" stroke="white" stroke-width="2" stroke-linecap="round" />
            <path d="M29.0644 15.8958L21.7981 44.2349" stroke="white" stroke-width="2" stroke-linecap="round" />
            <path d="M7.26611 22.0723L36.3318 22.4356" stroke="white" stroke-width="2" stroke-linecap="round" />
          </svg>
          <span class="logo-text">Avicenna Hospital</span>
      </div>
      <div class="input-container">
        <div class="form-group floatingLabelField">
            <input class="form-control" type="text" name="username" id="username" required placeholder="Username" v-model="username">
            <label for="username" class="label">Username</label>
        </div>
        <div class="form-group floatingLabelField">
            <input class="form-control" type="password" name="password" id="password" required placeholder="Password" v-model="password">
            <label for="password" class="label">Password</label>
        </div>
        <a href="#" class="forgot">Forgot Password?</a>
        <button type="submit" class="btn">Sign In</button>
      </div>
      <!-- <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" class="form-control" id="username" v-model="username" />
      </div>
      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Password</label>
        <input type="password" class="form-control" id="exampleInputPassword1" v-model="password" />
      </div>
      <button type="submit" class="btn btn-primary">Submit</button> -->
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
      username: '',
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

      console.log(this.username)
      const formData = {
        username: this.username,
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

<style lang="scss" scoped>
.container-fluid {
  display: flex;
  border: 1px solid;
  height: 100%;
  background: var(--light-gray);
}

#form {
    max-width: 300px;
    background: var(--background-primary);
    box-shadow: 0 3px 20px 0 rgb(0 0 0 / 10%);
    border-radius: 5px;
    overflow: hidden;
    margin: auto;
    display: flex;
    flex-direction: column;
}

::v-deep .form-header {
  display: flex;
  align-items: center;
  padding: 15px;
  background: var(--primary-accent-dark);
  .logo-svg {
    border: black;
    margin-right: 10px;
    rect {
      fill: var(--background-primary);
    }
    path {
      stroke: var(--primary-accent-dark);
    }
  }
  .logo-text {
    color: var(--background-primary);
  }
}

#form .input-container {
  padding: 50px;
}

#form .btn {
  margin-top: 30px;
  width: 100%;
  background: var(--primary-accent-dark);
  color: var(--background-primary);
  &:focus {
    box-shadow: 0 0 0 0.25rem rgb(198 0 0 / 25%) !important;
    // background-color: rgb(198 0 0 / 25%);
  }
}

.floatingLabelField {
    position: relative !important;
    margin-top: 0px;
    margin-bottom: 7px;
    padding-bottom: 5px;
    border-bottom: 1px solid #9e9e9e;
}

.floatingLabelField:focus-within {
    border-bottom: 2px solid #03a9f4;
}

#form .forgot {
  display: flex;
  font-size: 0.75rem;
  // text-align: right;
  margin-top: 10px;
  justify-content: flex-end;
}

#form .form-control {
    display: block;
    width: 100%;
    padding: 20px 10px 0;
    border: none;
    border-radius: 0;
    padding-bottom: 5px;
}

#form .form-control:focus {
    box-shadow: none;
    border: none;
    outline: none;
}

#form .label {
    position: absolute;
    pointer-events: none;
    top: 5px;
    left: 0px;
    opacity: 0;
    font-size: 13px;
    background-color: transparent;
    padding: 0 10px;
    -webkit-transition: 0.2s ease-in-out;
    transition: 0.2s ease-in-out;
}

#form .form-control:not(:placeholder-shown)+.label {
    opacity: 1;
    top: -2px;
    color: #03a9f4;
}
</style>
