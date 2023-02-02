<template>
	<div v-if="response">
		<h2>게시글 목록</h2>
		<hr class="my-4" />

		<PostFilter
			v-model:title="params.title_like"
			:limit="params._limit"
			@update:limit="changeLimit"
		/>

		<hr class="my-4" />

		<AppLoading v-if="loading" />

		<AppError v-else-if="error" :message="error.message" />

		<template v-else-if="!isExist">
			<p class="text-center py-5 text-muted">No Results</p>
		</template>

		<template v-else>
			<AppGrid :items="posts" col-class="col-12 col-sm-6 col-md-4 col-lg-3">
				<template v-slot="{ item }">
					<PostItem
						:title="item.title"
						:content="item.content"
						:created-at="item.createdAt"
						@click="goPage(item.id)"
						@modal="openModal(item)"
						@preview="selectPreview(item.id)"
					></PostItem>
				</template>
			</AppGrid>
		</template>

		<AppPagination
			:current-page="params._page"
			:page-count="pageCount"
			@page="page => (params._page = page)"
		/>

		<Teleport to="#modal">
			<PostModal
				v-model="show"
				:title="modalTitle"
				:content="modalContent"
				:created-at="modalCreatedAt"
			/>
		</Teleport>

		<template v-if="previewId">
			<hr class="my-5" />
			<AppCard>
				<PostDetailView :id="previewId"></PostDetailView>
			</AppCard>
		</template>
	</div>
</template>

<script setup>
import PostItem from '../../components/posts/PostItem.vue';
import PostDetailView from './PostDetailView.vue';
import PostFilter from '../../components/posts/PostFilter.vue';
import PostModal from '../../components/posts/PostModal.vue';
import { computed, ref } from 'vue';
// import { getPosts } from '@/api/posts';
import { useRouter } from 'vue-router';
import { useAxios } from '@/hooks/useAxios';

const router = useRouter();

const previewId = ref(null);
const selectPreview = id => {
	previewId.value = id;
};

// const posts = ref([]);
// const error = ref(null);
// const loading = ref(false);

const params = ref({
	_sort: 'createdAt',
	_order: 'desc',
	_page: 1,
	_limit: 6,
	title_like: '',
});
const changeLimit = value => {
	params.value._limit = value;
	params.value._page = 1;
};
const {
	response,
	data: posts,
	error,
	loading,
} = useAxios('/posts', { params });

const isExist = computed(() => posts.value && posts.value.length > 0);

// pagination
const totalCount = computed(() => response.value.headers['x-total-count']);
const pageCount = computed(() =>
	Math.ceil(totalCount.value / params.value._limit),
);

// const fetchPosts = async () => {
// 	try {
// 		loading.value = true;
// 		const { data, headers } = await getPosts(params.value);
// 		posts.value = data;
// 		totalCount.value = headers['x-total-count'];
// 	} catch (err) {
// 		error.value = err;
// 	} finally {
// 		loading.value = false;
// 	}
// 	// const response = await getPosts();
// 	// console.dir(response);
// 	// getPosts()
// 	// 	.then(response => {
// 	// 		console.log('response: ', response);
// 	// 	})
// 	// 	.catch(error => {
// 	// 		console.log('error: ', error);
// 	// 	});
// };
// watchEffect(fetchPosts);
// fetchPosts();

const goPage = id => {
	// router.push(`/posts/${id}`);
	router.push({
		name: 'PostDetail',
		params: {
			id: id,
		},
	});
};
// modal
const show = ref(false);
const modalTitle = ref('');
const modalContent = ref('');
const modalCreatedAt = ref('');
const openModal = ({ title, content, createdAt }) => {
	show.value = true;
	modalTitle.value = title;
	modalContent.value = content;
	modalCreatedAt.value = createdAt;
};
</script>

<style lang="scss" scoped></style>
