<template>
  <div>
    <h1>Lunch</h1>
    <button @click="pickOneLunchMenu">Pick Lunch</button>
    <p v-if="selectedLunchMenu">{{ selectedLunchMenu }}</p>
    <button v-if="selectedLunchMenu" @click="moveToLotto">
      Lotto 뽑으러가기
    </button>
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: "TheLunch",
  data() {
    return {
      lunch: ["비빔냉면", "국밥", "햄버거", "피자", "파스타", "설렁탕"],
      selectedLunchMenu: null,
    }
  },
  methods: {
    pickOneLunchMenu() {
      const randomIndex = _.random(this.lunch.length - 1)
      this.selectedLunchMenu = this.lunch[randomIndex]
    },
    moveToLotto() {
      this.$router.push({
        name: "TheLotto",
        params: { menu: this.selectedLunchMenu },
      })
    },
  },
}
</script>

<style></style>
