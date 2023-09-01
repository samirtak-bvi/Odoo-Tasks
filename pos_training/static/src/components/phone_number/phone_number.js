odoo.define('pos_training.phone_number', function (require) {
    'use strict';
    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    var { Gui } = require('point_of_sale.Gui');
    const { _lt } = require('@web/core/l10n/translation');

    const PhoneNumber = (ProductScreen) => class PhoneNumber extends ProductScreen {
        setup() {
            super.setup();
        }
        async onClick() {
            const selectedOrder = this.env.pos.get_order();
            if (!selectedOrder) return;

            // console.log(order)
            const { confirmed, payload: inputPhone } = await this.showPopup('PhoneNumberPopup',
                {
                    initialNumber: selectedOrder.get_phone_number()
                });

            if (confirmed) {
                selectedOrder.set_phone_number(inputPhone)
            }
        }
        async _onClickPay() {
            // console.log(this.env.pos.get_order().partner==null)
            if (this.env.pos.get_order().partner==null) {
                Gui.showPopup('ErrorPopup', {
                    title: _lt('Customer'),
                    body: _lt(`Please select a customer before proceeding!`)
                });
            }
            else {
                super._onClickPay()
            }
        }
    }

    PhoneNumber.template = 'CustomerPhoneNumber';
    Registries.Component.extend(ProductScreen, PhoneNumber);

    return PhoneNumber;

});


//     const PosComponent = require('point_of_sale.PosComponent');
//     const ProductScreen = require('point_of_sale.ProductScreen');
//     const { useListener } = require("@web/core/utils/hooks");
//     const Registries = require('point_of_sale.Registries');

//     class CustomerPhoneNumber extends PosComponent {
//         setup() {
//             super.setup();
//             useListener('click', this.onClick);
//         }
//         async onClick() {
//             const selectedOrderline = this.env.pos.get_order().get_selected_orderline();
//             if (!selectedOrderline) return;

//             const { confirmed, payload: inputNote } = await this.showPopup('TextAreaPopup', {
//                 startingValue: selectedOrderline.get_customer_note(),
//                 title: this.env._t('Enter Phone Number'),
//             });

//             if (confirmed) {
//                 selectedOrderline.set_customer_note(inputNote);
//             }
//         }
//     }
//     CustomerPhoneNumber.template = 'CustomerPhoneNumber';

//     ProductScreen.addControlButton({
//         component: CustomerPhoneNumber,
//     });

//     Registries.Component.add(CustomerPhoneNumber);

//     return CustomerPhoneNumber;
// });
