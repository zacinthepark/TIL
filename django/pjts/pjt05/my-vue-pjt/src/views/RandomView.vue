<template>
  <div>
    <h2>오늘의 날씨는 {{ currentWeather }}! 이런 영화 어때요?</h2>
    <div style="width: 50%; width: 315px; margin: auto">
      <button
        class="btn btn-success"
        @click="pickMovie"
        style="display: block; width: 315px"
      >
        PICK
      </button>
      <div class="card h-200" v-if="isSelected">
        <img
          :src="`https://image.tmdb.org/t/p/original${this.movie.poster_path}`"
          class="card-img-top"
        />
        <div class="card-body">
          <h5 class="text-center" style="font-weight: bold; margin: 0px">
            {{ movie.title }}
          </h5>
        </div>
      </div>
    </div>
    <img src="" alt="" />
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: "RandomView",
  data() {
    return {
      movie: null,
      isSelected: false,
    }
  },
  methods: {
    pickMovie() {
      this.isSelected = true
      const rand_idx = _.random(0, 19)
      const selectedMovie = this.$store.state.movieCards[rand_idx]
      this.movie = selectedMovie
    },
  },
  computed: {
    currentWeather() {
      return this.$store.state.currentWeather
    }
  },
}
</script>

<style></style>
