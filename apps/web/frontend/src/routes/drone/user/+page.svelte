<script>
    import { onMount } from 'svelte'

    const url = 'http://localhost:8000/api';

    let timeout;
    let types = [];
    let drones = [];
    let statuses = [];

    let username = "";
    let first_name = "";
    let last_name = "";

    let totalRevenue = 0;

    let myDrones_error = '';
    let showDialogClickError = '';

    let droneName = '';
    let drone_selected;

    let dialog_addDrone; // Reference to the dialog tag
    let dialog_editDrone; // Reference to the dialog for edit drones

	onMount(() => {
        get_privateInfo();
        get_droneTypes();
        get_droneStatuses();
        get_myDrones();

		dialog_addDrone = document.getElementById('add_drone-dialog');
        dialog_editDrone = document.getElementById('edit_drone-dialog');
	});

    // get the users private data
    async function get_privateInfo() {
        fetch(url + '/private-owner-data/', {credentials: 'include', method: 'GET', mode: "cors"})
            .then((response) => {
                // console.log(response)
                return response.json()
            })
            .then((json) => {
                username = json.username;
                first_name = json.first_name;
                last_name = json.last_name;
                console.log(username);
            });
    }

    // get the different drone types from the database
    async function get_droneTypes() {
        fetch(url + '/drone-types/', {method: 'GET',})
            .then((response) => response.json())
            .then((json) => {
                types = json['droneTypes'];            
            });
    }

    async function get_droneStatuses() {
        fetch(url + '/drone-statuses/', {method: 'GET',})
            .then((response) => response.json())
            .then((json) => {
                statuses = json['droneStatuses'];
            });
    }

    async function get_myDrones() {
        fetch(url + '/my-drones/', {credentials: "include", method: 'GET'})
        .then((response) => response.json())
        .then((json) => {
            if (json['success'] == true) {
                drones = json['drones'];
            }
            else {
                myDrones_error = "There was an error getting your drones: " + json['message'];
            }
        });
    }

    async function post_newDrone(drone_name, drone_status, drone_type) {
        fetch(url + '/add-drone/', {credentials: "include", method: 'POST', body: JSON.stringify({name: drone_name, status: drone_status, droneType: drone_type})})
            .then((response) => response.json())
            .then((json) => {
                if (json['success'] == true) {
                    console.log('post new drone was successful');
                    get_myDrones();
                    let droneName_text = document.getElementById('drone_name');
                    droneName_text.value = "";
                    let radios = document.getElementsByName('drone_type');
                    for (let i = 0; i < radios.length; i++) {
                        radios[i].checked = false;
                    }
                }
                else {
                    console.log('there was an error');
                    showDialogClickError = "There was an error when adding the drone: " + json['message'];
                }
            });
    }

    async function edit_drone(drone_id, drone_info) {
        fetch(url + '/update-drone/', {credentials: "include", method: 'PATCH', mode: "cors", body: JSON.stringify({id: drone_id, name: drone_info.get('drone_name'), droneType: drone_info.get('drone_type')})})
            .then((response) => response.json())
            .then((json) => {
                if (json['success'] == true) {
                    console.log('patch drone was successful');
                    get_myDrones();
                    let droneName_editDrone = document.getElementById('drone_name_edit');
                    droneName_editDrone.value = "";
                    let radios = document.getElementsByName('drone_type');
                    for (let i = 0; i < radios.length; i++) {
                        radios[i].checked = false;
                    }
                }
                else {
                    console.log('there was an error');
                    showDialogClickError = "There was an error when editting the drone: " + json['message'];
                }
            });
    }

    async function changeDroneStatus (drone) {
        let droneStatus_range = document.getElementById('isActive');

        let newStatus;
        if (droneStatus_range.value == droneStatus_range.min) {
            newStatus = "owner";
        }
        else if (droneStatus_range.value == droneStatus_range.max) {
            newStatus = "idle";
        }
        fetch(url + '/update-drone/', {credentials: "include", method: 'PATCH', mode: "cors", body: JSON.stringify({id: drone.id, status: newStatus})})
            .then((response) => response.json())
            .then((json) => {
                if (json['success'] == true) {
                    console.log('patch drone was successful');
                    get_myDrones();
                    let droneName_editDrone = document.getElementById('drone_name_edit');
                    droneName_editDrone.value = "";
                    let radios = document.getElementsByName('drone_type');
                    for (let i = 0; i < radios.length; i++) {
                        radios[i].checked = false;
                    }
                }
                else {
                    console.log('there was an error');
                    showDialogClickError = "There was an error when editting the drone: " + json['message'];
                }
            });
    }
	
	// Show the dialog when clicking "Delete everything"
	const showDialogClick_addDone = (asModal = true) => {
		try {
            dialog_addDrone[asModal ? 'showModal' : 'show']();
		} catch(e) {
            showDialogClickError = e;
		}  
	};

    const showDialogClick_editDone = (asModal = true, drone) => {
		try {
            drone_selected = drone;
            document.getElementById("drone_name_edit").value = drone_selected.name;
            let radios = document.getElementsByName('drone_type');
            for (let i = 0; i < radios.length; i++) {
                if (radios[i].type == 'radio' && radios[i].value == drone.droneType.text) {
                    radios[i].checked = true;
                }
            }
            dialog_editDrone[asModal ? 'showModal' : 'show']();
		} catch(e) {
            showDialogClickError = e;
		}  
	};

    const closeClick = (dialogId) => {
        if (dialogId == 'add_drone') {
            dialog_addDrone.close();
        }
        else if (dialogId == 'edit_drone') {
            dialog_editDrone.close();
        }
	};

    const confirmClick_addDrone = () => {
        let form = document.querySelector("form");
        if (checkInput()) {
            dialog_addDrone.close();
            const data = new FormData(form);
            let output = "";
            for (const entry of data) {
                output = `${output}${entry[0]}=${entry[1]}\r`;
            }
            post_newDrone(data.get('drone_name'), statuses[0].text, data.get('drone_type'));
        }     
    }

    const confirmClick_editDrone = () => {
        let form = document.getElementById("editDrone-form");
        // console.log("im not broken")
        if (checkInput()) {
            const data = new FormData(form);
            let output = "";
            for (const entry of data) {
                output = `${output}${entry[0]}=${entry[1]}\r`;
            }
            if (data.get('drone_name') == "") {
                data.set('drone_name', drone_selected.name);
            }
            // console.log(data.get('drone_name'))
            edit_drone(drone_selected.id, data);
            closeClick('edit_drone');
        }
    }
    
    const checkInput = () => {
        if (document.getElementsByName.value == '') {
            // console.log("drone name empty")
            return false;
        }
        let isButtonChecked = false;
        let radios = document.getElementsByName('drone_type');
        for (let i = 0; i < radios.length; i++) {
            if (radios[i].type == 'radio' && radios[i].checked) {
                // console.log("a drone type is selected")
                isButtonChecked = true;
            }
        }
        // if (!isButtonChecked) {
        //     console.log("no drone type selected")
        // }
        return isButtonChecked;
    }

