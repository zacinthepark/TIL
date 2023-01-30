import axios from 'axios';

export function getPosts(params) {
	return axios.get('http://localhost:3000/posts', { params });
}

export function getPostById(id) {
	return axios.get(`http://localhost:3000/posts/${id}`);
}

export function createPost(data) {
	return axios.post('http://localhost:3000/posts', data);
}

export function updatePost(id, data) {
	return axios.put(`http://localhost:3000/posts/${id}`, data);
}

export function deletePost(id) {
	return axios.delete(`http://localhost:3000/posts/${id}`);
}
