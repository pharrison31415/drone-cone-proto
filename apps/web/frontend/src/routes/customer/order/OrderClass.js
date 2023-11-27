export class Order {
    constructor() {
    this.cart = [];
    };

    //Add to Order list
    addtoOrder(cone){
    this.cart.push(cone);
    };

    getCart(){
        return this.cart
    };

    //Removes Specific Cone from the order page
    removeCone(id){
        let newArray = this.cart.filter(obj=> obj.id !== id);
        this.cart = newArray;  
    }
}