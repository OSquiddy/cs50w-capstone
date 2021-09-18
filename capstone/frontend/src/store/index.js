import Vue from 'vue'
import Vuex from 'vuex'
import search from './search'
import axios from 'axios'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    token: null,
    isAuthenticated: false,
    isMobile: false,
    isCollapsed: false,
    patient: {},
    doctor: {},
    currentUser: {}
  },
  actions: {
    toggleCollapse({ commit }) {
      commit('TOGGLE_COLLAPSE')
    },
    async getPatientInfo({ commit }, patientID) {
      const response = await axios.get(process.env.VUE_APP_API_URL + '/p/' + patientID)
      const value = response.data.patientInfo
      sessionStorage.setItem('patient', JSON.stringify(value))
      commit('GET_PATIENT_INFO', value)
    },
    async getDoctorInfo({ commit }, doctorID) {
      const response = await axios.get(process.env.VUE_APP_API_URL + '/d/' + doctorID)
      const value = response.data.doctorInfo
      sessionStorage.setItem('doctor', JSON.stringify(value))
      commit('GET_DOCTOR_INFO', value)
    },
    setCurrentUser({ commit }, value) {
      commit('SET_CURRENT_USER', value)
    },
    checkToken({ commit }) {
      commit('CHECK_TOKEN')
    },
    setToken({ commit }, value) {
      commit('SET_TOKEN', value)
    },
    removeToken({ commit }, value) {
      commit('REMOVE_TOKEN', value)
    },
    setMobileView({ commit }, value) {
      commit('SET_MOBILE_VIEW', value)
    }
  },
  mutations: {
    SET_MOBILE_VIEW(state, payload) {
      state.isMobile = payload
    },
    TOGGLE_COLLAPSE(state) {
      state.isCollapsed = !state.isCollapsed
      sessionStorage.setItem('isCollapsed', state.isCollapsed)
    },
    SET_CURRENT_USER(state, payload) {
      state.currentUser = payload
    },
    GET_PATIENT_INFO(state, payload) {
      state.patient = payload
    },
    GET_DOCTOR_INFO(state, payload) {
      state.doctor = payload
    },
    SET_TOKEN(state, payload) {
      state.token = payload
      state.isAuthenticated = true
    },
    REMOVE_TOKEN(state, payload) {
      state.token = ''
      state.isAuthenticated = false
    },
    CHECK_TOKEN(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        console.log('Authentication has been set to:', state.isAuthenticated)
      } else {
        state.token = ''
        localStorage.removeItem('isAuthenticated')
        state.isAuthenticated = false
      }
    }

  },
  modules: {
    search
  }
})

export default store
