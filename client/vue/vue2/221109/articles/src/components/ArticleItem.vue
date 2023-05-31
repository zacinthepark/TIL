<template>
  <!-- @click="goDetail" -->
  <div @click="goDetail(article.id)">
    <p>Number: {{ article.id }}</p>
    <p>Title: {{ article.title }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  },
  methods: {
    // goDetail() {
    //   this.$router.push({ name: 'detail', params: {id: `${this.article.id}` }})
    // },
    goDetail(id) {
      this.$router.push({ name: 'detail', params: {id} })
    }
  }
}
</script>

<style>
</style>
