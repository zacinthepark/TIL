<template>
  <div>
    <p v-if="!imgSrc">{{ message }}</p>
    <img :src="imgSrc" alt="">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogView',
  data() {
    return {
      imgSrc: null,
      message: 'Loading...',
    }
  },
  methods: {
    getDogImage() {
      const breed = this.$route.params.breed
      const dogImageUrl = `https://dog.ceo/api/breed/${breed}/images/random`

      axios({
        method: 'get',
        url: dogImageUrl,
      })
        .then((response) => {
          console.log(response)
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => {
          console.log(error)
          // this.message = `${this.$route.params.breed} is not a dog breed...`
          this.$router.push('/404')
        })
    }
  },
  created() {
    this.getDogImage()
  },
}
</script>

<style>
</style>
