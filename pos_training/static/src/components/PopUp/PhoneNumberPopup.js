odoo.define('pos_training.PhoneNumberPopup', function (require) {
    'use strict';
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const { useState, useRef } = owl;
    const { _lt } = require('@web/core/l10n/translation');
    const models = require('point_of_sale.models');
    const { PosGlobalState, Order } = require('point_of_sale.models');
    var { Gui } = require('point_of_sale.Gui');

    // models.load_fields('pos.order', ['phoneNumber']);
    console.log(models)
    class PhoneNumberPopup extends AbstractAwaitablePopup {
        setup() {
            super.setup();
            this.state = useState({ phoneNumberInput: this.props.initialNumber });
            this.phoneNumber = useRef('phoneNumber')
            this.phone = useState({
                error: "",
            })
        }

        showError(title, body){
            Gui.showPopup('ErrorPopup', {
                title: _lt(title),
                body: _lt(body)
            });
        }
        
        // async confirm() {
        //     const phno = this.phoneNumber.el.value
        //     console.log(phno)
        //     if (phno == "") {
        //         this.showError("Enter Phone Number", "Phone Number cannot be empty");
        //     }
        //     else if (phno.length != 10) {
        //         this.showError("Wrong Phone Number", "The Entered Phone Number is not 10 digits.")
        //     }
        //     else {
        //         this.phone.error = ""

        //         const loadedData = await this.env.services.rpc({
        //             model: 'pos.order',
        //             method: 'search_count',
        //             args: [[['phoneNumber', '=', this.state.phoneNumberInput]]]
        //         });
        //         console.log(this.state.phoneNumberInput)
        //         console.log(loadedData)

        //         const loadedData1 = await this.env.services.rpc({
        //             model: 'pos.order',
        //             method: 'search_read',
        //             domain: [['phoneNumber', '=', this.state.phoneNumberInput]],
        //             fields: ['partner_id']
        //         });

        //         try {
        //             this.showError('Number Already Exists',`Similar Phone Number is already registered for ${loadedData1[0].partner_id[1]}`
        //             )
        //         }
        //         catch {
        //             super.confirm();
        //         }
        //     }
        // }

        getPayload() {
            return this.state.phoneNumberInput;
        }

    }
    PhoneNumberPopup.template = 'pos_training.PhoneNumberPopup';
    PhoneNumberPopup.defaultProps = {
        confirmText: _lt('Confirm'),
        cancelText: _lt('Cancel'),
    }

    Registries.Component.add(PhoneNumberPopup);

    const PosPhoneNumber = (Order) => class PosPhoneNumber extends Order {
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
    Registries.Model.extend(Order, PosPhoneNumber);
});