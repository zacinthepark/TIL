<template>
  <div>
    <h1>AppChild</h1>
    <input type="text" @input="onChildInput">
    <p>appData: {{ appInputData }}</p>
    <p>parentData {{ parentInputData }}</p>
    <p>childData: {{ childInputData }}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  props: {
    appInputData: String,
    parentInputData: String,
  },
  data: function() {
    return {
      childInputData: null,
    }
  },
  methods: {
    onChildInput(event) {
      this.childInputData = event.target.value
      this.$emit('on-child-input', this.childInputData)
    },
  }
}
</script>

<style>
</style>
