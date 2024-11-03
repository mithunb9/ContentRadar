<script>
	import '../app.css';
	let { children } = $props();
</script>

<div class="flex justify-between">
	<!-- Sidebar.svelte -->
	<div class="w-[20%] h-[100%] bg-gray-800 text-white fixed">
		<div class="p-4">
		<h2 class="text-2xl font-bold mb-6">Sidebar</h2>
		<nav class="space-y-4">
			<a href="/" class="block py-2 px-3 rounded hover:bg-gray-700">Home</a>
			<a href="/gaming" class="block py-2 px-3 rounded hover:bg-gray-700">Gaming</a>
			<a href="/shows" class="block py-2 px-3 rounded hover:bg-gray-700">Shows</a>
			<a href="/movies" class="block py-2 px-3 rounded hover:bg-gray-700">Movies</a>
			<a href="/news" class="block py-2 px-3 rounded hover:bg-gray-700">News</a>
			<a href="/tech" class="block py-2 px-3 rounded hover:bg-gray-700">Tech</a>
			<a href="/sports" class="block py-2 px-3 rounded hover:bg-gray-700">Sports</a>
			<a href="/music" class="block py-2 px-3 rounded hover:bg-gray-700">Music</a>
		</nav>
		</div>
	</div>

	<div class="w-[80%] justify-right absolute right-0">
		{@render children()}
	</div>
  
</div>
