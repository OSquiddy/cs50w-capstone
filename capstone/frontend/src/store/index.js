import Vue from 'vue'
import Vuex from 'vuex'
import search from './search'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isMobile: false,
    isCollapsed: false
  },
  actions: {
    toggleCollapse({ commit }) {
      commit('TOGGLE_COLLAPSE')
    }
  },
  mutations: {
    TOGGLE_COLLAPSE(state) {
      state.isCollapsed = !state.isCollapsed
      sessionStorage.setItem('isCollapsed', state.isCollapsed)
    }
  },
  modules: {
    search
  }
})
