<script>
	import '../app.css';
	let { children } = $props();

	import FaHome from 'svelte-icons/fa/FaHome.svelte'	
	import FaGamepad from 'svelte-icons/fa/FaGamepad.svelte'
	import FaTv from 'svelte-icons/fa/FaTv.svelte'	
	import FaFilm from 'svelte-icons/fa/FaFilm.svelte'
	import FaNewspaper from 'svelte-icons/fa/FaNewspaper.svelte'
	import FaLaptopCode from 'svelte-icons/fa/FaLaptopCode.svelte'
	import FaBasketballBall from 'svelte-icons/fa/FaBasketballBall.svelte'
	import FaMusic from 'svelte-icons/fa/FaMusic.svelte'
</script>

<div class="flex justify-between">
	<!-- Sidebar.svelte -->
	<div class="w-64 h-screen bg-gray-900 text-white fixed">
		<div class="p-6">
		  <div class="flex items-center mb-8">
			<span class="text-lg font-semibold">Hey Adith!</span>
		  </div>
		  <nav class="space-y-6">
			<a href="/" class="flex items-center py-2 px-3 rounded hover:bg-gray-800">
			  <FaHome class="mr-3" style="width: 5px; height: 5px;" />
			  Home
			</a>
			<a href="/gaming" class="flex items-center py-2 px-3 rounded hover:bg-gray-800">
			  <FaGamepad class="mr-3" style="width: 5px; height: 5px;" />
			  Gaming
			</a>
			<a href="/shows" class="flex items-center py-2 px-3 rounded hover:bg-gray-800">
			  <FaTv class="mr-3" style="width: 5px; height: 5px;" />
			  Shows
			</a>
			<a href="/movies" class="flex items-center py-2 px-3 rounded hover:bg-gray-800">
			  <FaFilm class="mr-3" style="width: 5px; height: 5px;" />
			  Movies
			</a>
			<a href="/news" class="flex items-center py-2 px-3 rounded hover:bg-gray-800">
			  <FaNewspaper class="mr-3" style="width: 5px; height: 5px;" />
			  News
			</a>
			<a href="/tech" class="flex items-center py-2 px-3 rounded hover:bg-gray-800">
			  <FaLaptopCode class="mr-3" style="width: 5px; height: 5px;" />
			  Tech
			</a>
			<a href="/sports" class="flex items-center py-2 px-3 rounded hover:bg-gray-800">
			  <FaBasketballBall class="mr-3" style="width: 5px; height: 5px;" />
			  Sports
			</a>
			<a href="/music" class="flex items-center py-2 px-3 rounded hover:bg-gray-800">
			  <FaMusic class="mr-3" style="width: 5px; height: 5px;" />
			  Music
			</a>
		  </nav>
		</div>
	  </div>
	  

	<div class="w-[80%] justify-right absolute right-0">
		{@render children()}
	</div>
  
</div>
