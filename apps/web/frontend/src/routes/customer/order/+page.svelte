<body>
<script></script>
<div>
    <!-- -->
    <form on:submit|preventDefault={submitCone}>
        <select bind:value={selectedIcecream}>
            {#each icecreamFlavor as flavor }
            <option value={flavor}> {flavor}</option> 
            {/each}
        </select>

        <select bind:value={selectedConeType}>
            {#each coneType as cone }
            <option value={cone}> {cone}</option> 
            {/each}
        </select>

        {#each toppings as topping }
            <label><input type="checkbox" value = {topping} bind:group={selectedToppings}> {topping} </label>
        {/each}

        <button type="submit"> Add to Cart </button>
    </form>
</div>
</body>





<script>
	import { onMount } from "svelte";
    import { Order } from "./OrderClass.js";
    import { Cone } from "./ConeClass.js";
    
    onMount(createOrderClass)
    /*Creates a new order object once enter into the page*/
    let order;

    function createOrderClass(){
        order = new Order()   
    }

    //Variables for flavor, cone, toppings
    let icecreamFlavor = ["Choose Icecream Flavor"];
    let coneType = ["Choose Cone Type"];
    let toppings = [];

    //Setters variables for selected items
    let selectedIcecream;
    let selectedConeType;
    let selectedToppings = [];

    //Once cone is made by user, create cone object and add to order
    function submitCone(){
        let cone = new Cone(selectedIcecream,selectedConeType,selectedToppings)
       
        order.addtoOrder(cone)

        console.log(order)

        
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
            coneType.push(item["name"]);
            coneType = coneType
        }
    });

    onMount(async() => {
        const response = await fetch (iceCreamUrl)
        const infoJson = await response.json()

        for(let item of infoJson["iceCreamTypes"]){
            icecreamFlavor.push(item["name"]);
            icecreamFlavor = icecreamFlavor
        }
    });

    onMount(async() => {
        const response = await fetch (topUrl)
        const infoJson = await response.json()
        
        for(let item of infoJson["toppingTypes"]){
            toppings.push(item["name"]);
            toppings = toppings
        }

    });
</script>