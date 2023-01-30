import axios from 'axios';
// axios
const posts = [
	{ id: 1, title: '제목1', content: '내용1', createdAt: '2023-01-30' },
	{ id: 2, title: '제목2', content: '내용2', createdAt: '2023-02-30' },
	{ id: 3, title: '제목3', content: '내용3', createdAt: '2023-03-30' },
	{ id: 4, title: '제목4', content: '내용4', createdAt: '2023-04-30' },
	{ id: 5, title: '제목5', content: '내용5', createdAt: '2023-05-30' },
];

export function getPosts() {
	return axios.get('http://localhost:3000/posts');
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
