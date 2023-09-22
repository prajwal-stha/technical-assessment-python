import { createStore } from 'vuex'

export default createStore({
  state:{
    response:''
  },
  mutations: {
    setResponse(state, res) {
      state.response = res;
    },
  },
  actions: {
      createProfile(context, data){
        return fetch("http://localhost:8000/api/",{
            method:"POST",
            headers: {
                'Content-Type': 'application/json',
              },
            body: JSON.stringify(data),
        })
        .then((response) => {
            if (response.ok) {
                return response.json();
              } else {
                console.log("ERROR")
              }
        })
        .then(() => {
            context.commit("setResponse", "SUCCESS");
        })
        .catch((err) => console.error(err));
    },
      
      
  },
  getters:{
      getResponse(state){
          return state.response
      }
  }
  
})
