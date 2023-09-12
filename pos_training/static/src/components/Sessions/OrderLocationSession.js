odoo.define('pos_training.locationsession', function (require) {
    'use strict';
    const Registries = require('point_of_sale.Registries');
    const { Order } = require('point_of_sale.models');
const OrderLocation = (Order) => class extends Order {
    constructor(obj, options) {
        super(...arguments);
    }

    set_location(location) {
        this.location = location;
    }
    get_location() {
        return this.location;
    }
    init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        this.set_location(json.location);
    }

    export_as_JSON() {
        const result = super.export_as_JSON(...arguments);
        result.location = this.location;
        return result;
    }

    export_for_printing() {
        const result = super.export_for_printing(...arguments);
        if (this.get_location()) {
            result.location = this.get_location().name;
        }
        // result.mobile_no = this.partner.mobile_no
        return result;
    }

}
Registries.Model.extend(Order, OrderLocation);
});