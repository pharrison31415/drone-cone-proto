<script>
    import { onMount } from 'svelte'
    const url = "http://localhost:8000/api"

    let username = "";
    let first_name = "";
    let last_name = "";
    let addresses = [];
    let error = '';

    let orders = [];

    let street_address = "";
    let city = "";
    let state = "";
    let zip = "";

    let showDialogClickError = "";

    let addAddress_dialog;

    let removeBttn_height = 0;

    let doneLoading = false;

    onMount(() => {
        get_privateData();
        get_myAddresses();
        get_myOrders();
        addAddress_dialog = document.getElementById("addAddress_dialog");
    });

    async function get_privateData() {
        fetch(url + "/private-customer-data/", {method: "GET", credentials: "include"})
            .then((response) => response.json())
            .then((json) => {
                if (json.success == false) {
                    showDialogClickError = "There was an error getting user data: " + json.message
                }
                else if (json.success == true) {
                    username = json.user.username;
                    first_name = json.user.firstName;
                    last_name = json.user.lastName;
                }
                else {
                    showDialogClickError = "There was an error"
                }
                doneLoading = true;
            });
    }

    async function get_myAddresses() {
        fetch(url + "/my-addresses/", {method: "GET", mode: 'cors', credentials: 'include'})
            .then((response) => response.json())
            .then((json) => {
                if (json['success'] == false) {
                    error = "There was an error: " + json['message'];
                }
                else {
                    addresses = json['addresses'];
                }
            })
    }

    async function get_myOrders() {
        fetch(url + "/past-orders/", {method: "GET", credentials: 'include'})
            .then((response) => response.json())
            .then((json) => {
                if (json['success'] == false) {
                    error = "There was an error getting your orders: " + json['message'];
                }
                else if (json['success'] == true) {
                    orders = json['orders'];
                }
                else {
                    error = "There was an error getting your orders"
                }
            });
    }

    async function post_newAddress() {
        fetch(url + '/add-address/', {method: 'POST', credentials: "include", body: JSON.stringify({lineOne: street_address, lineTwo: "", city: city, state: state, zipCode: zip})})
            .then((response) => response.json())
            .then((json) => {
                if (json['success'] == true) {
                    console.log('post was successful');
                    get_myAddresses();
                }
                else {
                    console.log('there was an error');
                    showDialogClickError = "There was an error when adding the address: " + json['message'];
                }
            });
    }

    async function deleteAddress(addressId) {
        fetch(url + '/delete-address/', {method: 'POST', credentials: 'include', body: JSON.stringify({addressId: addressId})})
            .then((response) => response.json())
            .then((json) => {
                if (json['success'] == true) {
                    console.log('delete address, addressID: ' + addressId + ' was successful');
                    get_myAddresses();
                }
                else {
                    console.log('there was an error deleting the address');
                    showDialogClickError = 'There was an error when deleting the address: ' + json['message'];
                }
            });
    }

    async function markAsDelivered(order) {
        fetch(url + '/order-delivered/', {method: 'POST', credentials: 'include'})
            .then((response) => response.json())
            .then((json) => {
                console.log(json);
                if (json.success == true) {
                    get_myOrders();
                }
            });

    }

    const showDialogClick = (asModal = true) => {
		try {
			addAddress_dialog[asModal ? 'showModal' : 'show']();
		} catch(e) {
            showDialogClickError = e;
		}  
	};

    const closeClick = () => {
        addAddress_dialog.close();
	};

    const submitClick = () => {
        if (street_address.length > 0 && city.length > 0 && state.length > 0 && zip.length > 0) {
            post_newAddress();
            street_address = "";
            city = "";
            state = "";
            zip = "";
            closeClick();
        }
    }

    const signIn = () => {
        window.location.href = "/customer/sign_in"
    }

    const placeOrder = () => {
        window.location.href = "/customer/order"
    }


</script>

