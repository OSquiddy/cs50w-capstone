const getDefaultSearchState = () => {
  return {
    searchKeyword: null
  }
}

export default {
  namespaced: true,
  state: getDefaultSearchState(),
  actions: {
    resetState({ commit }, value) {
      commit('RESET_SEARCH_STATE')
    },
    updateSearchKeyWord ({
      commit
    }, payload) {
      commit('UPDATE_SEARCH_KEYWORD', payload)
    }
  },
  mutations: {
    RESET_SEARCH_STATE(state, payload) {
      state = {}
    },
    UPDATE_SEARCH_KEYWORD (state, payload) {
      state.searchKeyword = payload
    }
  }
}
