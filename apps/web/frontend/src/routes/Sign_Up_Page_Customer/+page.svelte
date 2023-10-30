<script>
    let apiUrl = "http://127.0.0.1:8000/api/new-customer/";
    let firstName = '';
    let lastName = '';
    let username = '';
    let password = '';
    let confirmPassword = ''; 

    function createAccount(){
        var newDiv = document.createElement('div');
        var divContent = document.createElement('p');

        if (confirmPassword == password){
            print("test")
            fetch(apiUrl, {method: 'POST', mode: "cors", headers: {"Content-Type": "application/json"} , body: JSON.stringify({firstName: firstName, lastName: lastName, username: username, password: password})})
                .then(resp => resp.json())
                .then(json => {
                    if (json.hasOwnProperty('error')) {
                        throw json.error;
                    }
                    else {
                        divContent.textContent = json.value
                    }
                })
                .catch( err => {
                    divContent.textContent = err;
                })
                .finally( () => {
                    newDiv.appendChild(divContent)
                    document.getElementById(id = "button").append(newDiv)
                })
        }
    }


</script>

<h1>Sign Up Page Customer</h1>

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
    <div id = "button">
    <button on:click={createAccount}>Create Account</button>

    </div> 


