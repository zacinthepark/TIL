<template>
	<div>
		<h2 v-if="visible">Hello Vue!</h2>
		<h2 v-else>False입니다.</h2>
		<button v-on:click="visible = !visible">toggle</button>
		<hr />
		<button v-on:click="type = 'A'">toggle</button>
		<button v-on:click="type = 'B'">toggle</button>
		<button v-on:click="type = 'C'">toggle</button>
		<button v-on:click="type = 'D'">toggle</button>
		<h2 v-if="type === 'A'">A입니다.</h2>
		<h2 v-else-if="type === 'B'">B입니다.</h2>
		<h2 v-else-if="type === 'C'">C입니다.</h2>
		<h2 v-else>A, B, C가 아닙니다.</h2>
		<hr />
		<template v-if="visible">
			<h1>Title</h1>
			<p>Paragraph 1</p>
			<p>Paragraph 2</p>
		</template>
		<hr />
		<h1 v-show="ok">Title입니다.</h1>
		<button v-on:click="ok = !ok">show toggle</button>
	</div>
</template>

<script>
import { ref } from 'vue';

export default {
	setup() {
		const visible = ref(false);
		const type = ref('A');
		const ok = ref(true);
		return {
			visible,
			type,
			ok,
		};
	},
};
</script>

<style lang="scss" scoped></style>
