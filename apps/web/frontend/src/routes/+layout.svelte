<div id = "topBar">
  <img src="/CompanyLogo.png" alt="company logo" id="companyLogo">

  {#if showSlide }

  <!--Links and for side bar-->
  <div id="sideBar" transition:slide ={{delay:0, duration: 400, axis: 'x'}}>
      <button class = "links" on:click={home}>Home</button>
      {#if showSignOut}
      <button class = "links" on:click={signOut}> Sign Out</button>
      {/if}
      {#if droneSignIn()}
      <button class = "links" on:click={drone}> Drone Sign In</button>
      <button class = "links" on:click={drone2}> Drone Sign Up</button>
      {:else}
      <button class = "links" on:click={drone3}> Drone </button>
      {/if}
      <button class = "links" on:click={manager}>Manager</button>
      <button class = "links" on:click={contact}>Contact Manager</button>
      <button class = "links" on:click = {slideNav}> Close </button>
  </div>

  {:else}
  <!--Displays sidebar icon-->
  <button on:click={slideNav} id="sideBarIcon" transition:slide = {{delay:200, duration: 10, axis: 'x'}}> </button>
    
  {/if}
</div>

<script>
	import { onMount } from 'svelte';


  
  import { slide } from 'svelte/transition';

  let showSlide = false;

  let showSignOut = false;

  onMount(() => {
    showSignOut = checkCookie();
  })

  
  function slideNav(){
    showSlide = !showSlide 
  }

  function home(){
    window.location.href = '/'
  }

  function contact() {
    window.location.href = '/contact'
  }

  function manager(){
    let cookies = document.cookie.split('=')
    for (let cookie of cookies){
      if (cookie === 'manager-token'){
        return window.location.href = '/manager/manager_page'
      }
    }

    return window.location.href = '/manager/sign_in'
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

  function drone3(){
    window.location.href = '/drone/user'
  }

  function checkCookie(){
    let cookies = document.cookie.split(";")
    console.log(cookies)
    if (cookies[0] == ""){
      return false
    }
    else{
      return true
    }
  }

  function signOut(){
    let cookies = document.cookie.split(";")
    console.log(document.cookie)
    for (let cookie of cookies){
      let cookieName = cookie.split("=")[0]
      document.cookie = cookieName + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
    }
    home();
  }

  function droneSignIn(){
    let cookies = document.cookie.split("=")
    for (let cookie of cookies){
      if (cookie == 'owner-token'){
        return false
      }
    }
    return true
  }


</script>
  
<style>
  .links{
    background-color: aqua;
    border: none;
    width: 100%;
    height: 7%;
    font-size: large;
    font-family: system-ui;
  }

  .links:hover{
    background-color: aquamarine;
    box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;
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
    box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px; 
  }
  
  #sideBar{
    background-color: rgb(235, 107, 255);
    width: 20%;
    padding: 0%;
    margin: 0;
    height: 1000px;
    position: absolute;
    box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;

  }  
  </style>
  

<slot />