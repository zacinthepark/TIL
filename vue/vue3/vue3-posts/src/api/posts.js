// import axios from 'axios';
import { posts } from '.';

export function getPosts(params) {
	return posts.get('/', { params });
}
// export function getPosts(params) {
// 	return axios.get('http://localhost:3000/posts', { params });
// }

export function getPostById(id) {
	return posts.get(id);
}
// export function getPostById(id) {
// 	return axios.get(`http://localhost:3000/posts/${id}`);
// }

export function createPost(data) {
	return posts.post('', data);
}
// export function createPost(data) {
// 	return axios.post('http://localhost:3000/posts', data);
// }

export function updatePost(id, data) {
	return posts.put(id, data);
}
// export function updatePost(id, data) {
// 	return axios.put(`http://localhost:3000/posts/${id}`, data);
// }

export function deletePost(id) {
	return posts.delete(`/${id}`);
}
// export function deletePost(id) {
// 	return axios.delete(`http://localhost:3000/posts/${id}`);
// }
