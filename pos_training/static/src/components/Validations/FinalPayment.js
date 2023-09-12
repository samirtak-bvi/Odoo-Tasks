odoo.define("pos_training.FinalPayment", function (require) {
    'use strict';

    const Registries = require("point_of_sale.Registries");
    const PaymentScreen = require("point_of_sale.PaymentScreen");
    const { _lt } = require('@web/core/l10n/translation');

    const FinalPayment = (PaymentScreen) => class FinalPayment extends PaymentScreen {
        setup() {
            super.setup();
        }

        async _isOrderValid(isForceValidate) {
            if (this.env.pos.get_order().partner == null) {
                this.showNotification(_lt('Select Customer to Proceed Further!'));
                return false
            }
            return super._isOrderValid(isForceValidate)
        }
    }
    Registries.Component.extend(PaymentScreen, FinalPayment);
});