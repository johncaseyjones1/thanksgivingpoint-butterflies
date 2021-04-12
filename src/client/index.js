import Vue from 'vue'
import Router from 'vue-router'
import {ClientTable} from 'vue-tables-2'
import VCalendar from 'v-calendar'
import vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

import { BootstrapVue } from 'bootstrap-vue/dist/bootstrap-vue.esm'
import App from './App'
import Dashboard from './components/Dashboard'
import Gallery from './components/Gallery'
import ObservationInput from './components/ObservationInput'
import StaffDashboard from './components/StaffDashboard'
import ButterflyInfo from './components/ButterflyInfo'


import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.debug = true
Vue.use(Router)
Vue.use(BootstrapVue)
Vue.use(ClientTable, {}, false, 'bootstrap4')
Vue.use(VCalendar, {})
Vue.use(vuetify)

const opts = {}

export default new vuetify(opts)

const router = new Router({
  routes: [
    { name: 'Dashboard', path: '/', component: Dashboard },
    { name: 'Gallery', path: '/gallery', component: Gallery },
    { name: 'ObservationInput', path: '/observationInput', component: ObservationInput },
    { name: 'StaffDashboard', path: '/staff/dashboard', component: StaffDashboard },
    { name: 'SpeciesPage', path: '/species/:id', component: ButterflyInfo },
  ]
})


new Vue({
  el: '#app',
  vuetify,
  router,
  render (createElement) {
    return createElement(App)
  }
}).$mount('#app')

