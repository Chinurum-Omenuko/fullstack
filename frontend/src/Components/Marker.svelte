<script lang="ts">
	import * as L from "leaflet";
	import { getContext, onDestroy, onMount, setContext } from "svelte";

    let marker: L.Marker | undefined;
    let markerContainer: HTMLElement;
    export let width: number;
    export let height: number;

    interface mapContext {
        getMap: () => L.Map | undefined
    }

    const map: L.Map = getContext<mapContext>('map')?.getMap()

    setContext('layer', 
    {
        getLayer: () => marker
    });
    
    onMount( () => {
        if (map){
            marker = L.marker([51.514244, 7.468429]).addTo(map)
        }
    });

    onDestroy( () => {
        marker?.remove();
        marker = undefined;
    });
</script>

<div bind:this={markerContainer}>
    {#if marker}
        <slot />
    {/if}
</div>

<style>

</style>