<template>
	<div class="container py-4">
		<input ref="inputRef" type="text" value="hello world" />
		<hr />
		<button @click="visible = !visible">Toggle Child</button>
		<LifecycleChild v-if="visible"></LifecycleChild>
		<p id="message">{{ message }}</p>
	</div>
</template>

<script>
import { ref, onBeforeMount, onMounted, onBeforeUpdate, onUpdated } from 'vue';
import LifecycleChild from './LifecycleChild.vue';

export default {
	components: {
		LifecycleChild,
	},
	setup() {
		// console.log('setup');
		const inputRef = ref(null);
		const message = ref('');
		const visible = ref(false);
		// onBeforeMount(() => {
		// 	console.log('onBeforeMount', inputRef.value);
		// });
		// onMounted(() => {
		// 	console.log('onMounted', inputRef.value.value);
		// });
		// onBeforeUpdate(() => {
		// 	console.log('onBeforeUpdate');
		// 	console.log(
		// 		'DOM content: ',
		// 		document.querySelector('#message').textContent,
		// 	);
		// });
		// onUpdated(() => {
		// 	console.log('onUpdated');
		// 	console.log(
		// 		'DOM content: ',
		// 		document.querySelector('#message').textContent,
		// 	);
		// });
		return { inputRef, message, visible };
	},
};
</script>

<style lang="scss" scoped></style>
