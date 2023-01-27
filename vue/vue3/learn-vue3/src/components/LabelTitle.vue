<template>
	<div>
		<label>
			{{ label }}
			<input v-model="value" type="text" />
		</label>
	</div>
</template>

<script>
import { computed } from 'vue';
export default {
	props: ['title', 'label'],
	emits: ['update:title'],
	setup(props, context) {
		const value = computed({
			get() {
				return props.title;
			},
			set(value) {
				context.emit('update:title', value);
			},
		});
		return { value };
	},
};
</script>

<style lang="scss" scoped></style>
