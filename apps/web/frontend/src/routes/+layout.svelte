<div id = "topBar">
  <img src="/CompanyLogo.png" alt="company logo" id="companyLogo">

  {#if showSlide }

  <!--Links and for side bar-->
  <div id="sideBar" transition:slide ={{delay:0, duration: 400, axis: 'x'}}>
      <button class = "links" on:click={home}>Home</button>
      <button class = "links" on:click={drone}> Drone Sign In</button>
      <button class = "links" on:click={drone2}> Drone Sign Up</button>
      <button class = "links" on:click={manager}>Manager</button>
      <button class = "links" on:click = {slideNav}> Close </button>
  </div>

  {:else}
  <!--Displays sidebar icon-->
  <button on:click={slideNav} id="sideBarIcon" transition:slide = {{delay:200, duration: 10, axis: 'x'}}> </button>
    
  {/if}
</div>

<script>

  
  import { slide } from 'svelte/transition';

  let showSlide = false;



  
  function slideNav(){
    showSlide = !showSlide 
  }

  function home(){
    window.location.href = '/'
  }

  function manager(){
    let cookies = document.cookie.split('=')
    for (let cookie of cookies){
      if (cookie === 'manager-token'){
        return window.location.href = '/manager/manager_page'
      }
    }

    return window.location.href = '/manager/manager_sign_In'
  }

  function customers(){
    window.location.href = '/customer/account'
  }

  function drone(){
    window.location.href = '/drone/sign_in'
  }

  function drone2(){
    window.location.href = '/drone/sign_up'
  }

  function signIn(){
    window.location.href = '/customer/Sign_In_Page'
  }

  function signUp(){
    window.location.href = '/customer/Sign_Up_Page_Customer'
  }
</script>
  
<style>
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
    background-color: rgb(235, 107, 255);
    width: 15%;
    padding: 0%;
    margin: 0;
    height: 1000px;
    position: absolute;
  }  
  </style>
  

<slot />