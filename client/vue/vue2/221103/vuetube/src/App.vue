<template>
  <div id="app">
    <h1>VUETUBE!</h1>
    <header>
      <the-search-bar @input-change="onInputChange"></the-search-bar>
    </header>
    <section>
      <video-detail v-if="isGet" :video="selectedVideo"></video-detail>
      <video-list v-if="isGet" :videos="videos" @select-video="onVideoSelect"></video-list>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import TheSearchBar from './components/TheSearchBar.vue'
import VideoDetail from './components/VideoDetail.vue'
import VideoList from './components/VideoList.vue'

const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = 'AIzaSyCI8t8M1ADPjcTTAuIOs3G2w-Nev9hXwRs'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoDetail,
    VideoList,
  },
  data: function() {
    return {
      inputValue: null,
      videos: [],
      selectedVideo: null,
      isGet: false,
    }
  },
  methods: {
    onInputChange(inputValue) {
      // console.log(inputValue)
      this.inputValue = inputValue
      this.isGet = true

      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue
      }

      axios({
        method: 'get',
        url: API_URL,
        // params: params에 대한 JS 축약 문법
        params
      })
        .then((res) => {
          console.log(res)
          this.videos = res.data.items

        })
        .catch((err) => {
          console.log(err)
        })
    },
    onVideoSelect(video) {
      this.selectedVideo = video
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 50px;
}
</style>