</script>
<h1>Welcome, {username}</h1>
<p>Name: {first_name} {last_name}</p>
<p>Drones: {drones.length}</p>
<p>Total Revenue: ${totalRevenue}</p>
<p>Total Deliveries: ????</p>
<dialog id="add_drone-dialog">
    <h3>Add Drone</h3>
    <form>
        <label for="drone_name">Drone Name:</label>
        <input bind:value={droneName} type="text" id="drone_name" name="drone_name" placeholder="Drone Name" required>

        <fieldset>
            <legend>Size of Drone:</legend>
            <!-- for each type in types -->
            {#each types as item}
                <div>
                    <input type="radio" id={item.text} value={item.text} name="drone_type" required/>
                    <lable for={item.text}>{item.text}: Capacity of {item.capacity}</lable>
                </div>
            {/each}
        </fieldset>

        <button on:click={() => closeClick('add_drone')} type="reset">Cancel</button>
        <button on:click={confirmClick_addDrone}>Add Drone</button>
    </form>

</dialog>

<dialog id="edit_drone-dialog">
    <h3>Edit Drone</h3>
    <form id="editDrone-form">
        <label for="drone_name">Drone Name:</label>
        <input type="text" value="" id="drone_name_edit" name="drone_name" placeholder="Drone Name">

        <fieldset>
            <legend>Size of Drone:</legend>
            <!-- for each type in types -->
            {#each types as item}
                <div>
                    <input type="radio" id={item.text} value={item.text} name="drone_type" required/>
                    <lable for={item.text}>{item.text}: Capacity of {item.capacity}</lable>
                </div>
            {/each}
        </fieldset>

        <button on:click={() => closeClick('edit_drone')} type="reset">Cancel</button>
        <button on:click={confirmClick_editDrone}>Submit Edits</button>
    </form>
</dialog>

<p>{showDialogClickError}</p>
<button on:click={() => showDialogClick_addDone(true)} id="add_drone-button">
    <span>
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
    </span>
    Add new Drone
</button>
<div id="drones">
    <!-- for each drone that the user has -->
    {#if drones.length == 0}
        <div class='drone_error'>
            <h3>No Drones</h3>
            <p>To add a drone click the 'Add Drone' button</p>
            <p>{myDrones_error}</p>
        </div>
    {:else}
        {#each drones as drone}
            <div class="drone">
                <div class="drone_details">
                    <h2>Drone: {drone.name}</h2>
                    <ul>
                        <li>Type, capacity: {drone.droneType.text}, {drone.droneType.capacity}</li>
                        <li>Deliveries: ????</li>x
                        <li>Revenue: $</li>
                        <!-- <li hidden>{totalRevenue += drone.revenue}</li> -->
                        <li>Status: {drone.status.text}
                            <form>
                                {#if drone.status.text == 'delivering'}
                                    <input type="range" id="isActive" name="isActive" min="0" max="1" value="1" on:change={() => changeDroneStatus(drone)} disabled/>
                                {:else if drone.status.text == "idle"}
                                    <input type="range" id="isActive" name="isActive" min="0" max="1" value="1" on:change={() => changeDroneStatus(drone)}/>
                                {:else}
                                    <input type="range" id="isActive" name="isActive" min="0" max="1" value="0" on:change={() => changeDroneStatus(drone)}/>
                                {/if}

                                {#if drone.status.text != "owner"}
                                    <label for="isActive">Deactivate</label>
                                {:else}
                                    <label for="isActive">Activate</label>
                                {/if}
                            </form>
                        </li>
                    </ul>
                </div>

                <div class="edit_drone">
                    <button on:click={() => showDialogClick_editDone(true, drone)} id="edit_drone-button">
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
                          <p>Edit Drone</p>
                    </button>
                </div>
            </div>
        {/each}
    {/if}
    
</div>

<style>
    h1 {
        text-align: center;
    }

    p {
        padding-left: 15px;
    }

    #add_drone-button {
        display: flex;
        align-items: center;
        padding: 5px 15px;
    }

    #add_drone-button > span {
        margin-right: 5px;
    }

    #drones {
        padding: 20px;
    }

    .drone {
        display: flex;
        border: solid black;
        padding-left: 20px;
        margin-bottom: 10px;
    }

    .drone_error {
        border: solid black;
        padding-left: 20px;
    }

    .drone_details {
        width: -webkit-fill-available;
    }

    .edit_drone {
        display: flex;
        flex-direction: column;
        padding: 5px;
        margin: 5px;
    }

    .edit_drone > button > p{
        padding: 0px;
        margin: 5px;
        width: max-content;
    }

    .edit_drone > button > svg {
        padding-top: 5px;
    }


</style>
