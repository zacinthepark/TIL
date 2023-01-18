<template>
  <div>
    <WatchListForm />
    <WatchListItem
      v-for="(list, index) in watchList"
      :key="index"
      :list="list"
    />
    <button @click="loadList">저장했던 것 불러오기</button>
  </div>
</template>

<script>
import WatchListForm from "@/components/WatchListForm"
import WatchListItem from "@/components/WatchListItem"

export default {
  name: "WatchListView",
  components: {
    WatchListForm,
    WatchListItem,
  },
  computed: {
    watchList() {
      return this.$store.state.watchList
    },
  },
  methods:{
    loadList(){
      this.$store.dispatch('loadList')
    }
  }
}
</script>
