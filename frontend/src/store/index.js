import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state:{
        notepad:[{
            id:1,
            title:'Get More HashTags',
            editing:false
        }]

    }
})