<body>
    <dialog id="addAddress_dialog">
        <h3>Add New Address</h3>
        <form>
            <label for="street">Street address:</label>
            <input type="text" id="street" name="street" bind:value={street_address} placeholder="Street Address" required>

            <label for="city">City:</label>
            <input type="text" id="city" name="city" bind:value={city} placeholder="City" required>

            <label for="state">State:</label>
            <input type="text" id="state" name="state" bind:value={state} placeholder="State" required>

            <label for="zip">Zip Code:</label>
            <input type="text" id="zip" name="zip" bind:value={zip} placeholder="Zip Code" required>

            <div>
                <button type="submit" on:click={submitClick}>Add Address</button>
                <button type="reset" on:click={closeClick}>Cancel</button>
            </div>
        </form>
    </dialog>

    <h1>Welcome{#if username != ""}, {username}{/if}</h1>

    {#if !doneLoading}
        <h2>Loading...</h2>
        <p>Please wait</p>
    {/if}

    <h2>{error}</h2>
    <p>{showDialogClickError}</p>

    {#if error != ""}
        <p>Please make sure you are signed in</p>
        <button on:click={signIn}>Sign in</button>
    {/if}


    {#if first_name != "" && last_name != ""}
        <p>Name: {first_name} {last_name}</p>
        <p style="margin: 1px;">Addresses:</p>

        {#if addresses.length == 0}
            <h4 style="margin: 5px;">You have no Addresses, please add one</h4>
        {:else}
            <div id="addresses">
                {#each addresses as address, index}
                    <div class="address">Address #{index+1}: 
                        <p>{address.lineOne}{#if address.lineTwo != ""}, {address.lineTwo}{/if},</p>
                        <p>{address.city}, {address.state} {address.zipCode}</p>

                        <button id='removeAddress' on:click={deleteAddress(address.id)}>
                            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 25 25" fill="none">
                                <g clip-path="url(#clip0_8_8)">
                                    <path d="M6.25001 19.7917C6.25001 20.9427 7.1823 21.875 8.33334 21.875H16.6667C17.8177 21.875 18.75 20.9427 18.75 19.7917V7.29167H6.25001V19.7917ZM19.7917 4.16667H16.1458L15.1042 3.125H9.89584L8.85418 4.16667H5.20834V6.25H19.7917V4.16667Z" fill="black"/>
                                </g>
                                <defs>
                                    <clipPath id="clip0_8_8">
                                        <rect width="25" height="25" fill="white"/>
                                    </clipPath>
                                </defs>
                            </svg>
                            <p>Remove</p>
                        </button>

                    </div>
                {/each}
            </div>

        {/if}

        <div id="addAddress">
            <button on:click={() => showDialogClick(true)} id="addAddress-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
                    <g clip-path="url(#clip0_5_2)">
                        <path d="M16 29C13.4288 29 10.9154 28.2376 8.77759 26.8091C6.63975 25.3807 4.97351 23.3503 3.98957 20.9749C3.00563 18.5995 2.74819 15.9856 3.2498 13.4638C3.75141 10.9421 4.98953 8.6257 6.80762 6.80762C8.6257 4.98953 10.9421 3.75141 13.4638 3.2498C15.9856 2.74819 18.5995 3.00563 20.9749 3.98957C23.3503 4.97351 25.3807 6.63975 26.8091 8.77759C28.2376 10.9154 29 13.4288 29 16C29 19.4478 27.6304 22.7544 25.1924 25.1924C22.7544 27.6304 19.4478 29 16 29ZM16 5.00001C13.8244 5.00001 11.6977 5.64514 9.88873 6.85384C8.07979 8.06254 6.66989 9.7805 5.83733 11.7905C5.00477 13.8005 4.78693 16.0122 5.21137 18.146C5.63581 20.2798 6.68345 22.2398 8.22183 23.7782C9.76021 25.3166 11.7202 26.3642 13.854 26.7886C15.9878 27.2131 18.1995 26.9952 20.2095 26.1627C22.2195 25.3301 23.9375 23.9202 25.1462 22.1113C26.3549 20.3023 27 18.1756 27 16C27 13.0826 25.8411 10.2847 23.7782 8.22183C21.7153 6.15893 18.9174 5.00001 16 5.00001Z" fill="black"/>
                        <path d="M16 23C15.7348 23 15.4804 22.8946 15.2929 22.7071C15.1054 22.5196 15 22.2652 15 22V10C15 9.73478 15.1054 9.48043 15.2929 9.29289C15.4804 9.10536 15.7348 9 16 9C16.2652 9 16.5196 9.10536 16.7071 9.29289C16.8946 9.48043 17 9.73478 17 10V22C17 22.2652 16.8946 22.5196 16.7071 22.7071C16.5196 22.8946 16.2652 23 16 23Z" fill="black"/>
                        <path d="M22 17H10C9.73478 17 9.48043 16.8946 9.29289 16.7071C9.10536 16.5196 9 16.2652 9 16C9 15.7348 9.10536 15.4804 9.29289 15.2929C9.48043 15.1054 9.73478 15 10 15H22C22.2652 15 22.5196 15.1054 22.7071 15.2929C22.8946 15.4804 23 15.7348 23 16C23 16.2652 22.8946 16.5196 22.7071 16.7071C22.5196 16.8946 22.2652 17 22 17Z" fill="black"/>
                    </g>
                    <defs>
                        <clipPath id="clip0_5_2">
                        <rect width="32" height="32" fill="white"/>
                        </clipPath>
                    </defs>
                </svg>
                Add new Address
            </button>
        </div>

        <h2>Recent Order:</h2>

        {#if orders.length == 0}
            <h4 style="margin: 5px;">You have no orders, please place one</h4>
            <button on:click={placeOrder}>Place Order</button>
        {:else}
            {#each orders as order}
                <div id="orders">
                    <!-- for each order do this -->
                    <div id="order">
                        <div class="cone_details">
                            <h3>Order #{order.id}</h3>
                            <p>Order placed: {new Date(order.created).toLocaleString()}</p>
                            <p># of cones: {order.cones.length}</p>
                            <p>Total Cost: ${order.price}</p>
                            <p>Status: {order.status.text}</p>
                            {#if order.status.text == "delivered"}
                                <ul>
                                    <li>Delivered: {new Date(order.delivered_at).toLocaleString()}</li>
                                </ul>
                            {:else}
                                <button on:click={markAsDelivered(order)}>Marked as delivered</button>
                            {/if}
                            <ol>
                                <!-- repeat for every cone in the order -->
                                {#each order.cones as cone, index}
                                    <li>
                                        <!-- this is the cone number so like the list would have cone: #1 then  all the details for that cone-->
                                        <p>Cone #: {index + 1}</p>
                                        <ul>
                                            <li>Cone: {cone.coneType}</li>

                                            <li>Scoop: {cone.iceCreamType}</li>

                                            <li>Topping: {cone.toppingType}</li>

                                        </ul>
                                    </li>
                                {/each}
                            </ol>
                        </div>
                    </div>
                </div>
            {/each}
        {/if}

    {/if}

</body>


<style>

    body {
        background-color: rgb(180, 255, 255);
        margin: 0%;
        font-family: "Poppins", sans-serif;
    }

    button{
        background-color: rgb(59, 238, 137);
        height: 75px;
        width: 200px;
        border-radius: 10px;
        text-align: center;
        font-size: x-large;
        font-family: Verdana, sans-serif;
        font-weight: bold;
        margin-top: 20px;
        padding-left: 20px;
        margin-left: 10px;
    }

    button:hover{
        background-color: rgb(249, 255, 83);
        height: 75px;
        width: 200px;
        border-radius: 10px;
        text-align: center;
        font-size: x-large;
        font-family: Verdana, sans-serif;
        font-weight: bold;
        margin-top: 20px;
        padding-left: 20px;
        
    }

    h1 {
        text-align: center;
    }

    p {
        padding-left: 10px;
    }

    #addresses {
        display: flex;
        flex-direction: row;
        margin-left: 20px;
    }

    .address {
        border: solid black;
        margin: 5px;
        padding: 10px;
    }

    .address > button {
        padding: 0px;
    }

    .address > button > p{
        text-align: center;
        padding: 0px;
        margin: 0px;
    }

    .address > button > svg {
        margin: 0px;
        padding: 0px;
    }
    
    #order {
        border: solid black;
        display: flex;
        flex-shrink: 0;
        margin-left: 10px;
        margin-right: 10px;
        padding-left: 5px;
    }

    .cone_details {
        width: -webkit-fill-available;
    }

    .cone_details > p {
        padding-left: 25px;
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

    li > p {
        text-align: left;
        margin: 5px;
    }
    
    ol > li {
        text-align: left;
        margin: 10 px;
        padding: 5px;
    }
    

    h4 {
        padding-left: 20px;
    }

    #addAddress {
        padding: 5px;
    }

    #addAddress-button {
        display: flex;
        align-items: center;
    }

    #addAddress_dialog > h3 {
        margin: 5px;
    }

    #addAddress_dialog > form {
        display: flex;
        flex-direction: column;
    }

    #addAddress_dialog > form > input {
        margin-bottom: 5px;

    }

    #addAddress_dialog > form > div {
        margin-top: 5px;
    }

</style>