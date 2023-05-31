<template>
  <div v-if="video">
    <br>
    <iframe width="480" height="240" :src="videoUrl"></iframe>
    <hr>
    <h3>{{ video.snippet.title }}</h3>
    <p>{{ video.snippet.description }}</p>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: Object,
    }
  },
  computed: {
    videoUrl() {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>
</style>
