<template>
  <div class="videoList">
    <ul>
      <video-list-item 
        v-for="video in videos"
        :key="video.id.videoId"
        :video="video"
        @select-video="onSelectVideo"
      >
      </video-list-item>
    </ul>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
      required: true,
    }
  },
  methods: {
    onSelectVideo(video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>
  .videoList {
      margin: 20px auto;
      border: 2px solid black;
    }
</style>
