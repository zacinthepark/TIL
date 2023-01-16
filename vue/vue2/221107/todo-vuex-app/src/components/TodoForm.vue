<template>
  <input 
    type="text"
    v-model.trim="todoTitle"
    @keyup.enter="createTodo"
  >
</template>

<script>
export default {
  name: 'TodoForm',
  data() {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo() {
      // console.log(this.todoTitle)
      if (this.todoTitle) {
        this.$store.dispatch('createTodo', this.todoTitle)
      }
      this.todoTitle = null
    },
  }
}
</script>

<style>
</style>
