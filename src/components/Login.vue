<template>
  <div class="login page">
    <div class="signupbody">
        <img class="image" src="notepad.ico">
        <input class="Username" v-model="Username" type="text" placeholder="Username"><br>
        <input class="Password" v-model="Password" type="password" placeholder="Password"><br>
        <div v-if="check==false" class="message">
          <span class="alert" ><strong>Invalid</strong> Username and Password</span>
        </div>
        <form @submit.prevent="Login">
        <div v-if="loader==false">
          <button type="submit" class="btn btn-success " id="login" @click="!check">Login</button>
        </div>
        <div v-if="loader==true" class="loader1">
             <button class="btn btn-success" id="loader">
             <span></span>
             <span></span>
             <span></span>
             <span></span>
             <span></span></button>
        </div>
   
  
        </form>
        <br>
       <router-link to="/signup"><span class="logintag">need an account?</span></router-link>
        
        
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import TokenService from '../storage/service'
export default {
    name:'Login',
    data:function(){
        return{
            Username:'',
            Password:'',
            check:true,
            token:localStorage.getItem('user-token') || null,
            loader:false
        }
            
    },
    methods: {
        Login:function(){
            axios.post("https://stickynotepad.herokuapp.com/api-token-auth/",{
                username: this.Username,
                password: this.Password
            }).then(res => { 
                this.token=res.data.token;
                console.log(this.token)
                localStorage.setItem('user-token', res.data.token)
                localStorage.setItem('username',this.Username)
                this.loader=true
                setTimeout(()=>{
                  this.loader=false
                  this.$router.push('/')
                },4000)

                
                }).catch(err => {
                console.log(err)
                this.loader=true
                setTimeout(()=>{
                  this.loader=false
                  this.check=false
                  localStorage.removeItem('user-token')
                },4000)
                 
               
                })
               

        }
    },
    created() {
        this.token = TokenService.getToken() || null;
        console.log(TokenService.getToken())
    }
}
</script>

<style lang="scss">
.signupbody{
    background:#98f3ff;
    border:5px solid #98f3ff;
    width:510px;
    height: 360px;
    position: absolute;
    left:395px;
    top:155px;
    -moz-box-shadow:5px 5px 7px rgba(33,33,33,1);
   /* Safari+Chrome */
    -webkit-box-shadow: 5px 5px 7px rgba(33,33,33,.7);
    box-shadow: 5px 5px 7px rgba(33,33,33,.7);
}


input[type=text]{
   top:35px;
   border:none;
   margin:10px;
   background-color:#98f3ff;
   border-bottom:1px solid grey;
   font-size: 20px;
   width: 480px;
   position: relative;
   left:-11px;

}

input[type=password]{
   top:35px;
   border:none;
   margin:10px;
   background-color:#98f3ff;
   border-bottom:1px solid grey;
   font-size: 20px;
   width: 480px;
   position: relative;
   left:-11px;

}

.image{
    width:35px;
    height:35px;
    position:relative;
    left:-13px;
    
}
#login{
    position:relative;
    top:40px;
    width:72px;
    height:30px;
    left:-10px;
    font-size:15px;
}
#loader{
    position:relative;
    top:40px;
    width:72px;
    height:30px;
    left:-8px;
    font-size:15px;
}
.logintag{
    position:relative;
    top:50px;
    color:black;
    left:-8px;
}
.alert{
  color:white;
  font-size:15px;
  position:relative;
  width:200px;
  background-color: #33AEFF;

  
}
.message{
  position:relative;
  margin:1px;
  top:33px;
  transform:scale(1.5,1);
 

}

.loader1 {
   display:inline-block;
   font-size:0px;
   padding:0px;
   
}
.loader1 span {
   vertical-align:middle;
   border-radius:100%;
   
   display:inline-block;
   width:2px;
   height:2px;
   margin:3px 0.1px;
   -webkit-animation:loader1 0.8s linear infinite alternate;
   animation:loader1 0.8s linear infinite alternate;
}
.loader1 span:nth-child(1) {
   -webkit-animation-delay:-1s;
   animation-delay:-1s;
  background:white;
}
.loader1 span:nth-child(2) {
   -webkit-animation-delay:-0.8s;
   animation-delay:-0.8s;
  background:white;
}
.loader1 span:nth-child(3) {
   -webkit-animation-delay:-0.26666s;
   animation-delay:-0.26666s;
  background:white;
}
.loader1 span:nth-child(4) {
   -webkit-animation-delay:-0.8s;
   animation-delay:-0.8s;
  background:white;
  
}
.loader1 span:nth-child(5) {
   -webkit-animation-delay:-1s;
   animation-delay:-1s;
  background:white;
}

@keyframes loader1 {
   from {transform: scale(0, 0);}
   to {transform: scale(1, 1);}
}
@-webkit-keyframes loader1 {
   from {-webkit-transform: scale(0, 0);}
   to {-webkit-transform: scale(1, 1);}
}
</style>