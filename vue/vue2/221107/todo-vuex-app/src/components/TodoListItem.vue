<template>
  <div>
    <span 
      @click="updateTodoStatus"
      :class="{ 'is-completed': todo.isCompleted }"
    >
      {{ todo.title }}
    </span>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo() {
      this.$store.dispatch('deleteTodo', this.todo)
      // actions가 사실상 해주는 것이 없기에 actions를 거치지 않고 아래와 같이 바로 mutations를 호출하는 것도 괜찮음
      // this.$store.commit('DELETE_TODO', this.todo)
    },
    updateTodoStatus() {
      this.$store.dispatch('updateTodoStatus', this.todo)
    },
  }
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>
