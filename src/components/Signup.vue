<template>
  <div class="signup page">
    <form id="formvideo" @submit.prevent="Createuser">
    <div class="signupbody">
        <img class="image" src="notepad.ico">
        <input class="Firstname" type="text" placeholder="Firstname"><br>
        <input class="Lastname" type="text" placeholder="Lastname"><br>
        <input class="Username" type="text" placeholder="Username" v-model="Username"><br>
        <input class="Password" type="password" placeholder="Password" v-model="Password"><br>
        <input class="Lastname" type="password" placeholder="Confirm Password"><br>
        <div v-if="check" class="error">
          <span class="alert" ><strong>Empty</strong> Fields</span>
        </div>
        <div v-if="!loader">
            <button type="submit" class="btn btn-success ">Register</button>
        </div>
        <div v-else class="loader1">
                   <button class="btn btn-success" id="load">
                       <span></span>
                       <span></span>
                       <span></span>
                       <span></span>
                       <span></span></button>
        </div>
        <br>
       <router-link to="/login"><span class="logintag">Already have an account?</span></router-link>
        
        
    </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    name:'Signup',
    data:function() {
        return{
            Username:null,
            Password:null,
            loader:false,
            check:false

        }
    },
    methods: {
        Createuser:function(){
            axios.post('https://stickynotepad.herokuapp.com/api/user/',{
                username: this.Username,
                password: this.Password
            }).then(res => {
              console.log(res)
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
                if(this.Username==null || this.Password==null){
                    this.check=true
                  }else{
                    this.check=false
                  }
              },4000)
            })
            
        }
    }
    
}
</script>

<style lang="scss">
.signupbody{
    background:#98f3ff;
    border:5px solid #98f3ff;
    width:510px;
    height: 470px;
    position: absolute;
    left:410px;
    top:155px;
    -moz-box-shadow:5px 5px 7px rgba(33,33,33,1);
   /* Safari+Chrome */
    -webkit-box-shadow: 5px 5px 7px rgba(33,33,33,.7);
    box-shadow: 5px 5px 7px rgba(33,33,33,.7);
}


input[type=text]{
   top:35px;
   border:none;
   margin:5px;
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
   margin:5px;
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
.btn-success{
    position:relative;
    top:40px;
    width:72px;
    height:30px;
    left:-10px;
    font-size:15px;
}
.logintag{
    position:relative;
    top:50px;
    color:black;
}
#load{
    position:relative;
    top:40px;
    width:72px;
    height:30px;
    left:-10px;
    font-size:15px;

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
.error{
  position:relative;
  margin:1px;
  top:33px;
  transform:scale(1.5,1);
  color:white;
  font-size:15px;
  width:200px;
  background-color: #33AEFF;
  left:140px;
  border-radius:5px;
}
</style>