<script>
    let apiUrl = "http://localhost:8000/api/owner-login/";
    let username = '';
    let password = '';
    let status = '';
    let success = false

    // function login(){
    //     window.location.href = "/drone_user"
    // }

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
                        window.location.href = '/drone/user'
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
    <br>
    <h1>Drone Operator Sign-In</h1>
    {#if !success}
        <div>
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
        </div>
        
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

<style>
    body {
        background-color: rgb(195, 33, 254);
        margin: 0%;
        font-family: "Poppins", sans-serif;
    }

    h1{
        text-align: center;
        font-size: xx-large;
        color:white
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


