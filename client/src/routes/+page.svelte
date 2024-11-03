<script>
  // Import the `embeds` data from the `load` function
  import Mosiac from '../lib/Mosiac.svelte';

  let { data } = $props();

  let embeds = data.data
</script>

<div class="w-[100%]">
  <Mosiac recommendations={embeds} />
</div>

