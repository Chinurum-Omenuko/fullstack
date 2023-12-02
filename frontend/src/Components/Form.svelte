<script lang="ts">
    let name: any;
    let country: any;

    const submit = async () => {
        const url = 'http://127.0.0.1:8000/countries/';
        const headers = {
            'Content-Type': 'application/json'
        };
        const body = JSON.stringify({name, country});

        const response = fetch(url, {
            method: 'POST',
            headers: headers,
            body: body
        });

        
    }

</script>

<form on:submit|preventDefault={submit} >
    <div class="inner">
        <label for="name">Name</label>
        <input type="text"  id="name" bind:value={name}>
        <label for="country">Country</label>
        <input type="text"  id="country_input" bind:value={country}>
        <button type="submit">Submit</button>
    </div>

</form>

<style lang="scss">
    form{
        .inner{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            
            margin: 0px 5em;
            height: inherit;
        }


        height: 30vh;
    }
</style>