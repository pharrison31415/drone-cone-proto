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
                    if (json.hasOwnProperty('error')) {
                        throw json.error;
                    }
                    else {
                        status = json.status
                        success = json.success
                    }
                })
                .catch( err => {
                    status = err;
                })
                .finally( () => {
                    if (status == undefined){
                        status = 'Login Successful'
                        window.location.href = '/customer/account'
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

<h1>Sign In Page Customer</h1>
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
    <button on:click={login}>Login</button>

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


