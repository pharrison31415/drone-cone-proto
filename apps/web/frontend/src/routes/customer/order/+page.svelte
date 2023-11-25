<body>
    <div class = "parent">
    <div id = "order" class = "child">
        <h1>Order Here</h1>
        <form on:submit|preventDefault={submitCone}>
            <select bind:value={selectedToppings} class="select1">
                {#each toppings as toppings }
                <option value={toppings}> {toppings}</option> 
                {/each}
            </select>
        <br>    
            <select bind:value={selectedIcecream} class="select1">
                {#each icecreamFlavor as flavor }
                <option value={flavor}> {flavor}</option>
                {/each}
            </select>
        <br>
            <select bind:value={selectedConeType} class="select1">
                {#each coneType as cone }
                <option value={cone}> {cone}</option> 
                {/each}
            </select>
        <br>
            <button type="submit"> Add to Cart </button>
        </form>
    </div>
    <div id = "cart" class='child' bind:this={element}>
        {#each cart as cone }
        <div class = "cone">
        <p>Topping: {cone.toppingType}</p>  
        <p>Ice Cream Flavor: {cone.iceCreamType}</p> 
        <p>Cone: {cone.coneType}</p> 
        </div>  
        {/each} 
    </div>
    </div>

    <br>
    <button on:click={submitOrder}> Submit Order </button>
    <br>

    <div class = "parent2" id ="customer_info">
        <div class = "child2">
        <form on:submit={nothing}>
            <label for="line1">Enter Address:</label><br>
            <input bind:value={address["lineOne"]} placeholder= "Street Address: Line 1"><br>
            <input bind:value={address["lineTwo"]} placeholder= "Line 2 (optional)"><br>
            <input bind:value={address["city"]} placeholder= "City"><br>
            <select bind:value={address["state"]}>
                {#each states as state }
                <option value={state}> {state}</option> 
                {/each}
            </select><br>
            <input bind:value={address["zipCode"]} placeholder= "zipCode"><br>
            <button type = "submit"> see address inputs </button>
        </form>
        </div>
    </div>

    <br>

    <div class ="parent2" id="customer_payment">
        <div class = "child2">
            <form on:submit={nothing}>
                <label for="line1">Enter Payments:</label><br>
                <input bind:value={billing["creditCard"]} placeholder= "Credit Card"><br>
                <input bind:value={billing["ccv"]} placeholder= "cvv"><br>
                <input bind:value={billing["expireDate"]} placeholder= "Expired Date"><br>

                <label for="line1">Billing Info:</label><br>
                <input bind:value={billing["line1"]} placeholder= "Street Address: Line 1"><br>
                <input bind:value={billing["line2"]} placeholder= "Line 2 (optional)"><br>
                <input bind:value={billing["city"]} placeholder="City" ><br>
                <select bind:value={billing["state"]}>
                    {#each states as state }
                    <option value={state}> {state}</option> 
                    {/each}
                </select><br>
                <input bind:value={billing["zipCode"]} placeholder="zipCode" ><br>
            </form>
            </div>     
    </div>
</body>





<script>
	import { onMount } from "svelte";
    import { Order } from "./OrderClass.js";
    import { Cone } from "./ConeClass.js";
    import { afterUpdate} from 'svelte';

    /*Creates a new order object once enter into the page*/
    onMount(createOrderClass)
    let order;
    let cart = [];

    function createOrderClass(){
        order = new Order()   
    }

    //Variables for flavor, cone, toppings, and submitting data base testing
    let icecreamFlavor = ["Select a Ice Cream Flavor"];
    let coneType = ["Select a Cone"];
    let toppings = ["Select a Topping"];

    //Variables for new-order/ POST function to check inputs
    let address = {
        lineOne: "", 
        lineTwo: "", 
        city:"", 
        state:"", 
        zipCode:""
    };

    let price = 0;
    let cost = 0;
    let created = new Date().getTime();
    let status = "Recieved"

    //Setters variables for selected items for HTML
    let selectedIcecream;
    let selectedConeType;
    let selectedToppings;

    // API Variables
    let coneUrl = "http://localhost:8000/api/cone-types/";
    let iceCreamUrl = "http://localhost:8000/api/ice-cream-types/";
    let topUrl = "http://localhost:8000/api/topping-types/";

    // MISC Variables
    let states = ["ID","UT"];
    let billing = {
        creditCard:"",
        cvv:"",
        expireDate:'',
        lineOne: "", 
        lineTwo: "", 
        city:"", 
        state:"", 
        zipCode:""
    }
    let element;


    //Once a cone is made by user, create cone object and add to order
    function submitCone(){
        if (checkOrderInputs()){
        let cone = new Cone(selectedIcecream,selectedConeType,selectedToppings);
        order.addtoOrder(cone);
        cart = order.getCart();

        console.log(order);
        }
    }
    // nothing
    function nothing(){
        console.log(address)
    }

    //Check Inputs for Cones
    function checkOrderInputs(){
        if (selectedConeType == 'Select a Cone' || selectedIcecream == "Select a Ice Cream Flavor" || selectedToppings =='Select a Topping'){
            console.log("Your options")
            return false
        }
        return true
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
    };
    
    //Scroll Cart	
	// Either afterUpdate()
	afterUpdate(() => {
		if(cart) scrollToBottom(element);
    });
	
	$: if(cart && element) {
		scrollToBottom(element);
	}

    const scrollToBottom = async (node) => {
        node.scroll({ top: node.scrollHeight, behavior: 'smooth' });
    }; 

    //Remove cone from list
    function removeCone(){
        order.removeCart()
        cart = order.getCart();
    }
	

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

<style>
    body{
        background-color: rgb(180, 255, 255);
        margin: 0%;
    }

    p{
        margin: 0%;
    }

    input {
        border: 1px solid;
        padding: 0.3em;
        width: 300px;
    }

    label {
        font-size: large;
    }

    #cart {
        text-align: center;
        overflow:auto;
        height: 350px;
        border: 3px solid rgb(255, 0, 0);


    }

    #order {
        text-align: center;

    }

    #customer_info {
        text-align: center;

    }

    #customer_payment {
        text-align: center;

    }

    .select1{
        margin: 10px;
        height: 50px;
        width: 250px;
        text-align: center;
        font-size: medium;
    }

    .cone{
        border: 3px solid black;
    }

    .parent{
        border: 3px solid black;
        grid-template-columns: 1fr;
        width: 100%;
        height: 350px;
        display: grid;
    }

    .child {
        display: inline-block;
    }

    .parent2{
        border: 3px solid black;
        grid-template-columns: 1fr;
        width: 100%;
        height: 300px;
        display: grid;
    }

    .child2 {
        display: inline-block;
    }

    .child3{
        width: 100%;
        height: 33%;
    }
    

</style>