<script>
import Sidebar from '../lib/components/ui/sidebar/Sidebar.svelte';

let props = $props();
</script>

<div> 
  <Sidebar />
  <h1>Welcome to SvelteKit</h1>
  <h1>{props.data.recommendations}</h1>
</div>