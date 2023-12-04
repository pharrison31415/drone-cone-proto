<script>
    import '../../+layout.svelte'

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
                        window.location.href = "/customer/sign_in"

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
                <div class="form__group">
                    <label for="firstName" class="form__label"> First Name: </label>
                     <input bind:value={firstName} type="text" id="firstName" placeholder="First Name" class="form__field">
                </div>
                <div class="form__group">
                    <label for="lastName" class="form__label"> Last Name: </label>
                     <input bind:value={lastName} type="text" id="lastName" placeholder="Last Name" class="form__field">
                </div>
                <div class="form__group">
                    <label for="username" class="form__label"> Username: </label>
                     <input bind:value={username} type="text" id="username" placeholder="Username" class="form__field">
                </div>
                <div class="form__group">
                    <label for="password" class="form__label"> Password: </label>
                     <input bind:value={password} type="password" id="password" placeholder="Password" class="form__field">
                </div>
                <div class="form__group">
                    <label for="confirmPassword" class="form__label"> Confirm Password: </label>
                     <input bind:value={confirmPassword} type="password" id="confirmPassword" placeholder="Confirm Password" class="form__field">
                </div>
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
        font-family: "Poppins", sans-serif;

    }

    div{
        text-align: center;
        margin: 50px;
    }
    p{
        font-family: "Poppins", sans-serif;
    }

    .form__group{
        width: 75%;
        height: 60px;
        margin-left: 12%;
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

    #signUpButton{
        background-color: rgb(90, 164, 255);
        height: 75px;
        width: 200px;
        border-radius: 10px;
        text-align: center;
        font-size: x-large;
        font-weight: bold;
    }

    #signUpButton:hover{
        background-color: rgb(230, 255, 130);
    }
</style>