<h1>Manager Page</h1>

<!--Inventory data-->

<h2 class="centerText"> Inventory </h2>
<div id="inventory" class="center" >


</div>

<!--Revenue data-->
<h2 class="centerText"> Revenue </h2>
<div id="revenue" class="center">

</div>
<!--Contact data-->
<h2 class="centerText"> Customer's Contact </h2>
<div id="customer_contact"  class="center">

</div>



<!--
TODO: api calls to GET data from data base for manager information
**** RELOCATED WHEN to Script File WHEN DONE ****
-->


<script>
    import { onMount } from "svelte";
// "localhost:8000/api/[data]" url for api call for data

/*  
**** Inventory Status ****
onMount(async () => {
  fetch("")
  .then(response => response.json())
  .then(data => {
		inventory = data;  
    }).catch(error => {
    console.log(error);
  });
});

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



</script>

<!--Temp Style **** RELOCATE to CSS FILE WHEN DONE ****-->
<style>
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
        height:250px;
        border-style: solid;
        margin-bottom: 20px;
        border-radius: 20px;
            }
    #revenue {
        float:center; 
        background:hsl(0, 0%, 100%);
        width:75%;
        height:250px;
        border-style: solid;
        margin-bottom: 20px;
        border-radius: 20px;
        }
    #customer_contact{
        float:center; 
        background:rgb(249, 249, 249);
        width:75%;
        height:250px;
        border-style: solid;
        margin-bottom: 20px;
        border-radius: 20px;
            }
    
</style>

