<template>
  <div>
    <div class="col">
      <div class="card h-100 m-3">
        <img :src="posterPath" class="card-img-top" alt="" />
        <div class="card-body">
          <h5 class="text-center" style="font-weight: bold">
            {{ movieCard.title }}
          </h5>
          <div class="card-text">{{ movieCard.overview }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movieCard: Object,
  },
  computed: {
    posterPath() {
      return "https://image.tmdb.org/t/p/w500" + this.movieCard.poster_path
    },
  },
}
</script>

<style>
.card {
  max-width: 100%;
}
.card-text {
  width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  text-align: justify;
  text-indent: 7px;
  line-height: 2rem;
}
.card-img-top {
  width: 100%;
  height: 30rem;
  object-fit: cover;
}
</style>
