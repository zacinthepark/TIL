<template>
	<div></div>
</template>

<script>
import { ref, reactive } from 'vue';
export default {
	setup() {
		// ref -> Object
		const count = ref(0);
		const state = reactive({
			count,
		});
		count.value++;
		count.value++;
		console.log(count.value);
		console.log('state.count: ', state.count); // ref 객체를 reactive Object에 넣으면 자동으로 언래핑

		// ref -> Array
		const message = ref('Hello');
		const arr = reactive([message]);
		console.log('arr[0]: ', arr[0].value); // ref 객체를 reactive Array에 넣으면 value로 접근
		return {};
	},
};
</script>

<style lang="scss" scoped></style>
