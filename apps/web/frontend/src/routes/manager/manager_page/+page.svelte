<body>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<!--Inventory data-->
<h1 class="centerText"> Inventory </h1>

<div class="center">
  <button on:click={test}>TEST</button>
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

<!--Revenue data-->
<h1 class="centerText"> Revenue </h1>

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
<h1 class="centerText"> Customer's Contact </h1>
  
<div id="customer_contact"  class="center">
</div>

</body>

<script>
//Imported Items
import { onMount } from "svelte";

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

let revenue = 500;
let cost = 500;

let labels = ['Monday', 'Tuesday', 'Wenesday', 'Thursday', 'Friday',"Saturday"];
let dataG = [-11,-32,-3,-4,-45,420];
let dataC = [12, 16, 3, 5, 2];
let dataN = [11, 49, 94, 19, 200];

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
}

//update inventory price
function updateInventory(){
  updateInvURL = 'http://localhost:8000/api/update-inventory/'

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
    
</style>

