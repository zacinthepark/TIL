<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" @input="onAppInput">
    <!-- <p>appData: {{appInputData}}</p> -->
    <p>parentData: {{ parentInputData }}</p>
    <p>childData: {{ childInputData }}</p>
    <app-parent :app-input-data="appInputData" @on-parent-input="getParentInput" @on-child-input="getChildInput"></app-parent>
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  components: {
    AppParent,
  },
  data: function() {
    return {
      appInputData: null,
      parentInputData: null,
      childInputData: null,
    }
  },
  methods: {
    onAppInput(event) {
      this.appInputData = event.target.value
    },
    getParentInput(parentInputData) {
      this.parentInputData = parentInputData
    },
    getChildInput(childInputData) {
      this.childInputData = childInputData
    },
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
