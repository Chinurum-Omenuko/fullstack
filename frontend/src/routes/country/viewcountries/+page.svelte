<script lang="ts">
	import Card from "../../../Components/Card.svelte";

    export let data;
</script>


{#each data.countries as country}
    <Card name={country.name} country={country.country}/>
{/each}

<!-- <li>{country.name}</li>
    <li>{country.country}</li> -->