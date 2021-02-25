import Vue from 'vue'
import Router from 'vue-router'

import App from './App'
import Dashboard from './components/Dashboard'
import Activities from './components/Activities'
import Gallery from './components/Gallery'
import ObservationInput from './components/ObservationInput'

Vue.config.debug = true
Vue.use(Router)

const router = new Router({
  routes: [
    { name: 'Dashboard', path: '/', component: Dashboard },
    { name: 'Activities', path: '/activities', component: Activities },
    { name: 'Gallery', path: '/gallery', component: Gallery },
    { name: 'ObservationInput', path: '/observationInput', component: ObservationInput }
  ]
})

new Vue({
  el: '#app',
  router,
  render (createElement) {
    return createElement(App)
  }
})
