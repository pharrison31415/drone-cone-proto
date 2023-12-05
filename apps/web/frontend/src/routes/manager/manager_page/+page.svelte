<body>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<!--Inventory data-->

<div class="max">
  <h1 class="centerText"> Inventory </h1>
</div>

<div id="inventory" class="center" >
  <div class="parent">
    <div class="child">
      <h1 class="colorTitle">Ice Cream Flavors</h1>
      {#each iceCreamTypes as flavor }
      <div class="doll">
          <h2>{flavor["name"]}</h2>
          <p>Quantity: {flavor["quantity"]}</p>
          <p>Cost: {USDollar.format(flavor["unitCost"] / 100)}</p>
      </div> 
      {/each}
    </div>
    <div class="child">
      <h1 class="colorTitle">Cones</h1>
      {#each coneTypes as cone }
      <div class="doll">
          <h2>{cone["name"]}</h2>
          <p>Quantity: {cone["quantity"]}</p>
          <p>Cost: {USDollar.format(cone["unitCost"] / 100)}</p>
      </div>
      {/each}
    </div>
    <div class="child">
      <h1 class="colorTitle">Toppings</h1>
      {#each toppings as topping }
      <div class="doll">
          <h2>{topping["name"]}</h2>
          <p>Quantity: {topping["quantity"]}</p>
          <p>Cost: {USDollar.format(topping["unitCost"] / 100)}</p>
      </div> 
      {/each}
    </div>
  </div>
</div>

<div class="parent3" >
  <div class="child3">
    <h1 class="colorTitle">Resupply</h1>
    <label for="Line One" class="form__label"> Select a Item Type:</label>
    <select bind:value={itemType} class="select1">
      {#each itemList as item }
      <option value={item}> {item}</option> 
      {/each}
    </select>

    <label for="Line One" class="form__label"> Select a Item:</label>
    {#if itemType == "Cones"}
    <select bind:value={itemName} class="select1">
      {#each coneTypes as cone }
      <option value={cone['name']}> {cone['name']}</option> 
      {/each}
    </select>

    {:else if itemType == "Ice Cream"}
    <select bind:value={itemName} class="select1">
      {#each iceCreamTypes as flavor }
      <option value={flavor['name']}> {flavor['name']}</option> 
      {/each}
    </select>

    {:else if itemType == "Topping"}
    <select bind:value={itemName} class="select1">
      {#each toppings as topping }
      <option value={topping['name']}> {topping['name']}</option> 
      {/each}
    </select>

    {:else}
    <select class="select1"> </select>

    {/if}

    <div class="form__group field">
      <input type="number" class="form__field" placeholder=" Amount" bind:value={amount}/>
    </div>

    <button on:click={updateInventory} class = "orderButton">Purchase</button>
    <p> <p>
  </div>
  <div class="child3">
    <h1 class="colorTitle">Update Prices</h1>

    <div>
      <label for="Line One" class="form__label"> Select a Item Type:</label>
      <select bind:value={itemType2} class="select1__2">
        {#each itemList as item }
        <option value={item}> {item}</option> 
        {/each}
      </select>
    </div>
    <br>
    <div class="form__group field">
      <input type="number" class="form__field" placeholder=" Unit Cost" bind:value={unitCost}/>
    </div>
    <button on:click={updateInventoryItems} class="orderButton">Update Item</button>

  </div>
  
</div>

<!--Revenue data-->
<div class="max">
  <h1 class="centerText"> Revenue </h1>
</div>

<div id="revenue" class="center">
  <div class="parent2">
    <div class="chart">
      <canvas id="myChart"></canvas> 
    </div>
    <div class="chartInfo">
      <p>Revenue: {USDollar.format(revenue)} </p>
      <p>Costs: {USDollar.format(cost)}</p>
      <p>Net: {USDollar.format(revenue - cost)}</p>
    </div>
  </div>
</div>


<!--Contact data-->
<div class="max">
  <h1 class="centerText"> Customer Contacts </h1>
</div>
  
<div id="customer_contact"  class="center">
</div>

</body>

<script>
//Imported Items
import { onMount } from "svelte";

//Trigger function once called
onMount(()=>{
  getRevenueandCost()
    .then(revenueChart());
  getInventory();  
  getContacts();
});

//Variables

let inventory;
let iceCreamTypes = [];
let coneTypes = [];
let toppings = [];

let revenue = 0;
let cost = 0;

let itemList = ["", "Cones","Ice Cream", "Topping"]
let itemType;
let itemName;
let amount;

let itemType2;
let unitCost;

let mondayR = 0;
let tuesdayR = 0;
let wenesdayR = 0;
let thursdayR = 0;
let fridayR = 0;
let saturdayR = 0;
let sundayR =0;


let mondayC = 0;
let tuesdayC = 0;
let wenesdayC = 0;
let thursdayC = 0;
let fridayC = 0;
let saturdayC = 0;
let sundayC = 0;

let labels = ['Suday', 'Monday', 'Tuesday', 'Wenesday', 'Thursday', 'Friday',"Saturday"];
let dataG = [ sundayR, mondayR, tuesdayR , wenesdayR , thursdayR , fridayR , saturdayR ];
let dataC = [ sundayC, mondayC, tuesdayC , wenesdayC , thursdayC , fridayC , saturdayC ];
let dataN = [ sundayR - sundayC , mondayR - mondayC , tuesdayR - tuesdayC , wenesdayR - wenesdayC , thursdayR - thursdayC , fridayR - fridayC , saturdayR - saturdayC];


let getToday = new Date().getDay();

// ******** FUNCTIONS FOR INVENTORY *************************************************************
// GET request for Inventory
async function getInventory(){
  let invURL = 'http://localhost:8000/api/inventory/'
  
  const response = await fetch (
    invURL,{
      method: "GET",
      credentials: "include"
    })
  const infoJson = await response.json()
  inventory = infoJson['inventory']
  console.log(inventory)

  for(let item of inventory["iceCreamTypes"]){
    iceCreamTypes.push(item);
    
    iceCreamTypes = iceCreamTypes;
  }

  for(let item of inventory["coneTypes"]){
    coneTypes.push(item);
    coneTypes = coneTypes;
  }

  for(let item of inventory["toppingTypes"]){
    toppings.push(item);
    toppings = toppings;
  }
};

//update inventory amount
async function updateInventory(){
  let updateInvURL = "http://localhost:8000/api/purchase-inventory/";

  await fetch(updateInvURL, {
    method: 'POST',
    credentials: 'include',
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      name:itemName,
      itemType: inputCheckforPurchase(),
      additionalUnits: amount,
    })
  })
  .then(resp => resp.json())
  .then(json => console.log(json))
  
  window.location.href = '/manager/manager_page'
}

function checkInputs(){

}

//update inventory items amount
async function updateInventoryItems(){
  let updateInvItemURL = 'http://localhost:8000/api/update-inventory-item/';

  await fetch(updateInvItemURL,{
    method: "PATCH",
    credentials: "include",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      itemType: itemType2,
      unitCost: unitCost
    })
  })
  .then(resp => resp.json())
  .then(json => console.log(json))

  }


// ******** FUNCTIONS FOR CONTACTS *************************************************************
//GET request for list of contacts
async function getContacts(){
  let contactURl = 'http://localhost:8000/api/messages'

  const response = await fetch(
    contactURl,{
      method: "GET",
      credentials: "include",
    })
  const infoJson = await response.json()
  console.log(infoJson)
}

// ******** FUNCTIONS FOR REVENUE *************************************************************
//GET request for revenue
async function getRevenueandCost(){
  let revURL = 'http://localhost:8000/api/manager-revenues/'
  let costURL = 'http://localhost:8000/api/manager-costs/'
  
  const response = await fetch (
    revURL,{
      method: "GET",
      credentials: "include"
    })
  const infoJson = await response.json()
  
  for (let rev of infoJson['revenues']){
    revenue += rev['amount']
  }
  revenue = revenue / 100;
  


  const response2 = await fetch(
    costURL,{
      method: "GET",
      credentials: "include"
    })
  const infoJson2 = await response2.json()
  for (let cos of infoJson2['costs']){
    cost += cos['amount']
  }
  cost = cost / 100;


  placementOfRevenues();
  
}

// function for creating graph for manager
async function revenueChart() {
  const chart = document.getElementById('myChart');
 
  await new Chart(chart, {
    type: 'line',
    data: {
      // Labels Data types
      labels: labels,

      //Datasets for the graph
      datasets: [
      {
        label: 'Gross',
        data: dataG,
        borderWidth: 3
      },
      { 
      //2nd Datasets for the graph
      label: 'Expenses',
        data: dataC,
        borderWidth: 3
      },

      //3rd Datasets for the graph
      {
      label: 'Net',
      data: dataN,
      borderWidth: 3
      }]
    },
    //Options
    options: {
      scales: {
        y: {
          min: -20,
          max: 20
        }
      }
    }
  });
}

function placementOfRevenues(){

  switch (getToday){
    case 0: 
      sundayR += revenue;
      sundayR = sundayR;
      console.log(sundayR)
  }

}
//****************************************** Misc Functions ******************************************
function test(){
  console.log(inventory)
  console.log(iceCreamTypes)
}

function inputCheckforPurchase(){
  if (itemType == 'Cones'){ return 'coneType'}
  else if (itemType == 'Ice Cream'){ return 'iceCreamType'}
  else if (itemType == 'Topping'){ return 'toppingType'}
  else return 'Error'
}

// Format the price above to USD using the locale, style, and currency.
let USDollar = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    });




</script>

<!--Temp Style **** RELOCATE to CSS FILE WHEN DONE ****-->
<style>
  body {
    background-color: rgb(33, 122, 254);
    margin: 0%;
    font-family: "Poppins", sans-serif;
  }

  h1{
    text-align: center;
    font-size: xx-large;
    width: 100%;
  }

  p{
        text-align: left;
        font-size: medium;
    }
    
  .chart{
    width: 100%;
    height: 97%;    
    display: inline-block;
  }
  .chartInfo{
    width: 100%;
    height: 97%;
    display: inline-block;

  }
    
  .center {
      margin: auto;
      width: 50%;
      border: 3px solid rgb(0, 0, 0);
      font-family: 'Trebuchet MS', sans-serif;
  }

  .centerText {
      margin: auto;
      width: 50%;
      text-align: center;
  }

  .parent{
      grid-template-columns: 1fr 1fr 1fr;
      width: 100%;
      height: 100%;
      display: grid;
  }

  .child {
      display: inline-block;
      border-top: none;
      overflow: auto;
      border: 10px solid black;
  }

  .parent3{
      grid-template-columns: 1fr 1fr;
      display: grid;
      background:rgb(255, 255, 255);
      width:90%;
      height:400px;
      margin: auto;
  }

  .child3{
      display: inline-block;
      border-top: none;
      overflow: auto;
      border: 10px solid black;
  }

  .parent2{
      grid-template-columns: 80% 20%;
      width: 100%;
      height: 100%;
      display: grid;
  }

  .doll{
    border-bottom: dotted 10px black;
    padding-left: 10px;
  }

  #inventory {
      background:rgb(255, 255, 255);
      width:90%;
      height:500px;
  }

  #revenue {
      float:center; 
      background:hsl(0, 0%, 100%);
      width:90%;
      height:500px;
      border-style: solid;
      margin-bottom: 20px;
      border-radius: 20px;
  }
        
  #customer_contact{
        float:center; 
        background:rgb(249, 249, 249);
        width:90%;
        height:500px;
        border-style: solid;
        margin-bottom: 20px;
        border-radius: 20px;
            }

    #myChart{
      width: 400px;
    }
    
    .form__group{
        width: 75%;
        height: 60px;
        margin-left: 10%;
        margin-bottom: 10px;
        margin-top: 5px;
        text-align: center;
        grid-template-rows: 100px 2;
        display: grid;
    }

    .form__field{
        font-size: large;
        width: 250px;
        margin-left: 22%;
        border-radius: 10px;
    }

    .form__field:focus::-webkit-input-placeholder{
        opacity: 0;
    }

    .form__label{
        width: 16rem;
        font-size: medium;
        margin-left: 1%;
        text-align: left;
        position: absolute;
    }

    .orderButton{
        width: 200px;
        height: 50px;
        font-size: x-large;
        border-radius: 40px;
        background-color: rgb(0, 255, 166);
        margin-left: 30%;
        font-weight: bold;

    }

    .orderButton:hover{
        width: 200px;
        height: 50px;
        font-size: x-large;
        border-radius: 40px;
        background-color: yellow;
        margin-left: 30%;
        font-weight: bold;
    }
    
    .max{
      width: 100%;
      background-color: white;
      margin-top: 100px;
      margin-bottom: 50px;
      border-top: double 5px black;
      border-bottom: double black 4px;
      box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;

    }

    .select1{
      margin: 25px;
      height: 50px;
      width: 250px;
      text-align: center;
      font-size: medium;
      border-radius: 10px;
  }

    .select1__2{
      margin-left: 27%;
      height: 50px;
      width: 250px;
      text-align: center;
      font-size: medium;
      border-radius: 10px;
  }

    .colorTitle{
    text-align: center;
    font-size: xx-large;
    width: 100%;
    margin: none;
    padding:none;
    border-bottom: double black 6px;
    background-color: rgb(255, 255, 255);

    }
    

</style>

