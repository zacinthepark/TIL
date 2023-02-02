<template>
	<div>
		<h2>Home View</h2>
		<!-- <p>{{ $route.path }}</p> -->
		<!-- <p>{{ $route.name }}</p> -->
		<button class="btn btn-primary" @click="goAboutPage">About으로 이동</button>
		<hr class="my-4" />
		<AppGrid :items="items" v-slot="{ item }" col-class="col-6">
			<AppCard>{{ item }}</AppCard>
		</AppGrid>
		<hr class="my-4" />
		<!-- <h2>{{ $person.name }}</h2>
		<button class="btn btn-primary" @click="person.say">click person</button> -->
		<h2>{{ position }}</h2>
		<h2>x: {{ x }}</h2>
		<h2>y: {{ y }}</h2>
	</div>
</template>

<!-- <script>
export default {
	created() {
			console.log(this.$person.name);
			this.$person.say();
	},
};
</script> -->

<script setup>
import { ref, reactive, inject, toRef, toRefs } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const goAboutPage = () => {
	router.push('/about');
};

const items = ref(['김민경', '김호준', '박이령', '박진우', '이성희', '황영준']);

// const person = inject('person');
// console.log('person.name: ', person.name);

const position = reactive({
	x: 100,
	y: 1000,
});
// const { x, y } = position;
// console.log('x: ', typeof x);
// console.log('y: ', typeof y);

// toRef and toRefs
// const x = toRef(position, 'x');
// const y = toRef(position, 'y');
const { x, y } = toRefs(position);
</script>

<style lang="scss" scoped></style>
