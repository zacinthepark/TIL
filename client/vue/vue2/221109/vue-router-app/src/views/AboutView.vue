<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{ name: 'home' }">To HOME!</router-link> |
    <button @click="toHome">To HOME!</button>
    <input type="text" @keyup.enter="goToHello" v-model="inputData" />
  </div>
</template>

<script>
export default {
  name: "AboutView",
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    toHome() {
      this.$router.push({ name: "home" })
    },
    goToHello() {
      this.$router.push({ name: "hello", params: { userName: this.inputData } })
      // this.$router.push({ path: `hello/${this.inputData}` })
    },
  },
}
</script>
