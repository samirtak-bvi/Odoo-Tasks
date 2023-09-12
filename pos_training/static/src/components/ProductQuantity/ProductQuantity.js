// odoo.define('pos_training.ProductQuantityValidation', function (require) {
//     "use strict";
    
//     // const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
//     const OrderSummary = require('point_of_sale.OrderSummary')
//     const Registries = require('point_of_sale.Registries');

//     const QuantityCheck = (OrderSummary) => class extends OrderSummary{
//     getTotal(){
//         for (let o of this.env.pos.get_order().orderlines){
//             console.log(o.product.qty_available - o.quantity)
//             if (o.product.qty_available - o.quantity < 0){
//                 this.showNotification('Quantity Out Of Stock!!')
//             }
//             else{
//                 return super.getTotal();
//             }
//         }
//     }
//     }
//     Registries.Component.extend(OrderSummary, QuantityCheck);
// });