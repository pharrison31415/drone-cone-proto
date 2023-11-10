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
    
    /*Creates a new order object once enter into the page*/
    let order;
    onMount(createOrderClass)
    function createOrderClass(){
        order = new Order()    
    }

    //Variables for flavor, cone, toppings
    let icecreamFlavor = ["Chocolate","Vanilla","Strawberry" ]
    let coneType = ["Waffle","Cup","Regular" ]
    let toppings = ["sprinkles","choco syrup", "strawberry syrup", "nuts"]

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
    

    
</script>