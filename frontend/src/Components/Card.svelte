<script lang="ts">
    export let name: string;
    export let country: string;

    let card;

    function clickalert(){
        alert('clicked')
    }
</script>

<article bind:this={card} on:click={clickalert} on:keydown={clickalert}>
    <header>
        <h3>{name}</h3>
    </header>
    <div class="body">
        <p>{country}</p>
    </div>
</article>

<style>

</style>