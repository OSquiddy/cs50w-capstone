<template>
  <div class="container-fluid">
    <div v-if="!form" class="row login-img-container my-4 justify-content-around border border-dark">
      <div class="col-md-4 col-lg-3 my-3 p-0" @click="changeTab(0)">
        <img class="login-img" src="https://thumbs.dreamstime.com/t/international-doctors-day-greeting-card-design-159838679.jpg" alt="doctor-image" width="320" height="160" />
        <span class="doctor-img-text">Doctor</span>
      </div>
      <div class="col-md-4 col-lg-3 my-3 p-0" @click="changeTab(1)">
        <img class="login-img" src="https://motionarray.imgix.net/preview-462404-H5o4XXyCSeJ16iIT-large.jpg?w=1400&q=60&fit=max&auto=format" alt="doctor-image" width="320" height="160" />
        <span class="patient-img-text">Patient</span>
      </div>
    </div>
    <div v-else>
      <LoginForm :user="user" @cancel="cancel" />
    </div>
  </div>
</template>

<script>
import LoginForm from './LoginForm.vue'

export default {
  name: 'LoginPage',
  components: {
    LoginForm
  },
  data() {
    return {
      tabs: ['doctor', 'patient'],
      form: false,
      user: ''
    }
  },
  methods: {
    changeTab(index) {
      this.user = this.tabs[index]
      this.form = true
    },
    cancel(payload) {
      this.form = payload
      console.log('Payload is ', payload)
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
