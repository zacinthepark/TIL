<template>
	<div class="card">
		<div class="card-header">Child Component</div>
		<div class="card-body">
			<DeepChildExample></DeepChildExample>
		</div>
	</div>
</template>

<script>
import DeepChildExample from './DeepChildExample.vue';

export default {
	components: {
		DeepChildExample,
	},
	setup() {
		return {};
	},
};
</script>

<style lang="scss" scoped></style>
