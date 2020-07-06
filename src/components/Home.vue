<template>
  <div class="home page">
   <nav class="navbar">
     <div class="container mt-5">
       <div class="dropdown"> 
            <a class="bars" type="button" id="dropdownMenu2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i @click="xTrue" v-bind:class="{'fa fa-bars': !x}"></i></a>
                      <a class="bars" type="button" id="dropdownMenu2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i @click="xFalse" v-bind:class="{'fa fa-close':!y}"></i></a>
         <!--Menu-->
         <div class="dropdown-menu dropdown-primary">
           <div v-if="token==null">
           <router-link to="/" ><a class="dropdown-item"><i class="fa fa-home"></i>&nbsp;&nbsp;Home</a></router-link>
           <div class="dropdown-divider"></div>
          
            <router-link to="/signup" ><a class="dropdown-item"><i class="fa fa-user-plus"></i>&nbsp;&nbsp;SignUp</a></router-link>
            <router-link to="/login" ><a class="dropdown-item"><i class="fa fa-sign-in"></i>&nbsp;&nbsp;Login</a></router-link>
           </div>
           <div v-else>
               <router-link to="/"><a class="dropdown-item"  @click="Logout"><i class="fa fa-sign-out"></i>&nbsp;&nbsp;Logout</a> </router-link>
            </div>
           
         </div>
       </div>
     </div>
   </nav>
   <div v-if="token != null">
   <div class="card text-center" v-for="(note,index) in notes" v-bind:key="note.id" @dblclick="Update(note)" v-if="note.user == username">
    

     <div class="card-body" v-if="note.editing==false">
       
       
        <div v-if="note.title.length > 6">
         <h1>{{note.title.substring(0,10)+'...'}}</h1>
        </div>
        <h1 v-else>{{note.title}}</h1>
       
        <a class="btn btn-danger" @click="remove(note,index)"><i class="fa fa-trash-o"></i></a>
       
     </div>
     <div v-else><textarea v-model="note.title" @keyup.enter="edit(note)" @keyup.esc="escape(note)" style="position:relative; left:-10px; top:-10px; width:149px; height:15em;font-family:Georgia, 'Times New Roman', Times, serif;
  font-weight:bold;"></textarea></div>
    
   </div>
  </div>
  <div v-if=" token!=null ">
   <div class="HoverOverme">
    <router-link to="/notepad"><i class="fa fa-plus-circle"></i></router-link> 
    <span class="AddNote">New Note</span>
   </div>
  </div>
  <div v-if=" token ==null ">
   <div class="HoverOverme">
    <router-link to="/login"><i class="fa fa-plus-circle"></i></router-link> 
    <span class="AddNote">New Note</span>
   </div>
  </div>
  <input type="file" ref="file" name="imagefile" style="display:none" @change="filestore">
  <form id="uploadimage" method="post" name="uploadimage" enctype="multipart/form-data" @submit.prevent="chooseimage(note)">
  
    <div v-for="(note,index) in images" v-bind:key="note.id" >
        <div v-if="token==null">
          <img @click="Uploadpicture" class="userimage" src="user1.png">
        </div>
         <img v-else @click="Uploadpicture" class="userimage" src="user1.png">
      
      <div v-if="token!=null">
       <div  v-if="note.user == username ">
     `   <img @click="Uploadpicture" class="userimage" v-bind:src="note.image">
       </div>
      </div>
    
    </div>
    
  <div v-for="(note,index) in user" v-bind:key="note.id"  v-if="note.username == username">
     
   
   <!--choose picture-->
    
  
    <div class="upload" v-if="!img ">
      <div v-if="selected_image==null">
        <div v-if="token==null">
        <router-link to="/login"><button class="btn btn-primary " id="upload">Upload</button></router-link>
        </div>
        <button v-else class="btn btn-primary " id="upload" @click="choosefile">Upload</button>
      </div>
      <div v-if="selected_image!=null && loader==false ">
       <button class="btn btn-primary" id="save" @click="!chooseimage(note)" >Save</button>
      </div>
      <div v-else-if="selected_image!=null && loader==true" class="loader1">
      <button class="btn btn-primary" id="loadL">
       <span></span>
       <span></span>
       <span></span>
       <span></span>
       <span></span></button>
      </div>
     
    </div>
  

  </div>
  </form>


  </div>

 
  
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Home',
  components:{
    
    
  },
  props:{
    loading:{
      type:Boolean,
      default:true
    },
    color: { 
      type: String,
      default: 'white'
    },
    size: {
      type: String,
      default: '20px'
    },
    radius: {
      type: String,
      default: '100%'
    }
  },
  data:function(){
    return{
      x:false,
      y:true,
      note:'',
      beforenote:'',
      img:true,
      count:1,
      token:localStorage.getItem('user-token') || null,
      username:localStorage.getItem('username'),
      notes:[axios.get("http://127.0.0.1:8000/api/note/").then(res => console.log(this.notes=res.data)).catch(err => console.log(err))],
      images:[axios.get("http://127.0.0.1:8000/api/image/").then(res => console.log(this.images=res.data)).catch(err => console.log(err))],
      selected_image:null,
      getimage:localStorage.getItem('image') || null,
      loader:false,
      imageshow:false,
      user : [axios.get("http://127.0.0.1:8000/api/user/").then(res => console.log(this.user=res.data)).catch(err => console.log(err))]
      
    
    };
  },
  methods: {
    xTrue:function(){
      this.x=true;
      this.y=false;
      console.log(this.token)
    },
    Logout:function(){
        this.token = null;
        localStorage.removeItem('user-token');
        this.$router.push('/');
    },
    xFalse:function(){
      this.x= false;
      this.y=true;
  
  },remove:function(note,index){
    axios.delete("http://127.0.0.1:8000/api/note/"+note.id).then(res=>{
      this.notes.splice(index,1)
      console.log(this.notes)
    })
    
  },
    Update:function(note){
     note.editing=true;
     this.beforenote=note.title
     axios.put("http://127.0.0.1:8000/api/note/"+note.id+"/",{
      title:note.title,
      username:note.username,
      editing:false
     }).then(res=> console.log(res)).catch(err => console.log(err))
    },
    edit:function(note){
      note.editing=false;
      axios.put("http://127.0.0.1:8000/api/note/"+note.id+"/",{
      title:note.title,
      username:note.username,
      editing:false
     }).then(res=> console.log(res)).catch(err => console.log(err))
    },
    Uploadpicture:function(){
      if (this.count % 2 == 1){
           this.img=false;
      }else if( this.count % 2 == 0){
           this.img=true;
      }
      this.count+=1;
     
    },
    escape:function(note){
      note.editing=false;
      axios.put("http://127.0.0.1:8000/api/note/"+note.id+"/",{
      title:this.beforenote,
      username:note.username,
      editing:false
     }).then(res=> console.log(res)).catch(err => console.log(err))

    },
    choosefile:function(){
      this.$refs.file.click()
      console.log(this.$refs.file.click())
    },
    filestore:function(event){
      console.log(event.target.files[0]);
      this.selected_image=event.target.files[0]
    },
    chooseimage:function(note){
      const config = { headers :{'Content-Type' : 'multipart/form-data'}}
      const data= new FormData(document.getElementById('uploadimage'))
      data.append('image',this.selected_image)
      data.append('username',note.id)
      data.append('show',true)
      axios.post("http://127.0.0.1:8000/api/image/",data,config).then(res =>{ 
        console.log(res.data,' <<< res.data >>> ')
        localStorage.setItem('image',res.data)
        this.loader=true
        
        setTimeout( () => {
          window.location.reload();

        },3000)
        
    }).catch(err => console.log(err))
      setTimeout( () => {
          this.loader=false
          this.imageshow=true
          console.log("2000")

        },12000)
    }
  },
 
 
}
</script>

<style lang="scss">


.navbar{
  margin:auto;
  top:-45px;
}
.dropdown{
  margin: auto;
  left:-620px;
  top:-15px;

}
.fa-bars{
  transform:scale(3,2.5);
}

.fa-plus-circle{
    transform:scale(6,5.5);
    color: white;
    position: fixed;
    left: 1250px;
    top:610px;

}
.fa-close{
  transform:scale(3,2.5);
}

.HoverOverme .AddNote{
  visibility:hidden;
  background-color:rgb(128, 128, 128);
  position: absolute;
  z-index: 1;
  top: 575px;
  left:1229px;
  border-radius: 10px;
  text-align: center;
  color: white;
  width:50px;
  font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
 
}
.HoverOverme:hover .AddNote{
  visibility: visible;
}
.card{
   text-decoration:none;
   color:#000;
   background:#7aefff;
   display:block;
   height:15em;
   width:15em;
   padding:1em;
   -moz-box-shadow:5px 5px 7px rgba(33,33,33,1);
   /* Safari+Chrome */
   -webkit-box-shadow: 5px 5px 7px rgba(33,33,33,.7);
   box-shadow: 5px 5px 7px rgba(33,33,33,.7);
   transition:-moz-transform .15s linear;
   -o-transition:-o-transform .15s linear;
   -webkit-transition:-webkit-transform .15s linear;
   margin:1em;
   float:left;
   transform:rotate(-3deg);
   -webkit-transform:rotate(-3deg);
   -moz-transform:rotate(-3deg); 
   top:30px;
   left:15px;
}
.card:nth-child(even){
  transform:rotate(4deg);
  -webkit-transform:rotate(4deg);
  -moz-transform:rotate(4deg);
}
.card:hover, .card:focus{ 
  -moz-box-shadow:10px 10px 7px rgba(0,0,0,.7);
  -webkit-box-shadow: 10px 10px 7px rgba(0,0,0,.7);
   box-shadow:10px 10px 7px rgba(0,0,0,.7);
  -webkit-transform: scale(1.25);
  -moz-transform: scale(1.25);
   transform: scale(1.25);
   position:relative;
   z-index:5;
    
}
h1{
  font-family:Georgia, 'Times New Roman', Times, serif;
  font-weight:bold;
  color:white;
}
h1:hover{
  color:#000;
}
.btn-danger{
  position: absolute;
  top: 120px;
  margin-right: 30px;
  z-index: 1;
  left:61px;
 
}
.btn-danger:hover{
  visibility:visible;
}
.userimage{
  border:1px solid;
  border-radius: 50%;
  width:35px;
  height: 35px;
  position:absolute;
  top:28px;
  left:1240px;
}
.upload{

  border-radius:7px;
  width:70px;
  height:50px;
  left:1222px;
  top:65px;
  position:absolute;
}
.btn-primary{
  left:10px;
  border-radius:10px;
  transform:scale(1.5,1.5);
  top:10px;
  position:absolute;
  background-color:linear-gradient(to right, #0062E6, #33AEFF);
}
#save{
  left:15px;
  position:absolute;
  transform:scale(1.5,1.5);
  border-radius:10px;


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
#loadL{
  left:15px;
}
#changeImage{
  font-size:9px;
  transform:scale(1.2,1.2);
  
}
</style>
