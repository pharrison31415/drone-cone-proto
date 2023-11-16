<script>
    import '../+layout.svelte'

    let apiUrl = "http://127.0.0.1:8000/api/new-customer/";
    let firstName = '';
    let lastName = '';
    let username = '';
    let password = '';
    let confirmPassword = ''; 
    let status = '';
    let success = false

    function createAccount(){
        var newDiv = document.createElement('div');
        var divContent = document.createElement('p');

        if (checkInput()){
            status = '';
            fetch(apiUrl, {method: 'POST', mode: "cors", headers: {"Content-Type": "application/json"} , body: JSON.stringify({firstName: firstName, lastName: lastName, username: username, password: password})})
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
                        status = 'Account created! Please sign in.'
                    }
                })
        }
    }

    function checkInput(){
        if (firstName == '') {
            status = 'Please provide your First Name'
            return false
        }
        if (lastName == '') {
            status = "Please provide your Last Name"
            return false
        }
        if (username == '') {
            status = "Please provide a Username"
            return false
        }
        if (password == ''){
            status = "Please provide a Password"
            return false
        }
        if (password.length < 8){
            status = "Password must be 8 characters or greater"
            return false
        }
        if (confirmPassword == ''){
            status = "Please confirm your password"
            return false
        }
        if (password != confirmPassword){
            status = "Passwords do not match, please try again"
            return false
        }
        return true


    }


</script>

<body>
    <div>
        <h1>Customer Sign Up</h1>
        {#if !success}
            <div>
                <label for="firstName">
                    First Name:
                </label>
                <input 
                    bind:value={firstName}
                    type="text" 
                    id="firstName"
                    placeholder="First Name"
                >
                <br>
                <label for="lastName">
                    Last Name:
                </label>
                <input 
                    bind:value={lastName}
                    type="text"
                    id="lastName"
                    placeholder="Last Name"
                >
                <br>
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
                <br>
                <label for="confirm-password">
                    Confirm Password: 
                </label>
                <input 
                    bind:value={confirmPassword}
                    type="password"
                    id="confirm-password"
                    placeholder="Confirm Password"
                >
            </div>
            <button id = "signUpButton" on:click={createAccount}>Create Account</button>
        
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
</style>