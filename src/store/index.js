import Vue from 'vue'
import Vuex from 'vuex'
import ambassadors from './modules/ambassadors'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    ambassadors
  }
})