<div id = "topBar">
    
    {#if showSlide }
    <div id="sideBar" transition:slide ={{delay: 250, duration: 300, axis: 'x'}} >
        <ul>  
            <li> <button on:click={slideNav} class="button-19"> back </button> </li>
            <li> <a href="/" on:click={slideNav}>home</a> </li>
            <li> <a href="/contact" on:click={slideNav}>contact</a> </li>
            <li> <a href="/track_order" on:click={slideNav}>track Order</a> </li>
            <li> <a href="/account" on:click={slideNav}>account</a> </li>
            <li> <a href="/Manager_Page" on:click={slideNav}>Manager Page</a> </li>
            <li> <a href="Sign_Up_Page_Drone" on:click={slideNav}>Drone Sign Up</a>  </li>
        </ul>
    </div>

    {:else}
    <button on:click={slideNav} class="button-19"> test  </button>
    
    {/if}

</div>


<script>
  import { slide } from 'svelte/transition';

  let showSlide = false;
  
   function slideNav(){
    showSlide = !showSlide 
  }
 

</script>
  
<style>

  #topBar{
    background-color: pink;
    width: 100%;
    height: 150px;

  }
  
  #sideBar{
    background-color: rgb(255, 0, 43);
    width: 25%;
    padding: 0%;
    margin: 0;
    height: 1000px;
    text-align: center;
    position: absolute;
  }  
  .button-19 {
    appearance: button;
    background-color: #1899D6;
    border: solid transparent;
    border-radius: 16px;
    border-width: 0 0 4px;
    box-sizing: border-box;
    color: #FFFFFF;
    cursor: pointer;
    display: inline-block;
    font-family: din-round,sans-serif;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: .8px;
    line-height: 20px;
    margin: 0;
    outline: none;
    overflow: visible;
    padding: 13px 16px;
    text-align: center;
    text-transform: uppercase;
    touch-action: manipulation;
    transform: translateZ(0);
    transition: filter .2s;
    user-select: none;
    -webkit-user-select: none;
    vertical-align: middle;
    white-space: nowrap;
    width: 10%;
  }
  
  .button-19:after {
    background-clip: padding-box;
    background-color: #1CB0F6;
    border: solid transparent;
    border-radius: 16px;
    border-width: 0 0 4px;
    bottom: -4px;
    content: "";
    left: 0;
    position: absolute;
    right: 0;
    top: 0;
    z-index: -1;
  }
  
  .button-19:main,
  .button-19:focus {
    user-select: auto;
  }
  
  .button-19:hover:not(:disabled) {
    filter: brightness(1.1);
    -webkit-filter: brightness(1.1);
  }
  
  .button-19:disabled {
    cursor: auto;
  }
  
  </style>
  

<slot />