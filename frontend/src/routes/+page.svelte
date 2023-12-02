<script lang="ts">
	import Marker from "../Components/Marker.svelte";
    import Leaflet from "../lib/Leaflet.svelte";

    import type { LatLngExpression } from "leaflet";

    const initialView: LatLngExpression = [51.514244, 7.468429];
</script>

<main>
    <h1>Map</h1>
    <Leaflet view={initialView} zoom={13}>
        <Marker width={40} height={50} />
    </Leaflet>
</main>

<style lang="scss">
    
</style>