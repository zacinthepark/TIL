<template>
	<div>
		<!-- <p>params: {{ $route.params }}</p> -->
		<!-- <p>query: {{ $route.query }}</p> -->
		<!-- <p>hash: {{ $route.hash }}</p> -->
		<h2>{{ form.title }}</h2>
		<p>{{ form.content }}</p>
		<p class="text-muted">{{ form.createdAt }}</p>
		<hr class="my-4" />
		<div class="row g-2">
			<div class="col-auto">
				<button class="btn btn-outline-dark">이전글</button>
			</div>
			<div class="col-auto">
				<button class="btn btn-outline-dark">다음글</button>
			</div>
			<div class="col-auto me-auto"></div>
			<div class="col-auto">
				<button class="btn btn-outline-dark" @click="goListPage">목록</button>
			</div>
			<div class="col-auto">
				<button class="btn btn-outline-primary" @click="goEditPage">
					수정
				</button>
			</div>
			<div class="col-auto">
				<button class="btn btn-outline-danger">삭제</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { reactive } from 'vue';
import { useRouter } from 'vue-router';
import { getPostById } from '../../api/posts';

const props = defineProps({
	id: Number,
});

// const route = useRoute();
const router = useRouter();
// const id = route.params.id;
// const form = ref({});
let form = reactive({});
// console.log('post: ', getPostById(id));
const fetchPost = () => {
	const data = getPostById(props.id);
	// form.value = { ...data };
	form.title = data.title;
	form.content = data.content;
	form.createdAt = data.createdAt;
};
fetchPost();

const goListPage = () => {
	router.push({ name: 'PostList' });
};
const goEditPage = () => {
	router.push({ name: 'PostEdit', params: { id: props.id } });
};
</script>

<style lang="scss" scoped></style>
