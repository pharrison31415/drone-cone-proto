<body style="background: #BAF3FF; margin: 0%">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<!--Inventory data-->

<h2 class="centerText"> Inventory </h2>
<div id="inventory" class="center" >
<canvas id="Cones"></canvas>

</div>

<!--Revenue data-->
<h2 class="centerText"> Revenue </h2>
<div id="revenue" class="center">
  <canvas id="myChart"></canvas>
  <p>Current revenue $500</p>
</div>
<!--Contact data-->
<h2 class="centerText"> Customer's Contact </h2>
<div id="customer_contact"  class="center">

</div>

</body>

<script>
//Imported Items
import { onMount } from "svelte";

onMount(revenueChart , getInventory)

//Variables

let inventory;

// ******** FUNCTIONS FOR INVENTORY *************************************************************
// GET request for Inventory
function getInventory(){
  invURL = 'http://localhost:8000/api/inventory/'
  
  async() => {
    const response = await fetch(invURL,{method: 'GET'})
    .then(jsonData = await response.json())
    .catch(console.log(error))
  }
  inventory = jsonData
  console.log(inventory)
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
function getRevenue(){

}

// function for creating graph for manager
function revenueChart() {
  const chart = document.getElementById('myChart');
 
  new Chart(chart, {
    type: 'line',
    data: {
      // Labels Data types
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple',"TEST"],

      //Datasets for the graph
      datasets: [{
        label: 'Revenue',
        data: [12, 16, 3, 5, 2],
        borderWidth: 3
      },
      { 
      //2nd Datasets for the graph
      label: 'Expenees',
        data: [-11,-32,-3,-4,-45,420],
        borderWidth: 3
      }]
    },
    //Options
    options: {
      scales: {
        y: {
          min: -500,
          max: 500
        }
      }
    }
  });
}
</script>

<!--Temp Style **** RELOCATE to CSS FILE WHEN DONE ****-->
<style>
    canvas{
      margin: 0;
    }
    h2 {
        font-family: 'Trebuchet MS', sans-serif;
    }
    .center {
        margin: auto;
        width: 50%;
        border: 3px solid rgb(0, 0, 0);
        padding: 10px;
        font-family: 'Trebuchet MS', sans-serif;
        }
    

    .centerText {
        margin: auto;
        width: 50%;
        padding: 10px;
        text-align: center;
            }    

    #inventory {
        background:rgb(255, 255, 255);
        width:75%;
        height:500px;
        border-style: solid;
        margin-bottom: 20px;
        border-radius: 20px;
            }
    #revenue {
        float:center; 
        background:hsl(0, 0%, 100%);
        width:75%;
        height:500px;
        border-style: solid;
        margin-bottom: 20px;
        border-radius: 20px;
        }
    #customer_contact{
        float:center; 
        background:rgb(249, 249, 249);
        width:75%;
        height:500px;
        border-style: solid;
        margin-bottom: 20px;
        border-radius: 20px;
            }

    #myChart{
      width: 400px;
    }
    
</style>

