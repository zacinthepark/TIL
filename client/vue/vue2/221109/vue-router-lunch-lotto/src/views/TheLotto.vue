<template>
  <div>
    <h1>{{ menu }} 먹고 Lotto 추첨</h1>
    <button @click="getLuckyNumbers">Pick Numbers</button>
    <p v-if="selectedLuckyNumbers">{{ selectedLuckyNumbers }}</p>
    <button v-if="selectedLuckyNumbers" @click="moveToLunch">처음으로</button>
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: "TheLotto",
  data() {
    return {
      menu: this.$route.params.menu,
      selectedLuckyNumbers: null,
    }
  },
  methods: {
    getLuckyNumbers() {
      const numbers = _.range(1, 46)
      this.sampleNumbers = _.sampleSize(numbers, 6)
      this.selectedLuckyNumbers = _.sortBy(this.sampleNumbers)
    },
    moveToLunch() {
      this.$router.push({ name: "TheLunch" })
    },
  },
}
</script>

<style></style>
