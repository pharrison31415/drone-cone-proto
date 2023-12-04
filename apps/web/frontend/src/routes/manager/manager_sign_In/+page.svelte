<body>
    <h1>Manager Login Page</h1>
    {#if !success}
        <div class="form__group">
            <label for="username" class="form__label"> Username: </label>
            <input bind:value={username} type="text" id="username" placeholder="Username" class="form__field">
        </div>
        <br>
        <div class="form__group">
            <label for="password" class="form__label"> Password: </label>
            <input bind:value={password} type="password" id="password" placeholder="Password" class="form__field">
        </div>
        <button on:click={login} class="loginButton">Login</button>

        <div>
            <p>
                {status}
            </p>
        </div>
    {:else}
        <div>
            <p>
                {status}
            </p>
        </div>
    {/if}

</body>

<script>
	import { onMount } from "svelte";

    let apiUrl = "http://localhost:8000/api/manager-login/";
    let username = '';
    let password = '';
    let status = '';
    let success = false


    function login(){
        var newDiv = document.createElement('div');
        var divContent = document.createElement('p');

        if (checkInput()){
            status = '';
            fetch(apiUrl, {method: 'POST',credentials: "include", mode: "cors", headers: {"Content-Type": "application/json"} , body: JSON.stringify({username: username, password: password})})
                .then(resp => resp.json())
                .then(json => {
                    if (json.hasOwnProperty('error')) {
                        throw json.error;
                    }
                    else {
                        status = json.message
                        success = json.success
                    }
                })
                .catch( err => {
                    status = err;
                })
                .finally( () => {
                    if (status == undefined){
                        status = 'Login Successful'
                        window.location.href = '/manager/manager_page'
                    }
                })
        }
    }

    function checkInput(){
        if (username == '') {
            status = "Please provide a Username"
            return false
        }
        if (password == ''){
            status = "Please provide a Password"
            return false
        }
            return true
    }


</script>

<style>
    body {
        background-color: rgb(33, 122, 254);
        margin: 0%;
        font-family: "Poppins", sans-serif;
    }

    h1{
        text-align: center;
        font-size: xx-large;
    }

    p{
        text-align: center;
        font-size: xx-large;
        color: white;
    }


    .form__group{
        width: 75%;
        height: 60px;
        margin-left: 15%;
        margin-bottom: 10px;
        margin-top: 5px;
        text-align: center;
        grid-template-rows: 100px 2;
        display: grid;
    }

    .form__field{
        font-size: large;
        width: 500px;
        margin-left: 22%;
        border-radius: 10px;
    }

    .form__field:focus::-webkit-input-placeholder{
        opacity: 0;
    }

    .form__label{
        width: 16rem;
        font-size: medium;
        margin-left: 22%;
        text-align: left;
    }

    .loginButton{
        background-color: aquamarine;
        height: 75px;
        width: 200px;
        border-radius: 10px;
        text-align: center;
        font-size: x-large;
        font-family: Verdana, sans-serif;
        font-weight: bold;
        margin-left: 42%;
        margin-top: 20px;
        
    }

    .loginButton:hover{
        background-color: rgb(249, 255, 83);
        height: 75px;
        width: 200px;
        border-radius: 10px;
        text-align: center;
        font-size: x-large;
        font-family: Verdana, sans-serif;
        font-weight: bold;
        margin-left: 42%;
        margin-top: 20px;
        
    }

</style>


