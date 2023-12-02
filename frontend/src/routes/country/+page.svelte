<script lang="ts">
	import Form from '../../Components/Form.svelte';
    import { page } from '$app/stores';
    import { goto } from '$app/navigation';


    const viewcountries = () =>{
        goto('/country/viewcountries')
    }

    // export let data;
    
</script>

<main class="container">
    <h1>country</h1>
    <h2>Tell me where you are from: </h2>

    <Form />

    <button on:click={viewcountries}>
        View Submissions
    </button>

</main>

<style>
    main{
        text-align: center;
    }

    button a{
        color: whitesmoke;
    }
</style>