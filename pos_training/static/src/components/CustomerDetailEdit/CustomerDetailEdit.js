odoo.define("pos_training.CustomerDetail", function (require) {
    'use strict';

    const PartnerDetailsEdit = require("point_of_sale.PartnerDetailsEdit");
    const Registries = require("point_of_sale.Registries");
    var { Gui } = require('point_of_sale.Gui');
    const { _lt } = require('@web/core/l10n/translation');

    const CustomerMobile = (PartnerDetailsEdit) => class CustomerMobile extends PartnerDetailsEdit {
        setup() {
            super.setup();
            this.changes.mobile_no = this.props.partner.mobile_no || ""
            console.log(this.changes);
        }
        
        async saveChanges() {
            console.log()
            const loadedData = await this.env.services.rpc({
                model: 'res.partner',
                method: 'search_read',
                args: [[['mobile_no', '=', this.changes.mobile_no], ["id", "!=", this.props.partner.id]]]
            });
            // console.log(loadedData)

            if (loadedData.length > 0) {
                Gui.showPopup('ErrorPopup', {
                    title: _lt('Mobile Number'),
                    body: _lt(`Mobile Number already registered for ${loadedData[0].name}!!`)
                });            
            }
            else{
                super.saveChanges()
            }
        }
    }
    CustomerMobile.template = 'pos_training.CustomerMobile'
    Registries.Component.extend(PartnerDetailsEdit, CustomerMobile);
    return CustomerMobile;
});