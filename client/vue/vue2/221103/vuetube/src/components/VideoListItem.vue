<template>
  <div style="display: flex">
    <li @click="selectVideo">
      <img 
        :src="video.snippet.thumbnails.default.url" 
        alt="youtube thumbnail"
      >
      <span>{{video.snippet.title}}</span>
    </li>
  </div>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
      required: true,
    }
  },
  methods: {
    selectVideo() {
      this.$emit('select-video', this.video)
    }
  }
}
</script>

<style>
</style>
