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

<!--TODO: api calls to GET data from data base for manager information-->


<script>
import { onMount } from "svelte";

function createChart() {
  const chart = document.getElementById('myChart');
 
  new Chart(chart, {
    type: 'line',
    data: {
      // Labels Data types
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple'],

      //Datasets for the graph
      datasets: [{
        label: 'Revenue',
        data: [12, 16, 3, 5, 2],
        borderWidth: 3
      },
      { 
      //2nd Datasets for the graph
      label: 'Expenees',
        data: [-11,-32,-3,-4,-45],
        borderWidth: 3
      }]
    },
    //Options
    options: {
      scales: {
        y: {
          min: -50,
          max: 50
        }
      }
    }
  });
}

function createInventory(){
  const cones = document.getElementById("Cones")

  new Chart(cones,{
    type: "doughnut",
    data:{
      datasets:[{
        data:[120,100],
        borderWidth: 3 
      }]
    }

  }); 
  
}

// "localhost:8000/api/[data]" url for api call for data
let apiUrl = "http://localhost:8000/api/cone-types/"
//**** Inventory Status ****
onMount(async () => {
  fetch(apiUrl)
  .then(data => {
		let inventory = data;
    console.log(inventory) 
    }).catch(error => {
    console.log(error);
  });
});

/*
**** Revenue Status ****
onMount(async () => {
  fetch('')
  .then(response => response.json())
  .then(revenueData => {
		revenue = revenueData
    }).catch(error => {
    console.log(error);
  });
});


**** Contatct Status ****
onMount(async () => {
  fetch('')
  .then(response => response.json())
  .then(contactData => {
		contact = contactData;  
    }).catch(error => {
    console.log(error);
  });
});



*/

onMount(createChart)
onMount(createInventory)

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

