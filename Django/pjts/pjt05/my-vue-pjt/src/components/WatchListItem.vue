<template>
  <div
    :class="{ 'is-completed': list.isCompleted }"
    style="padding: 10px; border: 0.1px black solid"
  >
    <span @click="updateStatus()">
      {{ list.title }}
    </span>
    <button @click="deleteList">삭제</button>
  </div>
</template>

<script>
export default {
  name: "WatchListItem",
  props: {
    list: Object,
  },
  computed: {
    watchlist() {
      return this.$store.state.WatchList
    },
  },
  methods: {
    updateStatus() {
      this.$store.dispatch("updatedWatchList", this.list)
    },
    deleteList() {
      this.$store.dispatch("deleteList", this.list)
    },
  },
}
</script>

<style>
.is-completed {
  text-decoration: line-through;
  background-color: rgb(238, 238, 238);
}
</style>
