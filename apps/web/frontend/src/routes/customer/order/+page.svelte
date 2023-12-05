<body>
    <div class = "parent">
    <div id = "order" class = "child">
        <h1>Order Here</h1>
        <form on:submit|preventDefault={submitCone}>
            <label for="topping">Select a Topping: </label><br>
            <select bind:value={selectedToppings} class="select1">
                {#each toppings as toppings }
                <option value={toppings}> {toppings}</option> 
                {/each}
            </select>
        <br>
            <br><label for="iceCreamFlavor">Select a Ice Cream Flavor: </label><br>
            <select bind:value={selectedIcecream} class="select1">
                {#each icecreamFlavor as flavor }
                <option value={flavor}> {flavor}</option>
                {/each}
            </select>
        <br>
            <br><label for="iceCreamFlavor">Select a Cone: </label><br>
            <select bind:value={selectedConeType} class="select1">
                {#each coneType as cone }
                <option value={cone}> {cone}</option> 
                {/each}
            </select>
        <br>
        <br>
            <button type="submit" class="addCart"> Add to Cart </button>
            <h3>{error}</h3>
        </form>
    </div>
    <div id = "cart" class='child' bind:this={element}>
        <h1>Your Cart:</h1>
        {#each cart as cone }
        <div class="parent3">
            <div class = "child3">
                <h4>Ice Cream Description:</h4>
                <p><strong>Topping: </strong>{cone.toppingType}</p>
                <p><strong>Cream Flavor: </strong>{cone.iceCreamType}</p>
                <p><strong>Cone: </strong>{cone.coneType}</p>
                <p><strong>Price:</strong> $2.50</p>
                <br>
            </div>
            <div class = "child3">
                <button class = "delete_button" on:click={removeCone(cone.id)}></button>
            </div>
        </div>  
        {/each}
    </div>
    </div>

  

    <div class = "parent2" id ="customer_info">
        <div class = "child2">

            <h1> Delivery Address</h1>

            <form on:submit={nothing}>
            <!--
            <div class="form__group field">
                <label for="Line One" class="form__label"> Street Line 1:</label>
                <input type="input" class="form__field" placeholder="Street Line 1" bind:value={address["lineOne"]}/>
            </div>
            <div class="form__group field">
                <label for="Line One" class="form__label"> Line 2:</label>
                <input type="input" class="form__field" placeholder="Line 2 (optional)" bind:value={address["lineTwo"]}/>
            </div>
            <div class="form__group field">
                <label for="Line One" class="form__label"> City:</label>
                <input type="input" class="form__field" placeholder="City" bind:value={address["city"]}/>
            </div>
            <select bind:value={address["state"]} class="select2">
                {#each states as state }
                <option value={state}> {state}</option> 
                {/each}
            </select><br>
            <div class="form__group field">
                <label for="Line One" class="form__label"> Zip Code:</label>
                <input type="number" class="form__field" placeholder="Zip Code" bind:value={address["zipCode"]} on:input={handleInput}/>
            </div>
        -->
            </form>
        </div>
    </div>

    <div class ="parent2__paymentInfo" id="customer_payment">
        <div class = "child2">
            <h1> Payment Information</h1>
            <br>
            <form on:submit={nothing}>
                <h2> Credit Card Information:</h2>
                <div class="form__group field">
                    <label for="cc number" class="form__label"> Credit Card Number</label>
                    <input type="input" class="form__field" placeholder="Credit Number" bind:value={billing["creditCard"]} on:input={handleInput4}/>
                </div>
                <div class="form__group field">
                    <label for="cvv" class="form__label"> CVV:</label>
                    <input type='input' class="form__field__cvv" placeholder="cvv" bind:value={billing["cvv"]}  on:input={handleInput3}/>
                </div>
                <div class="form__group field">
                    <label for="expireDate" class="form__label"> Expire Date</label>
                    <input type="Month" class="form__field__ex" placeholder="MM/YY" bind:value={billing["expireDate"]}/>
                </div>
                <br>
                <h2> Billing Address:</h2>
                <div class="form__group field">
                    <label for="lineOne" class="form__label"> Street Line 1:</label>
                    <input type="input" class="form__field" placeholder="Street Line 1" bind:value={billing["lineOne"]}/>
                </div>
                <div class="form__group field">
                    <label for="lineTwo" class="form__label"> Line 2:</label>
                    <input type="input" class="form__field" placeholder="Street Address: Line 1" bind:value={billing["lineTwo"]}/>
                </div>
                <div class="form__group field">
                    <label for="city" class="form__label"> City:</label>
                    <input type="input" class="form__field" placeholder="City" bind:value={billing["city"]}/>
                </div>
                <select bind:value={billing["state"]} class="select2">
                    {#each states as state }
                    <option value={state}> {state}</option> 
                    {/each}
                </select><br>
                <div class="form__group field">
                    <label for="zipCode" class="form__label"> Zip Code:</label>
                    <input type='input' class="form__field" placeholder="Zip Code" bind:value={billing["zipCode"]}  on:input={handleInput2}/>
                </div>
            </form>
            </div>     
    </div>
    <div class="parent2_orderButton_div">
        <br>
        <p class='total'>Your Total is {USDollar.format(price)}<p>
        <h3>{check}</h3>
        <h3>{inputError}</h3>
        <button on:click={submitOrder} class="orderButton"> Submit Order </button>
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
    let states = ["Idaho","Utah"];
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
    let element = "";
    let id = 0;
    let error = " ";
    let inputError = " ";
    let check = " ";
    let success = false;


    //Once a cone is made by user, create cone object and add to order
    function submitCone(){
        if (checkOrderInputs()){
        let cone = new Cone(id, selectedIcecream,selectedConeType,selectedToppings);
        id++;
        order.addtoOrder(cone);
        cart = order.getCart();
        console.log(cart.length);
        price = cart.length * 2.50;
     }
    }
   
    //Check Inputs for Cones
    function checkOrderInputs(){
        if (selectedConeType == 'Select a Cone' || selectedIcecream == "Select a Ice Cream Flavor" || selectedToppings =='Select a Topping'){
            error = "One of your options is missing";
            return false
        }
        error = " ";
        return true
    }

    function checkAddressInputs(){

        /*
        if (address["lineOne"] === ''|| address["city"]=== '' || address["state"] ===''|| address['zipCode'] === ''){
            inputError = "You're address is missing required inputs"
            return false
        }

        else if (billing["lineOne"] == ''|| billing["city"]== '' || billing["state"] == ''|| billing['zipCode'] == ''){
            inputError = "You're billing address is missing required inputs"
            return false
        }

        else if (billing['creditCard'] == ''){
            inputError = "You're creditCard inputs are incorrect"
            return false
        }

        else if (billing['cvv'] == ''){
            inputError = "You're cvv inputs are incorrect"
            return false
        }

        else{
            inputError = ' '
            return true
        }
        */
       return true
    }
    
// ****************************************** Cart/Order Usage  ******************************************	
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
    function removeCone(id){
        order.removeCone(id)
        cart = order.getCart();
        price = cart.length * 2.50;
    };
	
      //POST order into database
    async function submitOrder(){
        let orderURL = "http://localhost:8000/api/new-customer-order/"

        if(checkAddressInputs()){
            fetch(orderURL,{
                method: 'POST',
                credentials: 'include',
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    cones: order.getCart(), // array of cones
                    id: 1,
                    price: price,
                    cost: cost,
                    created: created,
                    addressId: 1,
                    status: status
                })
            })
            .then((response) => response.json())
            .then((json => {check = json.message , console.log(json)}))
        }
    };

//****************************************** Inventory Status ******************************************
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

//*************************MISC FUNCTION*************************/

    function nothing(){
        console.log('')
    }

    // Format the price above to USD using the locale, style, and currency.
    let USDollar = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    });

    function handleInput(event) {
    // Ensure only digits are entered
        const sanitizedValue = event.target.value.replace(/\D/g, '');
    // Limit the input to 5 digits
        address['zipCode'] = sanitizedValue.slice(0, 5);
  }

  function handleInput2(event) {
    // Ensure only digits are entered
        const sanitizedValue = event.target.value.replace(/\D/g, '');
    // Limit the input to 5 digits
        billing['zipCode'] = sanitizedValue.slice(0, 5);
  }

  function handleInput3(event) {
    // Ensure only digits are entered
        const sanitizedValue = event.target.value.replace(/\D/g, '');
    // Limit the input to 3 digits
        billing['cvv'] = sanitizedValue.slice(0,3);
  }

  function handleInput4(event) {
    // Ensure only digits are entered
        const sanitizedValue = event.target.value.replace(/\D/g, '');
    // Limit the input to 16 digits
        billing['creditCard'] = sanitizedValue.slice(0,16);
  }


</script>

<style>
    body{
        background-color: rgb(180, 255, 255);
        margin: 0%;
        font-family: "Poppins", sans-serif;
    }

    p{
        margin: 0%;
        font-family: 'Arial', sans-serif;
        font-size: 16px;
        color: #333;
        text-align: left;
        padding-left: 20px;

    }

    h1{
        text-align: center;
    }

    h2{
        text-align: center;
    }

    h3{
        text-align: center;
        color: red;
    }

    h4{
        text-align: center;
    }

    h5{
        margin: 0%;
        padding-left: 50px;
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
        overflow:auto;
        height: 550px; 
        background-color: aquamarine;

    }

    #cart:hover {
        overflow:auto;
        height: 550px; 
        background-color: aquamarine;
        box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;
    }

    #order {
        text-align: center;
    }

    #order:hover{
        text-align: center;
        box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;

    }

    #customer_info {
        text-align: center;

    }

    #customer_payment {
        text-align: center;
        height: 800px;
    }

    .select1{
        margin: 10px;
        height: 50px;
        width: 250px;
        text-align: center;
        font-size: medium;
        border-radius: 10px;
    }

    .select2{
        margin: 10px;
        height: 50px;
        width: 250px;
        text-align: center;
        font-size: medium;
        border-radius: 10px;
    }

    .parent{
        grid-template-columns: 1fr 1fr;
        width: 100%;
        height: 550px;
        display: grid;
    }

    .parent:hover{
        grid-template-columns: 1fr 1fr;
        width: 100%;
        height: 550px;
        display: grid;
    }

    .child {
        display: inline-block;
        border: dotted 4px;
        border-top: none;
    }

    .parent2{
        grid-template-columns: 1fr;
        width: 100%;
        height: 500px;
        display: grid;
        border-top: dotted 4px;

    }

    .parent2:hover{
        grid-template-columns: 1fr;
        width: 100%;
        height: 500px;
        display: grid;
        border-top: dotted 4px;
        box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;

    }

    .parent2__paymentInfo{
        grid-template-columns: 1fr;
        width: 100%;
        height: 650px;
        display: grid;
        border-top: dotted 4px;
    }

    .child2 {
        display: inline-block;
    }

    .parent3{
        border: 3px solid rgb(0, 0, 0);
        grid-template-columns: 1fr 1fr;
        width: 100%;
        height: 30%;
        display: grid;

    }

    .parent3:hover{
        border: 3px solid rgb(0, 0, 0);
        grid-template-columns: 1fr 1fr;
        width: 100%;
        height: 30%;
        display: grid;
        box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;

    }

    .child3{
        border: 1px solid rgb(0, 0, 0);
        background-color: rgb(0, 255, 242);
    }

    .child3:hover{
        border: 1px solid rgb(0, 0, 0);
        background-color: rgba(159, 255, 80, 0.607);
        box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;

    }

    .delete_button{
        text-align: none;
        background: url("/211836_trash_icon.png");
        width: 48px;
        height: 48px;
        border: none;    
        margin-left: 45%;
    }

    .form__group{
        width: 75%;
        height: 60px;
        margin-left: 15%;
        margin-bottom: 10px;
        margin-top: 5px;
        text-align: center;
        grid-template-rows: 100px 2;
        display: grid;
    }

    .form__field{
        font-size: large;
        width: 500px;
        margin-left: 22%;
        border-radius: 10px;
    }

    .form__field__cvv{
        font-size: large;
        width: 65px;
        margin-left: 22%;
        border-radius: 10px;
    }

    .form__field__ex{
        font-size: large;
        width: 150px;
        margin-left: 22%;
        border-radius: 10px;
    }

    .form__field:focus::-webkit-input-placeholder{
        opacity: 0;
    }

    .form__label{
        width: 16rem;
        font-size: medium;
        margin-left: 22%;
        text-align: left;
    }

    .orderButton{
        width: 200px;
        height: 100px;
        font-size: x-large;
        border-radius: 40px;
        background-color: red;
        margin-left: 43%;
        font-weight: bold;

    }

    .orderButton:hover{
        width: 200px;
        height: 100px;
        font-size: x-large;
        border-radius: 40px;
        background-color: yellow;
        margin-left: 43%;
        font-weight: bold;
    }

    .parent2_orderButton_div{
        grid-template-columns: 1fr;
        width: 100%;
        height: 450px;
        display: grid;
    }

    .addCart{
        width: 200px;
        height: 50px;
        font-size: x-large;
        border-radius: 40px;
        background-color: rgb(0, 255, 21);
        font-weight: bold;

    }

    .addCart:hover{
        width: 200px;
        height: 50px;
        font-size: x-large;
        border-radius: 40px;
        background-color: yellow;
        font-weight: bold;
    }

    .total{
        font-size: xx-large;
        color: red;
        text-align: center;
    }
</style>