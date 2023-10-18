<h1>Contact Manager</h1>
<form method="POST">
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
            placeholder="Message to manager goes here." ></textarea>
    </div>

    <div id="button">
        <input type="submit" value="Send Message"/>
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
    
    #button > input {
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

    #button > input:hover {
        background-color: blue;
    }

    #button > input:active {
        box-shadow:
            inset -2px -2px 3px rgba(255, 255, 255, 0.6),
            inset 2px 2px 3px rgba(0, 0, 0, 0.6);
    }


</style>
