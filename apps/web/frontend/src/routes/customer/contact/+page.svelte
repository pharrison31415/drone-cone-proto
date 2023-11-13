<script>
    import { onMount } from 'svelte'

    const url = 'http://localhost:8000/api';

    let error = "";

    let name = '';
    let content = '';
    let email = '';

    let width = "165px";
    
    async function postMessage() {
        fetch(url + "/new-message/", {method: "POST", mode: 'cors', "Access-Control-Allow-Origin": "*", body: JSON.stringify({content: content, email: email})})
            .then((response) => response.json())
            .then((json) => {
                if (json['success'] == false) {
                    error = "There was an error: " + json['message'];
                }
                else {
                    console.log("Message was sent.");
                }

            });
    }

    const submitMessage = () => {
        if (name != "" && content != "" && email != "") {
            console.log("not empty!");
            postMessage();
        }
        else {
            return;
        }
    }

    const resize = () => {
        let message_textArea = document.getElementById('message');
        if (width != message_textArea.style.width) {
            width = message_textArea.style.width;
        }
    }

    console.log(width);
</script>

<h1>Contact Manager</h1>
<p>{error}</p>
<form>
    <div>
        <label for="name">
            Name:
        </label>
        <input
            type="text"
            id="name"
            name="name"
            autocomplete="off"
            placeholder="Your name"
            bind:value={name}
            style:width={width}
            required
        />
    </div>

    <div>
        <label for="email">
            Email:
        </label>
        <input
            type="email"
            id="email"
            name="email"
            autocomplete="off"
            placeholder="Your email"
            bind:value={email}
            style:width={width}
            required
        />
    </div>

    <div>
        <label for="message">
            Message:
        </label>
        <textarea
            id="message"
            name="message"
            autocomplete="off"
            rows="10"
            required
            bind:value={content}
            style:width={width}
            on:mousemove={resize}
            placeholder="Message to manager goes here."></textarea>
    </div>

    <div id="button">
        <button value="Send Message" on:click={submitMessage}>Send Message</button>
    </div>

</form>

<style>
    h1 {
        text-align: center;
    }

	form {
        width: 100%;
        text-align: center;
        display: inline-flex;
        flex-direction: column;
		align-items: center;
        gap: 15px;
    }

    div {
        width: fit-content;
        display:flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
    }

    #button {
        align-items: center;
        text-align: center;
    }
    
    button {
        color: whitesmoke;
        border: 0;
        line-height: 1.5;
        text-shadow: 1px 1px 1px #000;
        border-radius: 7px;
        background-color: rgb(67, 67, 238);
        box-shadow:
            inset 2px 2px 3px rgba(255, 255, 255, 0.6),
            inset -2px -2px 3px rgba(0, 0, 0, 0.6);
    }

    button:hover {
        background-color: blue;
    }

    button:active {
        box-shadow:
            inset -2px -2px 3px rgba(255, 255, 255, 0.6),
            inset 2px 2px 3px rgba(0, 0, 0, 0.6);
    }


</style>
