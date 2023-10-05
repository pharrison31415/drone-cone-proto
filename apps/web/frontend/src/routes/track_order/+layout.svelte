<style>
    body {
        display: flex;
        justify-content: center;
    }

    h1 {
        text-align: center;
    }

    #buttons {
        height: fit-content;
        text-align: right;
    }

    #cone {
        display:grid;
        grid-template-columns: 3fr 1fr;
        border: solid 0.1em;
    }
    #buttons>div>p {
        padding:0em;
        margin:0em;
        text-align:center;
    }

    div {
        padding:.1em;
        /*border: solid;*/
    }
    div>ul {
        list-style:none;
        padding-left:.5em;
    }

    ul>li>ul {
        list-style: disc;
    }
</style>