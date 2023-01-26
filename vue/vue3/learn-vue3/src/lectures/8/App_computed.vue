<template>
	<div>
		<h2>{{ teacher.name }}</h2>
		<h3>강의가 있습니까?</h3>
		<!-- <p>{{ teacher.lectures.length > 0 ? '있음' : '없음' }}</p> -->
		<!-- computed는 method와 다르게 반응형 데이터에 변화가 없다면 캐싱된 데이터를 돌려줌, 고로 더 유리함 -->
		<p>{{ hasLecture }}</p>
		<p>{{ hasLecture }}</p>
		<p>{{ existLecture() }}</p>
		<p>{{ existLecture() }}</p>
		<button v-on:click="counter++">Counter: {{ counter }}</button>

		<h2>이름</h2>
		<p>{{ fullName }}</p>
	</div>
</template>

<script>
import { ref, computed, reactive } from 'vue';

export default {
	setup() {
		const teacher = reactive({
			name: 'Aiden',
			lectures: ['HTML/CSS', 'JavaScript', 'Vue3'],
		});

		const hasLecture = computed(() => {
			console.log('computed');
			return teacher.lectures.length > 0 ? '있음' : '없음';
		});

		const existLecture = () => {
			console.log('method');
			return teacher.lectures.length > 0 ? '있음' : '없음';
		};

		const counter = ref(0);

		const firstName = ref('홍');
		const lastName = ref('길동');
		const fullName = computed({
			get() {
				return firstName.value + ' ' + lastName.value;
			},
			set(value) {
				console.log('value ', value);
				console.log(value.split(' '));
				[firstName.value, lastName.value] = value.split(' ');
			},
		});
		console.log('Console 출력: ', fullName.value);
		fullName.value = '짐 코딩';
		return {
			teacher,
			hasLecture,
			existLecture,
			counter,
			fullName,
		};
	},
};
</script>

<style lang="scss" scoped></style>
