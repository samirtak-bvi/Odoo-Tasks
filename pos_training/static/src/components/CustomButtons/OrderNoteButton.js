odoo.define('pos_training.phone_number', function (require) {
    'use strict';
    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { _lt } = require('@web/core/l10n/translation');
    const { useListener } = require('@web/core/utils/hooks')

    class OrderNote extends PosComponent {
        setup() {
            super.setup();
            this.currentOrder = this.env.pos.get_order()
            useListener('click', this.onClick);
        }

        async onClick() {
            const selectedOrder = this.currentOrder;
            if (!selectedOrder) return;
            const { confirmed, payload: inputPhone } = await this.showPopup('OrderNotePopup',
                {
                    initialNumber: selectedOrder.get_phone_number()
                });
            if (confirmed) {
                selectedOrder.set_phone_number(inputPhone)
            }
        }

        
    }

    OrderNote.template = 'CustomerOrderNote';
    ProductScreen.addControlButton({
        component: OrderNote,
        position: ['after', 'SetFiscalPositionButton']
    });
    Registries.Component.add(OrderNote)
});


