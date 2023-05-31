<template>
  <div class="border">
    <h1>This is My Component!</h1>
    <!-- 3. 보여주기 -->
    <MyComponentItem 
      static-props="Props Data from MyComponent"
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent"
      @child-input="getDynamicData"
    />
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name: 'MyComponent',
  // 2. 등록하기
  components: {
    MyComponentItem,
  },
  // Vue CLI에서는 data가 함수의 리턴 객체여야함
  data: function() {
    return {
      dynamicProps: 'This is a Dynamic Props Data',
    }
  },
  methods: {
    parentGetEvent: function(childData) {
      console.log('Listening to Emit Event from Child Component!')
      console.log(`DATA: ${childData}`)
      // this.$emit('go-up-again', childData)  // MyComponentItem에서 온 데이터를 다시 App으로 올려주고 싶은 경우
    },
    getDynamicData: function(childInputData) {
      console.log(`USER said: ${childInputData}!`)
    }
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>
