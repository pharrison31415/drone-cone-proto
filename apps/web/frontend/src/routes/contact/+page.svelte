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
            message:
        </label>
        <textarea
            id="message"
            name="message"
            autocomplete="off"
            rows="10"
            placeholder="Message to manager goes here."
            required>
        </textarea>
    </div>

    <div>
        <input type="submit" value="Send Message"/>
    </div>

</form>
