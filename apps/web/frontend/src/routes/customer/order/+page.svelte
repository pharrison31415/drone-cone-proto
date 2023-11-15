<body>
<script></script>
<div>
    <!-- -->
    <form on:submit|preventDefault={submitCone}>
        <select bind:value={selectedIcecream}>
            {#each icecreamFlavor as flavor }
            <option value={flavor["name"]}> {flavor["name"]}</option>
            {/each}
        </select>
    <br>
        <select bind:value={selectedConeType}>
            {#each coneType as cone }
            <option value={cone["name"]}> {cone["name"]}</option> 
            {/each}
        </select>
    <br>
        {#each toppings as topping }
            <label><input type="checkbox" value = {topping["name"]} bind:group={selectedToppings}> {topping["name"]} </label>
        {/each}
    <br>
        <button type="submit"> Add to Cart </button>
    </form>

    <button on:click={submitOrder}> Order </button>
</div>
</body>





<script>
	import { onMount } from "svelte";
    import { Order } from "./OrderClass.js";
    import { Cone } from "./ConeClass.js";

    /*Creates a new order object once enter into the page*/
    onMount(createOrderClass)
    let order;

    function createOrderClass(){
        order = new Order()   
    }

    //Variables for flavor, cone, toppings, and submitting data base testing
    let icecreamFlavor = [];
    let coneType = [];
    let topping = "No topping";

    //Variables for new-order/ POST
    let address = {line1: "123 address" , line2: "" , city:"Logan", state:"UT", zipCode:"84321"};
    let price = 0;
    let cost = 0;
    let created = new Date().getTime();
    let status = "Recieved"

    //Setters variables for selected items for HTML
    let selectedIcecream;
    let selectedConeType;
    let selectedToppings;

    //Once a cone is made by user, create cone object and add to order
    function submitCone(){
        let cone = new Cone(selectedIcecream,selectedConeType,topping)
       
        order.addtoOrder(cone)

        console.log(order.getCart())
    }

    //POST order into database
    async function submitOrder(){
        let orderURL = "http://localhost:8000/api/new-order/"
    
        fetch(orderURL,{
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                cones: order.getCart(), // array of cones
                id: 1,
                price: price,
                cost: cost,
                created: created,
                address_id: address,
                status: status
            })
        })
        .then((response) => response.json())
        .then((json) => console.log(json))
    }

    //API CALLS **TODO move to seperate file**

    let coneUrl = "http://localhost:8000/api/cone-types/"
    let iceCreamUrl = "http://localhost:8000/api/ice-cream-types/"
    let topUrl = "http://localhost:8000/api/topping-types/"

    //**** Inventory Status ****
    onMount(async() => {
        const response = await fetch (coneUrl)
        const infoJson = await response.json()

        for(let item of infoJson["coneTypes"]){
            coneType.push(item);
            coneType = coneType
        }
    });

    onMount(async() => {
        const response = await fetch (iceCreamUrl)
        const infoJson = await response.json()

        for(let item of infoJson["iceCreamTypes"]){
            icecreamFlavor.push(item);
            icecreamFlavor = icecreamFlavor
        }
    });

    onMount(async() => {
        const response = await fetch (topUrl)
        const infoJson = await response.json()
        
        for(let item of infoJson["toppingTypes"]){
            toppings.push(item);
            toppings = toppings
        }

    });
</script>