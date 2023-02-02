<template>
	<AppLoading v-if="loading" />

	<AppError v-else-if="error" :message="error.message" />

	<div v-else>
		<!-- <p>params: {{ $route.params }}</p> -->
		<!-- <p>query: {{ $route.query }}</p> -->
		<!-- <p>hash: {{ $route.hash }}</p> -->
		<h2>{{ post.title }}</h2>
		<p>{{ props.id }}, isOdd: {{ isOdd }}</p>
		<p>{{ post.content }}</p>
		<p class="text-muted">
			{{ $dayjs(post.createdAt).format('YYYY. MM. DD. HH:mm:ss') }}
		</p>
		<hr class="my-4" />
		<AppError v-if="removeError" :message="removeError.message" />
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
				<button
					class="btn btn-outline-danger"
					@click="remove"
					:disabled="removeLoading"
				>
					<template v-if="removeLoading">
						<span
							class="spinner-border spinner-border-sm"
							role="status"
							aria-hidden="true"
						></span>
						<span class="visually-hidden">Loading...</span>
					</template>
					<template v-else> 삭제 </template>
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { computed, ref, toRef, toRefs } from 'vue';

import { useRouter } from 'vue-router';
import { deletePost } from '../../api/posts';
import { useAlert } from '../../composables/alert';
import { useNumber } from '../../composables/number';
import { useAxios } from '../../hooks/useAxios';

const { vAlert, vSuccess } = useAlert();
// const idRef = toRef(props, 'id');
const { id: idRef } = toRefs(props);
const { isOdd } = useNumber(idRef);

const props = defineProps({
	id: [String, Number],
});
// const route = useRoute();
const router = useRouter();
// const id = route.params.id;
// const post = ref({});
// let post = reactive({});
// console.log('post: ', getPostById(id));
// const error = ref(null);
// const loading = ref(false);

const url = computed(() => `/posts/${props.id}`);
const { error, loading, data: post } = useAxios(url);

// const fetchPost = async () => {
// 	try {
// 		loading.value = true;
// 		const { data } = await getPostById(props.id);
// 		setPost(data);
// 	} catch (err) {
// 		error.value = err;
// 	} finally {
// 		loading.value = false;
// 	}
// 	// post.value = { ...data };
// 	// post.title = data.title;
// 	// post.content = data.content;
// 	// post.createdAt = data.createdAt;
// };
// const setPost = ({ title, content, createdAt }) => {
// 	post.value.title = title;
// 	post.value.content = content;
// 	post.value.createdAt = createdAt;
// };
// fetchPost();

const {
	error: removeError,
	loading: removeLoading,
	execute,
} = useAxios(
	`/posts/${props.id}`,
	{ method: 'delete' },
	{
		immediate: false,
		onSuccess: () => {
			vSuccess('삭제가 완료되었습니다.');
			router.push({ name: 'PostList' });
		},
		onError: err => {
			vAlert(err.message);
		},
	},
);
const remove = async () => {
	if (confirm('삭제하시겠습니까?') === false) {
		return;
	}
	execute();
};

// const removeError = ref(null);
// const removeLoading = ref(false);
// const remove = async () => {
// 	try {
// 		if (confirm('삭제하시겠습니까?') === false) {
// 			return;
// 		}
// 		removeLoading.value = true;
// 		await deletePost(props.id);
// 		router.push({ name: 'PostList' });
// 	} catch (err) {
// 		removeError.value = err;
// 	} finally {
// 		removeLoading.value = false;
// 	}
// };

const goListPage = () => {
	router.push({ name: 'PostList' });
};
const goEditPage = () => {
	router.push({ name: 'PostEdit', params: { id: props.id } });
};
</script>

<style lang="scss" scoped></style>
