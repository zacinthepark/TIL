<template>
	<div class="containter py-4">
		<div class="card">
			<div class="card-header">ProvideInject Component</div>
			<div class="card-body">
				<button @click="count++">Click</button>
				<p>appMessage: {{ appMessage }}</p>
				<ChildExample></ChildExample>
			</div>
		</div>
	</div>
</template>

<script>
import { inject, readonly, provide, ref } from 'vue';
import ChildExample from './ChildExample.vue';

export default {
	components: {
		ChildExample,
	},
	setup() {
		const staticMessage = ref('static message');
		const message = ref('message');
		const updateMessage = appendMessage => {
			message.value = message.value + appendMessage;
		};
		const count = ref(10);
		// provide('static-message', staticMessage);
		provide('message', { message: readonly(message), updateMessage });
		provide('count', count);
		const msg = inject('msg');
		console.log('msg: ', msg);

		const appMessage = inject('app-message');
		return { count, appMessage };
	},
	mounted() {
		console.log('this.msg: ', this.msg);
	},
};
</script>

<style lang="scss" scoped></style>
