<template>
  <li>
    {{ todo.title }}
    <button @click="deleteTodo">DELETE</button>
  </li>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo: function() {
      this.$emit('delete-todo', this.todo)  // 현재 반복문에서 눌린 todo를 같이 넘겨줘야 함
    }
  }
}
</script>

<style>
</style>
