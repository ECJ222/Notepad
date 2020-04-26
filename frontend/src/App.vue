<template>
  <div id="app">
 <transition name="fade">
  <router-view></router-view>
 </transition>
  </div>
</template>

<script>
import Home from './components/Home.vue'
import Notepad from './components/Notepad.vue'
import Signup from './components/Signup.vue'
import Login from './components/Login.vue'
export default {
  name: 'app',
  components:{
    Home,
    Notepad, 
    Login,
    Signup
  },
  
}
</script>

<style lang="scss">


#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.navbar{
  margin:auto;
  top:-45px;
}
body {
  background: #007bff;
  background: linear-gradient(to right, #0062E6, #33AEFF);
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .3s ease-out;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

/*
.fadeInUp{
  -webkit-animation-name:fadeInUp;
  animation-name:fadeInUp;
  
}

@-webkit-keyframes fadeInUp{
  0%{
    opacity:0;
    -webkit-transform:translate3d(0,100%,0);
    transform:translate3d(0,100%,0);
   }
  to{
  opacity:1;
  -webkit-transform:translateZ(0);
  transform:translateZ(0);
  }
}
@keyframes fadeInUp{
  0%{
    opacity:0;
    -webkit-transform:translate3d(0,100%,0);
    transform:translate3d(0,100%,0);
  }
  to{
    opacity:1;
    -webkit-transform:translateZ(0);
    transform:translateZ(0);
  }
}
*/
</style>
