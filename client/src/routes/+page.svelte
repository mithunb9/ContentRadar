<script>
import Sidebar from '../lib/components/ui/sidebar/Sidebar.svelte';

let props = $props();
const recommendations = [
      { link: 'https://www.streameast.gd/game/cfb/82148814', confidence: 0.4 },
      { link: 'https://svelte.dev/docs/kit/load', confidence: 0.5 },
      {
        link: 'https://stackoverflow.com/questions/34600003/converting-json-to-string-in-python',
        confidence: 0.1
      }
    ];
</script>

<div> 
  <Sidebar />
  <Mosiac {recommendations} />
</div>