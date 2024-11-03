<script>
    export let data;

    if (data.image == null) {
        data.image = "https://via.placeholder.com/300";
    }

  </script>
  
<!-- Refined Card Component -->
<div class="min-w-[100%] h-[100%] mx-auto bg-gray-900 border border-gray-800 rounded-lg shadow-lg transition-transform duration-300 hover:shadow-2xl">
  <div class="relative overflow-hidden rounded-t-lg">
    <img
      class="w-full h-48 object-cover transition-transform duration-500 hover:scale-110"
      src={data.image}
      alt="Game Thumbnail"
    />
  </div>
  <div class="p-6">
    <h2 class="text-2xl font-bold text-white mb-2">{data.title.substring(0, )}</h2>
    <p class="text-gray-400 text-sm mb-4">{data.description.substring(0, 80)}...</p>
    <div class="flex items-center mb-4">
      <span class="bg-gray-700 text-gray-300 text-xs font-semibold rounded-full px-3 py-1">
        {data.site_name}
      </span>
    </div>
    <a
      href={data.url}
      target="_blank"
      class="inline-block bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold px-5 py-2 rounded-lg transition-colors duration-200"
    >
      Watch Now
    </a>
  </div>
</div>

  