<script>
    import { onMount } from 'svelte'

    const url = "http://localhost:8000/api"

    let name = "";
    let addresses = [];
    let error = '';

    let removeBttn_height = 0;

    onMount(() => {
        get_myAddresses();
        console.log(document.cookie)
    });

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
</script>

<h1>Account</h1>
<p>{error}</p>
<p>Name: {name}</p>
<p style="margin: 1px;">Addresses:</p>
{#if addresses.length == 0}
    <h3 style="margin: 5px;">You have no Addresses, please add one</h3>
{:else}
    <div id="addresses">
        {#each addresses as address, index}
            <div class="address">Address #{index}: 
                <p>{address.lineOne}, {address.lineTwo}</p>
                <p>{address.city}, {address.state} {address.zipCode}</p>
                <button id='editAddress'>
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none">
                        <g clip-path="url(#clip0_7_2)">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M0 14.2V18H3.8L14.8 6.9L11 3.1L0 14.2ZM17.7 4C18.1 3.6 18.1 3 17.7 2.6L15.4 0.3C15 -0.1 14.4 -0.1 14 0.3L12.2 2.1L16 5.9L17.7 4Z" fill="black"/>
                        </g>
                        <defs>
                            <clipPath id="clip0_7_2">
                                <rect width="18" height="18" fill="white"/>
                            </clipPath>
                        </defs>
                    </svg>
                    <p>Edit</p>
                </button>

                <button id='removeAddress'>
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
    <button id="addAddress-button">
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
<div id="orders">
    <!-- for each order do this -->
    <div id="order">
        <div class="cone_details">
            <h3>Order #: ??????</h3>
            <p>Order placed: HH:MM</p>
            <p>Total Cost: $$$$$</p>
            <ol>
                <!-- repeat for every cone in the order -->
                <li>
                    <!-- this is the cone number so like the list would have cone: #1 then  all the details for that cone-->
                    <p>Cone #: ?</p>
                    <!-- the number of this cone ordered -->
                    <p>Cone Qty. ???</p>
                    <p>Cone Cost: $$$$</p>
                    <ul>
                        <li>Cone: ???</li>

                        <li>
                            Scoops:
                            <ul>
                                <li>options</li>
                                <li>options</li>
                                <li>options</li>
                            </ul>
                        </li>

                        <li>
                            Toppings:
                            <ul>
                                <li>options</li>
                                <li>options</li>
                                <li>options</li>
                            </ul>
                        </li>

                    </ul>

                </li>
                
            </ol>
        </div>

        <div class="add_to_cart">
            <button type="button">
                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30" fill="none">
                    <g clip-path="url(#clip0_11_8)">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M9 24C7.35 24 6 25.35 6 27C6 28.65 7.35 30 9 30C10.65 30 12 28.65 12 27C12 25.35 10.65 24 9 24ZM0 0V3H3L8.4 14.4L6.3 18C6.15 18.45 6 19.05 6 19.5C6 21.15 7.35 22.5 9 22.5H27V19.5H9.6C9.45 19.5 9.3 19.35 9.3 19.2V19.05L10.65 16.5H21.75C22.95 16.5 23.85 15.9 24.3 15L29.7 5.25C30 4.95 30 4.8 30 4.5C30 3.6 29.4 3 28.5 3H6.3L4.95 0H0ZM24 24C22.35 24 21 25.35 21 27C21 28.65 22.35 30 24 30C25.65 30 27 28.65 27 27C27 25.35 25.65 24 24 24Z" fill="black"/>
                    </g>
                    <defs>
                      <clipPath id="clip0_11_8">
                        <rect width="30" height="30" fill="white"/>
                      </clipPath>
                    </defs>
                  </svg>
                <p>Add to Cart</p>
            </button>
        </div>
    </div>
</div>

<style>
    h1 {
        text-align: center;
    }

    p {
        padding-left: 10px;
    }

    #addresses {
        display: flex;
        flex-direction: row;
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
    

    .add_to_cart > button {
        align-self: flex-end;
        width: fit-content;
    }

    .add_to_cart > button > svg {
        align-self: center;
    }

    .add_to_cart > button > p {
        margin: 0px;
        padding-left: 0px;
        text-align: center;
    }

    #editAddress > svg {
        padding-top: 3px;
        padding-bottom: 4px;
    }

    #editAddress {
        width: 53.64px;
    }

    #addAddress {
        padding: 5px;
    }

    #addAddress-button {
        display: flex;
        align-items: center;
    }

</style>