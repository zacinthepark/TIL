<template>
	<div class="container py-4">
		<button
			class="btn btn-primary me-2"
			@click="changeCurrentComp(DynamicApple)"
		>
			사과
		</button>
		<button class="btn btn-danger" @click="changeCurrentComp(DynamicBanana)">
			바나나
		</button>
		<hr />
		<component :is="currentComp" />
		<!-- <p>{{ obj1 }}</p> -->
		<!-- <p>{{ obj2 }}</p> -->
	</div>
</template>

<script setup>
import { ref, shallowRef } from 'vue';

import DynamicApple from './DynamicApple.vue';
import DynamicBanana from './DynamicBanana.vue';

const currentComp = shallowRef(DynamicApple);
const changeCurrentComp = comp => (currentComp.value = comp);

// shallowRef는 그 자체가 변경되었을 때만 반응하며, 그 안에 속성이 바뀌었을 때는 반응하지 않음
const obj1 = ref({ name: '홍길동' });
const obj2 = ref({ name: '김길동' });
</script>

<style lang="scss" scoped></style>
