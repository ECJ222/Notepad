<template>
  <div class="Notepad page">
      <router-link to="/"><i class="fa fa-arrow-circle-left"></i></router-link>
      <textarea class="textbox" type="text" placeholder="Type Here..." v-model="note"></textarea>
      <br>
    
         <div v-for="users in user" v-bind:key="users.id">
             <div v-if="users.username == username">
                <div v-if="loader==false">
                    <button @click="send(users)" @submit.prevent="send" type="submit" class="bcolor">Save</button>
                </div>

                 <div v-if="loader==true" class="loader1">
                   <button id="loaded">
                       <span></span>
                       <span></span>
                       <span></span>
                       <span></span>
                       <span></span></button>
                 </div>
             </div>

         </div>
       
  
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'app',
  components:{
    
  },
  data:function(){
    return{
      note:'',
      id:2,
      username:localStorage.getItem('username'),
      user:[axios.get("http://127.0.0.1:8000/api/user/").then(res => console.log(this.user=res.data)).catch(err => console.log(err))],
      loader:false
    };
  },
  methods: {
    Home:function(){
      this.$router.push('/')
    },
    send:function(users){
      axios.post("http://127.0.0.1:8000/api/note/",{
        title: this.note,
        username: users.id
      }).then(res => {
        console.log(res)
        this.loader=true
        setTimeout(()=>{
          this.loader=false
        },4000)
      }).catch(err => {
          console.log(err)
          this.loader=true
          setTimeout(()=>{
             this.loader=false
          },4000)
        })
      this.note=''
    }
   
  
  }
  
}
</script>

<style lang="scss">


.textbox{
    width: 1200px;
    height: 500px;
    font-size: 40px;
    font-family: 'Times New Roman', Times, serif;
}
.bcolor{
    border-radius: 20px;
    font-size: 20px;
    width: 100px;
    height: 50px;
    color:white;
    background: #007bff;
    background: linear-gradient(to right, #0062E6, #33AEFF);
    border-top-color:#007bff;
    border-left-color: #007bff;
    border-right-color: #007bff;
    border-bottom-color: #007bff;
}
.fa-arrow-circle-left{
  transform:scale(4,3.5);
  position: fixed;
  top: 30px;
  left:65px;
  color: white;
} 
.strong{
  font-size:400px;
}
#loaded{
    border-radius: 20px;
    font-size: 20px;
    width: 100px;
    height: 50px;
    color:white;
    background: #007bff;
    background: linear-gradient(to right, #0062E6, #33AEFF);
    border-top-color:#007bff;
    border-left-color: #007bff;
    border-right-color: #007bff;
    border-bottom-color: #007bff;
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
