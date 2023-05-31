<template>
  <div v-if="selectedMenu">
    <h2>{{ selectedMenu }} 먹고 로또</h2>
    <button @click="getLuckyNumbers">Get Lucky Numbers</button>
    <p>{{ selectedNumbers }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'TheLotto',
  data: function() {
    return {
      selectedNumbers: null,
    }
  },
  methods: {
    getLuckyNumbers: function() {
      const numbers = _.range(1, 45)
      this.selectedNumbers = _.sampleSize(numbers, 6)
    }
  },
  props: {
    selectedMenu: String,
  }
}
</script>

<style>
</style>
