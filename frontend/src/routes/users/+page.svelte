<script>
    export let data;
    console.log(data)
</script>

<main>
    <h1>Users</h1>

    <ul>
        {#each data.user_info as user}
            <li>{user.name}</li>
        {/each}
    </ul>
    
    
</main>