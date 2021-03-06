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
    currentUser: {},
    overviewMenu: false
  },
  actions: {
    toggleCollapse({ commit }) {
      commit('TOGGLE_COLLAPSE')
    },
    async getPatientInfo({ commit }, patientID) {
      const response = await axios.get(process.env.VUE_APP_API_URL + '/p/' + patientID)
      const value = response.data.patientInfo
      commit('GET_PATIENT_INFO', value)
      return response
    },
    async getDoctorInfo({ commit }, doctorID) {
      const response = await axios.get(process.env.VUE_APP_API_URL + '/d/' + doctorID)
      const value = response.data.doctorInfo
      commit('GET_DOCTOR_INFO', value)
    },
    setCurrentUser({ commit }, value) {
      commit('SET_CURRENT_USER', value)
    },
    clearUserSelection({ commit }, value) {
      commit('CLEAR_USER', value)
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
    },
    toggleOverviewMenu({ commit }) {
      commit('TOGGLE_OVERVIEW_MENU')
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
      localStorage.setItem('currentUser', JSON.stringify(payload))
      state.currentUser = payload
    },
    GET_PATIENT_INFO(state, payload) {
      sessionStorage.setItem('patient', JSON.stringify(payload))
      state.patient = payload
    },
    GET_DOCTOR_INFO(state, payload) {
      sessionStorage.setItem('doctor', JSON.stringify(payload))
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
    },
    CLEAR_USER(state, payload) {
      state[payload] = {}
    },
    TOGGLE_OVERVIEW_MENU(state) {
      state.overviewMenu = !state.overviewMenu
    }

  },
  modules: {
    search
  }
})

export default store
