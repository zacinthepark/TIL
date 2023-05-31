<template>
  <div>
    <h2>점심 메뉴</h2>
    <button @click="[getLunchMenu(), sendMenuToApp()]">Pick One</button>
    <p>{{ selectedMenu }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'TheLunch',
  data: function() {
    return {
      menus: ['국밥', '편백찜', '가락국수', '냉면', '햄버거', '팥죽', '곰탕', '초밥', '설렁탕', '간짜장', '짬뽕'],
      selectedMenu: null,
    }
  },
  methods: {
    getLunchMenu: function() {
      this.selectedMenu = _.sample(this.menus)
    },
    sendMenuToApp: function() {
      this.$emit('send-menu-to-app', this.selectedMenu)
    }
  }
}
</script>

<style>
</style>
