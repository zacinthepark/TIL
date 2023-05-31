<template>
  <div class="watchform" style="padding: 35px">
    <h1><label for="title">보고싶은 영화</label></h1>
    <input type="text" id="title" v-model="title" @keyup.enter="addmovie" />
    <button @click="addmovie">add</button>
  </div>
</template>

<script>
export default {
  name: "WatchListForm",
  data() {
    return {
      title: null,
    }
  },
  methods: {
    addmovie() {
      const title = this.title
      if (this.title) {
        this.$store.dispatch("createWatchList", title)
      }
      this.title = null
    },
  },
}
</script>

<style>
.watchform {
  background-color: rgb(228, 242, 253) !important;
}
</style>
