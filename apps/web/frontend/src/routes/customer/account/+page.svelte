<script>
	import { onMount } from "svelte";

    let userUrl = "http://localhost:8000/api/private-customer-data/";
    let orderUrl = "http://localhost:8000/api/my-addresses/";

    let status = 'loading';
    let success = false
    let firstName = ''
    let lastName = ''
    let addresses = []

    function getInfo(){
        getPrivateData()
        getAddresses()
    }

    function getPrivateData(){

        status = '';
        fetch(userUrl, {credentials: "include", method: 'GET'})
            .then(resp => resp.json())
            .then(json => {
                if (json.hasOwnProperty('error')) {
                    throw json.error;
                }
                else{
                    firstName = json.firstName
                    lastName = json.lastName
                    status = ''
                }
            })
            .catch(err => {
                status = err;
            })
            .finally( () => {
                if (status == ''){
                    success = true
                }
            })
    }

    function getAddresses(){
        fetch(orderUrl, {credentials: "include", method: 'GET'})
            .then(resp => resp.json())
            .then(json => {
                if (json.hasOwnProperty('error')) {
                    throw json.error;
                }
                else{
                    addresses = json.addresses
                    status = ''
                }
            })
            .catch(err => {
                status = err;
            })
            .finally( () => {
                if (status == ''){
                    success = true
                }
            })
    }

    onMount( () => { getInfo() })

</script>

<h1>Account</h1>
{#if !success}
    <div>
        <p>{status}</p>
    </div>
{:else}
    <div>
        <p>Name: {firstName} {lastName}</p>
    </div>
    <h2>My Addresses</h2>
    {#if addresses = []}
    <p>No addresses found</p>
    {:else}
    {#each addresses as address}
        <h3>Address {address.id}</h3>
        <p>{address.lineOne}</p>
        {#if address.lineTwo != ""}
        <p>{address.lineTwo}</p>
        {/if}
        <p>{address.city}</p>
        <p>{address.state}</p>
        <p>{address.zipCode}</p>
    {/each}
    {/if}
{/if}
<style>
    h1 {
        text-align: center;
    }

    p {
        padding-left: 10px;
    }
    
    #order {
        border: solid black;
        display: flex;
        flex-shrink: 0;
    }

    .cone_details {
        width: -webkit-fill-available;
    }

    .cone_details > p {
        padding-left: 25px;
    }

    li > p {
        text-align: left;
        margin: 5px;
    }
    
    ol > li {
        text-align: left;
        margin: 10 px;
        padding: 5px;
    }
    

    h3 {
        padding-left: 20px;
    }

    .add_to_cart {
        padding: 10px;
        flex-shrink: 0;
        display: flex;
        flex-direction: column;
    }

    span {
        align-self: center;
    }
    

    button {
        align-self: flex-end;
        width: fit-content;
    }

</style>