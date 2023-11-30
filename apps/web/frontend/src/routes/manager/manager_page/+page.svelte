<body>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<!--Inventory data-->

<div class="max">
  <h1 class="centerText"> Inventory </h1>
</div>

<div id="inventory" class="center" >
  <div class="parent">
    <div class="child">
      <h1>Ice Cream Flavors</h1>
      {#each iceCreamTypes as flavor }
      <div class="doll">
          <h2>{flavor["name"]}</h2>
          <p>Quantity: {flavor["quantity"]}</p>
          <p>Cost: {flavor["unitCost"]}</p>
      </div> 
      {/each}
    </div>
    <div class="child">
      <h1>Cones</h1>
      {#each coneTypes as cone }
      <div class="doll">
          <h2>{cone["name"]}</h2>
          <p>Quantity: {cone["quantity"]}</p>
          <p>Cost: {cone["unitCost"]}</p>
      </div>
      {/each}
    </div>
    <div class="child">
      <h1>Toppings</h1>
      {#each toppings as topping }
      <div class="doll">
          <h2>{topping["name"]}</h2>
          <p>Quantity: {topping["quantity"]}</p>
          <p>Cost: {topping["unitCost"]}</p>
      </div> 
      {/each}
    </div>
  </div>
</div>

<div class="parent3" >
  <div class="child3">
    <h1>Resupply</h1>
    <select bind:value={itemType} class="select1">
      {#each itemList as item }
      <option value={item}> {item}</option> 
      {/each}
    </select>


    {#if itemType == "coneType"}
    <select bind:value={itemName} class="select1">
      {#each coneTypes as cone }
      <option value={cone['name']}> {cone['name']}</option> 
      {/each}
    </select>

    {:else if itemType == "iceCreamType"}
    <select bind:value={itemName} class="select1">
      {#each iceCreamTypes as flavor }
      <option value={flavor['name']}> {flavor['name']}</option> 
      {/each}
    </select>

    {:else if itemType == "toppingType"}
    <select bind:value={itemName} class="select1">
      {#each toppings as topping }
      <option value={topping['name']}> {topping['name']}</option> 
      {/each}
    </select>

    {:else}
    <select class="select1"> </select>

    {/if}

    <div class="form__group field">
      <label for="amount" class="form__label"> Amount:</label>
      <input type="number" class="form__field" placeholder="Amount" bind:value={amount}/>
    </div>

    <button on:click={updateInventory} class = "orderButton">Purchase</button>
    <p> <p>
  </div>
  <div class="child3">
    <h1>Update Prices</h1>
    <div class="form__group field">
      <label for="Line One" class="form__label"> Item Type:</label>
      <input type="input" class="form__field" placeholder="Item Type" bind:value={itemType2}/>
    </div>

    <div class="form__group field">
      <label for="Line One" class="form__label"> Unit Cost:</label>
      <input type="input" class="form__field" placeholder="Unit Cost" bind:value={unitCost}/>
    </div>
    <button on:click={updateInventory} class="orderButton">Update Item</button>

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
      <p>Revenue: ${revenue} </p>
      <p>Costs: ${cost}</p>
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
  getRevenueandCost();
  getInventory();
  revenueChart();
});

//Variables

let inventory;
let iceCreamTypes = [];
let coneTypes = [];
let toppings = [];

let revenue = 150;
let cost = -40;

let itemList = ["", "coneType","iceCreamType", "toppingType"]
let itemType;
let itemName;
let amount;

let itemType2;
let unitCost;

let labels = ['Monday', 'Tuesday', 'Wenesday', 'Thursday', 'Friday',"Saturday"];
let dataG = [0,100,50,60,100,150];
let dataC = [-10,-50,-20,-70,-20,-40];
let dataN = [-10,40,70,60,140,250];

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

  fetch(updateInvURL, {
    method: 'POST',
    credentials: 'include',
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      name:itemName,
      itemType: itemType,
      additionalUnits: amount,
    })
  })
  .then(resp => resp.json())
  .then(json => console.log(json))
  
  window.location.href = '/manager/manager_page'
}

//update inventory items amount
function updateInventoryItems(){
  updateInvItemURL = 'http://localhost:8000/api/update-inventory-item/'


}


// ******** FUNCTIONS FOR CONTACTS *************************************************************
//GET request for list of contacts
function getContacts(){

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
  //inventory = infoJson['revenue']
  console.log(infoJson)


  const response2 = await fetch(
    costURL,{
      method: "GET",
      credentials: "include"
    })
  const infoJson2 = await response2.json()
  //inventory = infoJson['cost']
  console.log(infoJson2)

}

// function for creating graph for manager
function revenueChart() {
  const chart = document.getElementById('myChart');
 
  new Chart(chart, {
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
          min: -250,
          max: 250
        }
      }
    }
  });
}

//****************************************** Inventory Status ******************************************
function test(){
  console.log(inventory)
  console.log(iceCreamTypes)
}
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
    border-bottom: double 10px black;
    width: 100%;
  }

  p{
        text-align: left;
        font-size: medium;
    }
    
  h2 {
      font-family: 'Trebuchet MS', sans-serif;
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
      padding: 10px;
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
      width: 100%;
      display: grid;
      background:rgb(255, 255, 255);
      width:90%;
      height:400px;
      margin: auto;
      border: 3px solid rgb(0, 0, 0);
      font-family: 'Trebuchet MS', sans-serif;
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
        margin-left: 22%;
        text-align: left;
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
      border-bottom: 50px black double;
    }

    .select1{
      margin: 25px;
      height: 50px;
      width: 250px;
      text-align: center;
      font-size: medium;
      border-radius: 10px;
  }
    

</style>

