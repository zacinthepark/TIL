<template>
	<div>
		<p>{{ count }}</p>
		<p>{{ message }}</p>
		<button @click="increment">click!</button>
	</div>
</template>

<script>
import { ref } from 'vue';
export default {
	setup() {
		const count = ref(0);
		const message = ref('Hello Vue3');
		const increment = () => {
			count.value++;
		};
		return {
			count,
			message,
			increment,
		};
	},
};
</script>

<style lang="scss" scoped></style>
