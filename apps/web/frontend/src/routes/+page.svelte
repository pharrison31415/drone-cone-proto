<body> 
    <div>
        <div>
        <p> New to Drones Cones Sign Up</p>
        <button id = "signUpButton" on:click={signUp}> Sign Up</button>
        </div>
        <div>
            
        <div>
        <button id = "signInButton" on:click={signIn}> Sign In</button>
        <p> For Returning Customer</p>
        </div>
        
        
        <div>
        <button id = "orderButton" on:click={order}> Order Now!</button>
        <p> Continue as Guest</p>
        </div> 
    </div>
</body>

<script>
	import { onMount } from "svelte";

    onMount(()=>{
        checkCookie();
    });

    function signIn (){
        window.location.href = 'customer/sign_in'
    }

    function signUp (){
        window.location.href = 'customer/sign_up'
    }

    function order(){
        window.location.href = 'customer/order-guest'
    }

    function checkCookie(){
    let cookies = document.cookie.split('=')
        for (let cookie of cookies){
            if (cookie === 'customer-token'){
                return window.location.href = '/customer/account'
            }
        }
    }


</script>

<style>
    body{
        background-color: rgb(180, 255, 255);
        margin: 0%;
    }

    div{
        text-align: center;
        margin: 50px;
    }
    p{
        font-family: verdana, sans-serif;
    }
    #signInButton{
        background-color: aquamarine;
        height: 75px;
        width: 200px;
        border-radius: 10px;
        text-align: center;
        font-size: x-large;
        font-family: Verdana, sans-serif;
        font-weight: bold;
        
    }
    
    #signInButton:hover{
        background-color: rgb(230, 255, 130);
    }

    #signUpButton{
        background-color: rgb(90, 164, 255);
        height: 75px;
        width: 200px;
        border-radius: 10px;
        text-align: center;
        font-size: x-large;
        font-family: Verdana, sans-serif;
        font-weight: bold;
    }

    #signUpButton:hover{
        background-color: rgb(230, 255, 130);
    }


    #orderButton{
        background-color: rgb(255, 90, 90);
        height: 75px;
        width: 200px;
        border-radius: 10px;
        text-align: center;
        font-size: x-large;
        font-family: Verdana, sans-serif;
        font-weight: bold;
    }

    #orderButton:hover{
        background-color: rgb(249, 255, 73);
    }
</style>