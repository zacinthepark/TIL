import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import { createApp } from 'vue';
import App from './App.vue';
import router from '@/router';
import { createPinia } from 'pinia';
// import funcPlugins from './plugins/func';
// import objPlugins from './plugins/obj';
// import person from './plugins/person';
import globalComponents from './plugins/global-components';
import globalDirectives from './plugins/global-directives';
import dayjs from './plugins/dayjs';
// import focus from '@/directives/focus';

const app = createApp(App);
// app.use(funcPlugins);
// app.use(objPlugins, { name: 'zac' });
// app.use(person, { name: '홍길동' });
// app.directive('focus', focus);
app.use(globalComponents);
app.use(globalDirectives);
app.use(dayjs);
app.use(router);
app.use(createPinia());
app.mount('#app');
import 'bootstrap/dist/js/bootstrap.js';

// 현재 구동되는 어플리케이션이 개발모드인지, 혹은 어떤모드인지
// console.log('MODE: ', import.meta.env.MODE);
// console.log('BASE_URL: ', import.meta.env.BASE_URL);
// Production 모드라면 true
// console.log('PROD: ', import.meta.env.PROD);
// 개발 모드라면 true
// console.log('DEV: ', import.meta.env.DEV);
// console.log('VITE_APP_API_URL: ', import.meta.env.VITE_APP_API_URL);
