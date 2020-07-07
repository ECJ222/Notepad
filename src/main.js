import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Home from './components/Home.vue'
import Notepad from './components/Notepad.vue'
import {store} from './store/index'
import Signup from './components/Signup.vue'
import Login from './components/Login.vue'

Vue.use(VueRouter)
const routes=[
  {
    path:'/',
    component:Home
  }, 
  {
    path:'/notepad',
    component:Notepad

},{
  path:'/signup',
  component: Signup
},{
  path:'/login',
  component:Login
}]

const router= new VueRouter({
  routes:routes,
  mode:'history'
})
new Vue({
  el: '#app',
  router,
  store:store,

  render: h => h(App)
})
