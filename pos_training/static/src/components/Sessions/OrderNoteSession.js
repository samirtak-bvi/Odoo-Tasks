odoo.define('pos_training.OrderNoteSession', function (require) {
    'use strict';
    const Registries = require('point_of_sale.Registries');
    const { Order } = require('point_of_sale.models');

    const PosOrderNote = (Order) => class extends Order {
        constructor(obj, options) {
            super(...arguments);
        }

        set_phone_number(phoneNumber) {
            this.phoneNumber = phoneNumber;
        }
        get_phone_number() {
            return this.phoneNumber;
        }
        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            this.set_phone_number(json.phoneNumber);
        }

        export_as_JSON() {
            const result = super.export_as_JSON(...arguments);
            result.phoneNumber = this.phoneNumber;
            return result;
        }

        export_for_printing() {
            const result = super.export_for_printing(...arguments);
            if (this.get_phone_number()) {
                result.phoneNumber = this.get_phone_number();
            }
            result.mobile_no = this.partner.mobile_no
            return result;
        }
    }
    Registries.Model.extend(Order, PosOrderNote);
});