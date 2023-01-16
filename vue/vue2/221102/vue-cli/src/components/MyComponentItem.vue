<template>
  <div>
    <h3>MyComponent's Child Component</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent">Click!</button>
    <input type="text"
    v-model="childInputData"
    @keyup.enter="childInput"
    >
  </div>
</template>

<script>
export default {
  name: 'MyComponentItem',
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  data: function() {
    return {
      childInputData: null,
    }
  },
  methods: {
    // 정적 데이터 올리기
    childToParent: function() {
      // 이 컴포넌트 객체의 기본 내장 속성값이므로 $ 붙임
      // emit event 1번째 인자는 이벤트 이름, 2번째 인자는 데이터
      this.$emit('child-to-parent', 'i am data from child')
    },
    // 동적 데이터 올리기
    childInput: function() {
      this.$emit('child-input', this.childInputData)
      this.childInputData = null  // input에 값 입력 후 enter치면 값 초기화
    }
  },
}
</script>

<style>
</style>
