import ambassadorService from '../../services/ambassadorService'

const state = {
  ambassadors: [],
  counter: true
}

const getters = {
  ambassadors: state => {
    return state.ambassadors
  }
}

const actions = {
  getAmbassadors ({ state,  commit }) {
    ambassadorService.fetchAmbassadors()
    .then(ambassadors => {
      ambassadors = state.counter ? ambassadors: ambassadors[0]
      commit('setAmbassadors', ambassadors)
      commit('setCounter')
    })
  },
}

const mutations = {
  setAmbassadors (state, messages) {
    state.ambassadors = messages
  },
  setCounter (state) {
    state.counter = !state.counter
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}