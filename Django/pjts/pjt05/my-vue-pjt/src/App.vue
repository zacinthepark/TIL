<template>
  <div id="app">
    <div class="navbar">
      <img
        src="https://cdn-icons-png.flaticon.com/512/8274/8274697.png"
        class="d-inline-block align-top"
        style="margin-left: 10px; width: 35px"
      />
      <nav>
        <router-link class="navbar-item" :to="{ name: 'movies' }"
          >Movie</router-link
        >
        <router-link class="navbar-item" :to="{ name: 'random' }"
          >Random</router-link
        >
        <router-link class="navbar-item" :to="{ name: 'watchList' }"
          >WatchList</router-link
        >
      </nav>
    </div>
    <br />
    <router-view />
  </div>
</template>

<script>
export default {
  created() {
    this.$router.push({ name: "movies" }).catch(() => {})
    this.$store.dispatch('loadCurrentWeather')
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.navbar {
  display: flex;
  background-color: rgb(228, 242, 253) !important;
}

.navbar-item {
  margin: 15px;
  text-decoration: none;
}

nav {
  padding: 10px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
