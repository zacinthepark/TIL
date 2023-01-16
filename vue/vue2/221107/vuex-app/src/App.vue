<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <h2>Message Length: {{ messageLength }}</h2>
    <h2>x2 : {{ doubleLength }}</h2>
    <input 
      type="text"
      @keyup.enter="changeMessage"
      v-model="inputData"
    >
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      inputData: null,
    }
  },
  computed: {
    message() {
      return this.$store.state.message
    },
    messageLength() {
      return this.$store.getters.messageLength
    },
    doubleLength() {
      return this.$store.getters.doubleLength
    }
  },
  methods: {
    changeMessage() {
      const newMessage = this.inputData
      // action method 이름, 추가데이터
      this.$store.dispatch('changeMessage', newMessage)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
