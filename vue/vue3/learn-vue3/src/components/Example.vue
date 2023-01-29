<template>
	<main>
		<div class="container py-4">
			<MyButton class="my-button" id="my-button" @click="sayHello"></MyButton>
			<LabelInput label="이름"></LabelInput>
			<hr />
			<FancyButton>Click!! <span style="color: red">@@@</span></FancyButton>
			<FancyButton v-slot="{ fancyMessage }">{{ fancyMessage }}</FancyButton>
			<hr />
			<AppCard>
				<!-- <template #[slotArgs]>제목입니다</template> -->
				<!-- <template v-slot:default>내용입니다</template> -->
				<!-- 암시적으로 Default 슬롯입니다
				<template v-slot:footer>푸터입니다</template> -->
				<template #header="slotProps">
					{{ slotProps.headerMessage }}
				</template>
				<template #default="slotProps">
					디폴트입니다 {{ message }}
					<br />
					{{ slotProps.childMessage }}
					<br />
					{{ slotProps.helloMessage }}
				</template>
				<template #footer="slotProps">
					{{ slotProps.footerMessage }}
				</template>
			</AppCard>
			<hr />
			<AppCard>게시글입니다</AppCard>
		</div>
	</main>
</template>

<script>
import MyButton from './MyButton.vue';
import LabelInput from './LabelInput.vue';
import FancyButton from './FancyButton.vue';
import AppCard from './AppCard.vue';
import { ref } from 'vue';

export default {
	components: {
		MyButton,
		LabelInput,
		FancyButton,
		AppCard,
	},
	setup() {
		const sayHello = () => {
			alert('안녕하세요!');
		};
		const message = ref('안녕하세요!');
		const slotArgs = ref('header');
		return { sayHello, message, slotArgs };
	},
};
</script>

<style lang="scss" scoped></style>
