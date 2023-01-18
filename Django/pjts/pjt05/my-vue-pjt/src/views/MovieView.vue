<template>
  <div>
    <h1>MovieView</h1>
    <div class="py-5">
      <div class="c">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4">
          <MovieCard
            v-for="movieCard in movieCards"
            :key="movieCard.id"
            :movieCard="movieCard"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCard from "@/components/MovieCard"

export default {
  name: "MovieView",
  components: {
    MovieCard,
  },
  computed: {
    movieCards() {
      return this.$store.state.movieCards
    },
  },
  created: function () {
    this.$store.dispatch("loadMovieCards")
  },
}
</script>

<style>
.c {
  margin-left: 20px;
  margin-right: 20px;
  text-align: center;
}
</style>
