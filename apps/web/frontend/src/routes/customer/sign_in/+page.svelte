<script>
    import '../../+layout.svelte'

    let apiUrl = "http://localhost:8000/api/customer-login/";
    let username = '';
    let password = '';
    let status = '';
    let success = false;
    let signUpOption = false;

    function signUp(){
        window.location.href = '/customer/Sign_Up_Page_Customer'
    }

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
                        signUpOption = true
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
            <div class="stuff-box">
                <div class="form__group">
                    <label for="username" class="form__label"> Username: </label>
                    <input bind:value={username} type="text" id="username" placeholder="Username" class="form__field">
                </div>
                <br>
                <div class="form__group">
                        <label for="password" class="form__label"> Password: </label>
                         <input bind:value={password} type="password" id="password" placeholder="Password" class="form__field">
                </div>
            </div>
            <button id = "signInButton" on:click={login}>Login</button>
        
            <div>
                <p>
                    {status}
                    <!--
                    {#if signUpOption}
                        <button on:click={signUp}>Sign Up</button>
                    {/if}
                    -->
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
        text-align: center;
        font-size: xx-large;
        color: white;
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