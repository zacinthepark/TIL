import axios from 'axios';
import { isRef, ref, unref, watchEffect } from 'vue';

axios.defaults.baseURL = import.meta.env.VITE_APP_API_URL;

const defaultConfig = {
	method: 'get',
};

export const useAxios = (url, config = {}) => {
	const response = ref(null);
	const data = ref(null);
	const error = ref(null);
	const loading = ref(false);

	const { params } = config;
	const execute = () => {
		data.value = null;
		error.value = null;
		loading.value = true;
		axios(url, {
			...defaultConfig,
			...config,
			params: unref(params),
		})
			.then(res => {
				response.value = res;
				console.log(response.value);
				data.value = res.data;
			})
			.catch(err => {
				error.value = err;
			})
			.finally(() => {
				loading.value = false;
			});
	};
	if (isRef(params)) {
		watchEffect(execute);
	} else {
		execute();
	}
	return {
		response,
		data,
		error,
		loading,
	};
};
