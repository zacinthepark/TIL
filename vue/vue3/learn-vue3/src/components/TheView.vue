<template>
	<main>
		<div class="containter py-4">
			<div class="row g-3">
				<div class="col col-4">
					<AppCard></AppCard>
					<!-- <app-card></app-card> -->
				</div>
				<div class="col col-4">
					<AppCard></AppCard>
				</div>
				<div class="col col-4">
					<AppCard></AppCard>
				</div>
				<div class="col col-4">
					<AppCard></AppCard>
				</div>
				<div class="col col-4">
					<AppCard></AppCard>
				</div>
				<div class="col col-4">
					<AppCard></AppCard>
				</div>
			</div>
		</div>
	</main>
</template>

<script>
import AppCard from './AppCard.vue';

export default {
	components: {
		AppCard,
	},
	setup() {
		return {};
	},
};
</script>

<style lang="scss" scoped></style>
