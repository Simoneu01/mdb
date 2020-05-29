import Vue from 'vue'
import App from './App.vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon, FontAwesomeLayers, FontAwesomeLayersText } from '@fortawesome/vue-fontawesome'
import VueRouter from 'vue-router'
import router from './router'
import Vuex from 'vuex'
import VuexPersist from 'vuex-persist';

Vue.use(Vuex)
Vue.use(VueRouter)
library.add(fas,fab)

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.component('font-awesome-layers', FontAwesomeLayers)
Vue.component('font-awesome-layers-text', FontAwesomeLayersText)

Vue.config.productionTip = false

const vuexLocalStorage = new VuexPersist({
  key: 'vuex', // The key to store the state on in the storage provider.
  storage: window.localStorage, // or window.sessionStorage or localForage
  // Function that passes the state and returns the state with only the objects you want to store.
  // reducer: state => state,
  // Function that passes a mutation and lets you decide if it should update the state in localStorage.
  // filter: mutation => (true)
})

const store = new Vuex.Store({
  state: {
    nome: "NOME NON IMPOSTATO"
  },
  mutations: {
    changeName (state, payload) {
      state.nome = payload
    }
  },
  getters: {
    getName(state) {
      return state.nome;
    }
  },
  plugins: [vuexLocalStorage.plugin]
})

new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')
