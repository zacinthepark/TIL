<template>
	<div class="p-3 bg-danger">
		<!-- <button type="button" class="btn btn-primary" v-bind="$attrs"> -->
		<button type="button" class="btn btn-primary" @click="sayHello">
			My Button
		</button>
		<!-- {{ $attrs }} -->
	</div>
</template>

<script>
export default {
	// inheritAttrs: false,
	emits: ['click'],
	setup(props, { emit }) {
		// console.log('context.attrs: ', context.attrs);
		const sayHello = () => {
			emit('click');
		};
		return { sayHello };
	},
};
</script>

<style lang="scss" scoped></style>
