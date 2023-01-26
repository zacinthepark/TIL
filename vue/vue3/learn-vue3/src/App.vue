<template>
	<div>
		<p>{{ msg }}</p>
		<p v-text="msg"></p>
		<p v-text="htmlStr"></p>
		<p v-html="htmlStr"></p>
	</div>
</template>

<script>
import { ref } from 'vue';

export default {
	setup() {
		const msg = ref('안녕하세요');
		const htmlStr = ref('<strong>안녕!</strong>');
		return {
			msg,
			htmlStr,
		};
	},
};
</script>

<style lang="scss" scoped></style>
