odoo.define('pos_training.orderline_delete', function (require) {
    'use strict';
    const Orderline = require('point_of_sale.Orderline');
    // const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    // var { Gui } = require('point_of_sale.Gui');
    // const { _lt } = require('@web/core/l10n/translation');

    const OrderlineDelete = (ProductScreen) => class OrderlineDelete extends ProductScreen {
        setup() {
            super.setup();
        }
        deleteOrderline(order_to_delete){
            const order = this.env.pos.get_order()
            order.remove_orderline(order_to_delete)
        }
    }

    OrderlineDelete.template="OrderlineDelete"
    Registries.Component.extend(Orderline, OrderlineDelete)
});