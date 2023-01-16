<template>
  <div id="app">
    <h1>Todo List</h1>
    <h2>Total: {{ allTodosCount }}</h2>
    <h2>Completed: {{ completedTodosCount }}</h2>
    <h2>Not Completed: {{ unCompletedTodosCount }}</h2>
    <TodoList/>
    <TodoForm/>
    <br>
    <!-- <button @click="loadTodos">Load Todos</button> -->
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
  computed: {
    allTodosCount() {
      return this.$store.getters.allTodosCount
    },
    completedTodosCount() {
      return this.$store.getters.completedTodosCount
    },
    unCompletedTodosCount() {
      return this.$store.getters.unCompletedTodosCount
    },
  },
  methods: {
    loadTodos() {
      this.$store.dispatch('loadTodos')
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
