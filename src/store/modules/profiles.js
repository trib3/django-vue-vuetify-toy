import profileService from '../../services/profileService'

const state = {
  profiles: [],
  counter: true
}

const getters = {
  profiles: state => {
    return state.profiles
  }
}

const actions = {
  getProfiles ({ state,  commit }) {
    profileService.fetchProfiles()
    .then(profiles => {
      profiles = state.counter ? profiles: profiles[0]
      commit('setProfiles', profiles)
      commit('setCounter')
    })
  },
}

const mutations = {
  setProfiles (state, profiles) {
    state.profiles = profiles
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