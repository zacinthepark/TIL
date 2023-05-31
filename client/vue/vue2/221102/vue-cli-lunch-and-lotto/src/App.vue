<template>
  <div id="app">
    <TheLunch @send-menu-to-app="getMenu"/>
    <hr>
    <TheLotto :selected-menu="selectedMenu"/>
  </div>
</template>

<script>
import TheLunch from '@/components/TheLunch'
import TheLotto from '@/components/TheLotto'

export default {
  name: 'App',
  components: {
    TheLunch,
    TheLotto,
  },
  data: function() {
    return {
      selectedMenu: null,
    }
  },
  methods: {
    getMenu: function(selectedMenu) {
      this.selectedMenu = selectedMenu
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin-top: 20px;
}
</style>
