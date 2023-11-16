<script>
    import '../+layout.svelte'

    let apiUrl = "http://localhost:8000/api/customer-login/";
    let username = '';
    let password = '';
    let status = '';
    let success = false

    function login(){

        if (checkInput()){
            status = '';
            fetch(apiUrl, {credentials: "include", method: 'POST', mode: "cors", headers: {"Content-Type": "application/json"} , body: JSON.stringify({username: username, password: password})})
                .then(resp => resp.json())
                .then(json => {
                    console.log(json)
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
                    if (success){
                        status = 'Login Successful'
                        window.location.href = '/customer/account'
                    }
                    else {
                        status = "Bad login, please try again or create a new account"
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
<body>
    <div>
        <h1>Customer Log-In</h1>
        {#if !success}
            <div>
                <label for="username">
                    Username: 
                </label>
                <input 
                    bind:value={username}
                    type="text"
                    id="username"
                    placeholder="Username"
                >
                <br>
                <label for="password">
                    Password: 
                </label>
                <input 
                    bind:value={password}
                    type="password"
                    id="password"
                    placeholder="Password"
                >
            </div>
            <button id = "signInButton" on:click={login}>Login</button>
        
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
        
    </div>
</body>

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

</style>