<template>
	<div></div>
</template>

<script>
import { reactive, ref, watch } from 'vue';

export default {
	setup() {
		const x = ref(0);
		const y = ref(0);

		const obj = reactive({
			count: 0,
		});

		// object
		// watch(obj, (newValue, oldValue) => {
		// 	console.log('newValue: ', newValue);
		// 	console.log('oldValue: ', oldValue);
		// });

		// object 속성을 감지하고 싶을 때는 getter 함수로 접근
		// watch(
		// 	() => obj.count,
		// 	(newValue, oldValue) => {
		// 		console.log('newValue: ', newValue);
		// 	},
		// );

		// getter
		// watch(
		// 	() => x.value + y.value,
		// 	(sum, oldValue) => {
		// 		console.log('sum, ', sum);
		// 	},
		// );

		// array
		// watch([x, y], ([newX, newY]) => {
		// 	console.log(newX, newY);
		// });

		// deep option
		const person = reactive({
			name: '홍길동',
			age: 30,
			hobby: '운동',
			obj: {
				count: 0,
			},
		});

		watch(person, newValue => {
			console.log('newValue: ', newValue);
		});

		return { x, y, obj, person };
	},
};
</script>

<style lang="scss" scoped></style>
