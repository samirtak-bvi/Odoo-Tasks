odoo.define('pos_training.OrderNotePopup', function (require) {
    'use strict';
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const { useState, useRef } = owl;
    const { _lt } = require('@web/core/l10n/translation');
    var { Gui } = require('point_of_sale.Gui');
    class OrderNotePopup extends AbstractAwaitablePopup {
        setup() {
            super.setup();
            this.state = useState({ phoneNumberInput: this.props.initialNumber });
            this.phoneNumber = useRef('phoneNumber')
            this.phone = useState({
                error: "",
            })
        }

        showError(title, body) {
            Gui.showPopup('ErrorPopup', {
                title: _lt(title),
                body: _lt(body)
            });
        }
        getPayload() {
            return this.state.phoneNumberInput;
        }

    }
    OrderNotePopup.template = 'pos_training.OrderNotePopup';
    OrderNotePopup.defaultProps = {
        confirmText: _lt('Confirm'),
        cancelText: _lt('Cancel'),
    }

    Registries.Component.add(OrderNotePopup);

});