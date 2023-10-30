<div id = "topBar">
  <img src="/CompanyLogo.png" alt="company logo" id="companyLogo">

  {#if showSlide }

  <!--Links and for side bar-->
  <div id="sideBar" transition:slide ={{delay:0, duration: 400, axis: 'x'}}>
      <button class = "links" on:click={home}>Home</button>
      <button class = "links" on:click={customers}> Users Accounts </button>
      <button class = "links" on:click={drone}> Drone Operator</button>
      <button class = "links" on:click={manager}>Manager</button>
      <button class = "links" on:click = {slideNav}> Close </button>
  </div>

  {:else}
  <!--Displays sidebar icon-->
  <button on:click={slideNav} id="sideBarIcon" transition:slide = {{delay:200, duration: 10, axis: 'x'}}> </button>
    
  {/if}

  {#if !signedIn}
  <div class = "signButtons">
  <button id = "signUpButton"> Sign Up </button>
  <button> Sign In </button>
  </div>
  {/if}

</div>


<script>
  import { slide } from 'svelte/transition';

  let showSlide = false;

  let signedIn = false;
  
  function slideNav(){
    showSlide = !showSlide 
  }

  function home(){
    window.location.href = '/'
  }

  function manager(){
    window.location.href = '/Manager_Page'
  }

  function customers(){
    window.location.href = '/customer/account'
  }

  function drone(){
    window.location.href = '/drone_user'
  }
</script>
  
<style>

  .signButtons{
    margin-left: 80%;
    margin-top: 2%;
    position: absolute;
  }

  .links{
    background-color: aqua;
    border: none;
    width: 100%;
    height: 5%;
    font-size: large;
    font-family: system-ui;
  }

  .links:hover{
    background-color: aquamarine;
    box-shadow: 0 12px 16px 0 rgba(255, 178, 178, 0.24), 0 17px 50px 0 rgba(255, 255, 255, 0.19);
  }

  #signUpButton{
    margin: 20px;
    background-color: blueviolet;
  }

  #sideBarIcon{
    background: url("/sideBarIcon.png");
    width: 48px;
    height: 48px;
    margin: 10px;
    border: none;
    position: absolute;
  }
  #companyLogo{
    width: 681px;
    height: 121px;
    flex-shrink: 0;
    position: absolute;
    left: 25%;
  }

  #topBar{
    background-color: #FFA9DD;
    width: 100%;
    height: 121px;
  }
  
  #sideBar{
    background-color: rgb(255, 255, 255);
    width: 15%;
    padding: 0%;
    margin: 0;
    height: 1000px;
    position: absolute;
  }  
  </style>
  

<slot />