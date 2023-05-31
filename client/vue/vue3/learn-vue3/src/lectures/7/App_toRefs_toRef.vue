<template>
	<div>
		<p>author: {{ author }}</p>
		<p>title: {{ title }}</p>
		<p>year: {{ year }}</p>
	</div>
</template>

<script>
import { reactive, toRefs, toRef } from 'vue';

export default {
	setup() {
		const book = reactive({
			author: 'Vue Team',
			year: '2020',
			title: 'Vue 3 Guide',
			description: '당신은 이 책을 지금 바로 읽습니다 ;)',
			price: '무료',
		});

		// 구조분해할당하면 반응형 객체의 값을 재할당한 것으로 반응성을 잃어버림
		// toRef, toRefs를 통해 구조분해할당 시에도 반응성을 유지
		// const { author, title } = book;
		const { author, title } = toRefs(book);
		const year = toRef(book, 'year');

		return {
			author,
			title,
			year,
		};
	},
};
</script>

<style lang="scss" scoped></style>
