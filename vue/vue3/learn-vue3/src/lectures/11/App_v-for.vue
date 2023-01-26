<template>
	<div>
		<ul>
			<template v-for="(item, index) in evenItems" :key="item.id">
				<!-- <li v-if="item.id % 2 === 0"> -->
				<li>ID: {{ item.id }}, INDEX: {{ index }}, {{ item.message }}</li>
			</template>
		</ul>
		<hr />
		<ul>
			<li v-for="(value, key, index) in myObject" :key="key">
				{{ index }} - {{ key }} - {{ value }}
			</li>
		</ul>
	</div>
</template>

<script>
import { reactive, computed } from 'vue';

export default {
	setup() {
		const items = reactive([
			{ id: 1, message: 'Java' },
			{ id: 2, message: 'HTML' },
			{ id: 3, message: 'CSS' },
			{ id: 4, message: 'JavaScript' },
		]);

		const evenItems = computed(() => items.filter(item => item.id % 2 === 0));

		const myObject = reactive({
			title: '제목입니다.',
			author: '홍길동',
			publishedAt: '2016-04-10',
		});

		return { items, evenItems, myObject };
	},
};
</script>

<style lang="scss" scoped></style>
