odoo.define('pos_training.RemoveProducts', function (require) {
    'use strict';
    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { _lt } = require('@web/core/l10n/translation');
    const { useListener } = require('@web/core/utils/hooks')

    class RemoveProducts extends PosComponent {
        setup() {
            super.setup();
            this.currentOrder = this.env.pos.get_order()
            useListener('click', this.onClick);
        }

        async onClick() {
            const orderlines = this.currentOrder.orderlines
            const l = orderlines.length
            for (let i = 0; i < l; i++) {
                orderlines.pop()
            }
        }
    }

    RemoveProducts.template = 'RemoveProducts';
    ProductScreen.addControlButton({
        component: RemoveProducts,
        position: ['after', 'SetFiscalPositionButton']
    });
    Registries.Component.add(RemoveProducts)
});