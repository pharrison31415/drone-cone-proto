<h1>Manager Page</h1>

<!--Inventory data-->
<div id="inventory" class="center" >
  

</div>

<!--Revenue data-->
<div id="revenue" class="center">

</div>
<!--Contact data-->
<div id="customer_contact"  class="center">

</div>



<!--
TODO: api calls to GET data from data base for manager information
**** RELOCATED WHEN to Script File WHEN DONE ****
-->


<script>
	import { onMount } from "svelte";


    testSting = ""

    /*  
        contacts = None
    	
        async function  {
		const response = await fetch('api request for list of contact');
		contacts = await response.json();
        }

        revenue = None
    	
        async function  {
		const response = await fetch('api request for revenue ');
		revenue = await response.json();
        }


        inventory = None
    	async function  {
		const response = await fetch('api request for list of contact');
		inventory = await response.json();
        }   
    */


</script>

<!--Temp Style **** RELOCATE to CSS FILE WHEN DONE ****-->
<style>
    .center {
        margin: auto;
        width: 50%;
        border: 3px solid rgb(0, 0, 0);
        padding: 10px;
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
        background:hsl(189, 89%, 60%);
        width:75%;
        height:250px;
        border-style: double;
        margin-bottom: 20px;
        }
    #customer_contact{
        float:center; 
        background:rgb(61, 247, 133);
        width:75%;
        height:250px;
        border-style: double;
        margin-bottom: 20px;
            }
    
</style>

