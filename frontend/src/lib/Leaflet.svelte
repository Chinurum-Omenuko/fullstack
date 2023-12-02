<script lang="ts">
  import {onMount, onDestroy, setContext} from 'svelte'
  import * as L from 'leaflet';
  import 'leaflet/dist/leaflet.css'
  import Marker from '../Components/Marker.svelte';

  let map: L.Map | undefined;
  let mapElement: HTMLDivElement;

  export let bounds: L.LatLngBoundsExpression | undefined = undefined;
  export let view: L.LatLngExpression | undefined = undefined;
  export let zoom: number | undefined = undefined;

  onMount(() => {
    map = L.map(mapElement)

    L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
    attribution: `&copy;<a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>,&copy;<a href="https://carto.com/attributions" target="_blank">CARTO</a>`}).addTo(map);
  })

  onDestroy(() => {
    map?.remove();
    map = undefined;
  })

  setContext('map',{getMap: () => map})

  $: if(map) {
    if(bounds) {
      map.fitBounds(bounds);
    }else if (view && zoom) {
      map.setView(view, zoom)
    }
  }
</script>

<div bind:this={mapElement}>
  {#if map}
    <slot />
  {/if}
</div>

<style>
  div{
    position: absolute;
    width: 100%;
    min-height: 70vh;
    border: solid 2px red;
  }
</style>