export { matchers } from './matchers.js';

export const nodes = [
	() => import('./nodes/0'),
	() => import('./nodes/1'),
	() => import('./nodes/2'),
	() => import('./nodes/3'),
	() => import('./nodes/4'),
	() => import('./nodes/5'),
	() => import('./nodes/6'),
	() => import('./nodes/7'),
	() => import('./nodes/8'),
	() => import('./nodes/9'),
	() => import('./nodes/10'),
	() => import('./nodes/11'),
	() => import('./nodes/12'),
	() => import('./nodes/13'),
	() => import('./nodes/14')
];

export const server_loads = [];

export const dictionary = {
		"/": [8],
		"/Manager_Page": [9,[2]],
		"/Sign_In_Page": [10,[3]],
		"/Sign_Up_Page_Customer": [11,[4]],
		"/Sign_Up_Page_Drone": [12,[5]],
		"/contact": [13,[6]],
		"/track_order": [14,[7]]
	};

export const hooks = {
	handleError: (({ error }) => { console.error(error) }),
};

export { default as root } from '../root.svelte';