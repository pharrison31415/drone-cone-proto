import { sveltekit } from '@sveltejs/kit/vite';
import dns from 'dns';
import { defineConfig } from 'vite';

dns.setDefaultResultOrder('verbatim');

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		host: 'localhost',
		port: 5173
	}
});
