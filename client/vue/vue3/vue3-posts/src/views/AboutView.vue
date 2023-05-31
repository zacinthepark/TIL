<template>
	<div>
		<h2>About View</h2>
		<!-- <p>{{ $route.path }}</p> -->
		<button class="btn btn-primary" @click="$router.push('/')">
			Home으로 이동
		</button>
		<hr class="py-4" />
		<h2>Store</h2>
		<p>counter: {{ counter }}</p>
		<p>doubleCount: {{ doubleCount }}</p>
		<p>doubleCountPlusOne {{ doubleCountPlusOne }}</p>
		<button @click="increment()">Click!</button>
	</div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/store/counter';
import { storeToRefs } from 'pinia';

const route = useRoute();
console.log('route.path: ', route.path);

const store = useCounterStore();
// console.log(store);
const { counter, doubleCount, doubleCountPlusOne } = storeToRefs(store);
const { increment } = store;
counter.value = 100;
</script>

<style lang="scss" scoped></style>
