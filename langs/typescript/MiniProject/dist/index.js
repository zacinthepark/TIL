"use strict";
var btn = document.getElementById("btn"); //Type assertion
var input = document.getElementById("todoinput");
var form = document.querySelector("form");
var list = document.getElementById("todolist");
var todos = readTodos();
todos.forEach(createTodo);
// Load todos from local storage
function readTodos() {
    var todosJSON = localStorage.getItem("todos");
    if (todosJSON === null)
        return [];
    return JSON.parse(todosJSON);
}
// Save todos to local storage
function saveTodos() {
    localStorage.setItem("todos", JSON.stringify(todos));
}
function handleSubmit(e) {
    e.preventDefault();
    var newTodo = {
        text: input.value,
        completed: false,
    };
    createTodo(newTodo);
    todos.push(newTodo);
    saveTodos();
    input.value = "";
}
function createTodo(todo) {
    var newLI = document.createElement("li");
    var checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = todo.completed;
    checkbox.addEventListener("change", function () {
        todo.completed = checkbox.checked;
        saveTodos();
    });
    newLI.append(todo.text);
    newLI.append(checkbox);
    list.append(newLI);
}
form.addEventListener("submit", handleSubmit);
