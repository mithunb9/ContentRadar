<script>
  // Ensure recommendations is always an array by default
  import Embed from "./Embed.svelte";

  export let recommendations = [];

  // Sort recommendations by confidence in descending order
  let sortedRecommendations = recommendations ? [...recommendations].sort((a, b) => b.confidence - a.confidence) : [];
</script>

<!-- Mosaic Grid Layout -->
<div class="grid grid-cols-3 grid-rows-4 gap-2 w-[100%] h-screen p-2">
  <div class="col-span-2 row-span-2 flex items-center justify-center text-white font-bold text-lg">
    <Embed data={sortedRecommendations[0]}/>
  </div>
  <div class="col-span-1 row-span-2 flex items-center justify-center text-white font-bold text-lg">
    <Embed data={sortedRecommendations[1]}/>
  </div>
  <div class="col-span-1 row-span-2 flex items-center justify-center text-white font-bold text-lg">
    <Embed data={sortedRecommendations[2]}/>
  </div>
  <div class="col-span-1 row-span-2 flex items-center justify-center text-white font-bold text-lg">
    <Embed data={sortedRecommendations[3]}/>
  </div>
  <div class="col-span-1 row-span-2 flex items-center justify-center text-white font-bold text-lg">
    <Embed data={sortedRecommendations[4]}/>
  </div>
</div>

<style>
/* Add any additional custom styles if needed */
</style>