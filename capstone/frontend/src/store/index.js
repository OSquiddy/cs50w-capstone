import Vue from 'vue'
import Vuex from 'vuex'
import search from './search'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isMobile: false,
    isCollapsed: false,
    selectedTab: 0
  },
  actions: {
    toggleCollapse({ commit }) {
      commit('TOGGLE_COLLAPSE')
    },
    updateSelectedTab({ commit }, value) {
      commit('UPDATE_SELECTED_TAB', value)
    }
  },
  mutations: {
    TOGGLE_COLLAPSE(state) {
      state.isCollapsed = !state.isCollapsed
      sessionStorage.setItem('isCollapsed', state.isCollapsed)
    },
    UPDATE_SELECTED_TAB(state, payload) {
      state.selectedTab = payload
      sessionStorage.setItem('selectedTab', payload)
    }
  },
  modules: {
    search
  }
})
