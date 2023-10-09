<h1>Tracking Order#: ???????</h1>
<div id="order_tracking">
    <p id="time_order">Order Date: MM/DD/YYYY HH:MM</p>
    <p id="delivery_order">Delivered/Arriving: TIME</p>
    <p id="cost_order">Order Total: $?????? (# cones)</p>
    <div id="content_order">
        <div id="cone">
            <div class="details">
                <ul>
                    <li>Cone: ????</li>
                    <li>Scoops:
                        <ul>
                            <li>option</li>
                            <li>option</li>
                            <li>option</li>
                        </ul>
                    </li>
                    <li>Toppings:
                        <ul>
                            <li>options.</li>
                            <li>options.</li>
                            <li>options.</li>
                        </ul>
                    </li>
                </ul>
            </div>
            <div id="buttons">
                <p class="quantity">Qty. ??</p>
                <div>
                    <p><span class="add_to_cat_icon">h</span><p></p>
                    <button class="add_to_cart" type="button">Add to Cart</button>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
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