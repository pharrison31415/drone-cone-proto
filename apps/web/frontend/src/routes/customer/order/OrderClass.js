export class Order {
    constructor() {
    this.cart = [];
    }

    //Add to Order list
    addtoOrder(cone){
    this.cart.push(cone)
    }
}