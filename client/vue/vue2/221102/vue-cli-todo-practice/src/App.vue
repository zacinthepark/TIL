<template>
  <div id="app">
    <TodoList :todos="todos" @delete-todo="deleteTodo"/>
    <TodoForm @create-todo="createTodo"/>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data: function() {
    return {
      todos: [],
    }
  },
  methods: {
    createTodo: function(todoTitle) {
      const todo = {
        title: todoTitle
      }
      // 한글 입력기일 시 공백인 todo가 자동 추가되는 것을 방지
      if (todo.title) {
        this.todos.push(todo)
      }
    },
    deleteTodo: function(todo) {
      const index = this.todos.indexOf(todo)
      // 해당 인덱스의 요소 하나 빼주고 새로운 todos 만들어주는 것
      this.todos.splice(index, 1)
    }
  }
}
</script>

<style>
</style>
