import Vue from 'vue'
import Router from 'vue-router'

import App from './App'
import Hello from './components/Hello'
import Goodbye from './components/Goodbye'

Vue.config.debug = true
Vue.use(Router)

const router = new Router({
  routes: [
    { name: 'hello', path: '/hello', component: Hello },
    { name: 'goodbye', path: '/goodbye', component: Goodbye }
  ]
})

new Vue({
  el: '#app',
  router,
  render (createElement) {
    return createElement(App)
  }
})
