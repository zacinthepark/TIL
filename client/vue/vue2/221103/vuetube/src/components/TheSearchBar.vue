<template>
  <div>
    <input type="text" @keyup.enter="onInputKeyword">
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  methods: {
    onInputKeyword(event) {
      // console.log(event.target.value)
      this.$emit('input-change', event.target.value)
    }
  }
}
</script>

<style>
</style>
