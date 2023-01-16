import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store',
  },
  getters: {
    messageLength(state) {
      return state.message.length
    },
    // messageLength를 이용해서 새로운 값 계산 가능
    doubleLength(state, getters) {
      return getters.messageLength*2
    },
  },
  mutations: {
    CHANGE_MESSAGE(state, newMessage) {
      // console.log(state)
      // console.log(newMessage)
      state.message = newMessage
    }
  },
  actions: {
    // action이 vuex 모든 곳에 접근할 수 있는 이유는 context를 인자로 받기 때문
    changeMessage(context, newMessage) {
      // console.log(context)
      // console.log(newMessage)
      // mutation method 이름, 추가데이터
      context.commit('CHANGE_MESSAGE', newMessage)
    }
  },
  modules: {
  }
})
