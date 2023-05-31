<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" @input="onParentInput">
    <!-- <p>parentData: {{ parentInputData }}</p> -->
    <p>appData: {{ appInputData }}</p>
    <p>childData: {{ childInputData }}</p>
    <app-child :app-input-data="appInputData" :parent-input-data="parentInputData" @on-child-input="getChildInput"></app-child>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'

export default {
  name: 'AppParent',
  components: {
    AppChild,
  },
  props: {
    appInputData: String,
  },
  data: function() {
    return {
      parentInputData: null,
      childInputData: null,
    }
  },
  methods: {
    onParentInput(event) {
      this.parentInputData = event.target.value
      this.$emit('on-parent-input', this.parentInputData)
    },
    getChildInput(childInputData) {
      this.childInputData = childInputData
      this.$emit('on-child-input', this.childInputData)
    },
  }
}
</script>

<style>
</style>
