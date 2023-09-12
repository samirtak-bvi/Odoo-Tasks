odoo.define("pos_training.InitialPayment", function (require) {
    'use strict';

    const Registries = require("point_of_sale.Registries");
    const ProductScreen = require("point_of_sale.ProductScreen");
    const { _lt } = require('@web/core/l10n/translation');
    const OrderLocation = require('pos_training.location');
    const { Component, xml } = owl;


    const InitialPayment = (ProductScreen) => class InitialPayment extends ProductScreen {
        setup() {
            super.setup();
        }
        async _onClickPay() {
            const order = this.env.pos.get_order()

            if (order.partner == null) {
                const { confirmed } = await this.showPopup('ConfirmPopup', {
                    title: _lt('Customer Required'),
                    body: _lt(`Customer Required to proceed further!`),
                    confirmText: _lt('Ok'),
                });
                if (confirmed) {
                    const { confirmed, payload: newPartner } = await this.showTempScreen('PartnerListScreen')
                    if (confirmed) {
                        const { confirmed } = await this.showPopup('ConfirmPopup', {
                            title: _lt('Confirmation'),
                            body: _lt(`Customer Selected: ${newPartner.name}`),
                            confirmText: _lt('Ok'),
                        });
                        if (confirmed) {
                            this.currentOrder.set_partner(newPartner);
                            this.currentOrder.updatePricelist(newPartner);
                        }
                        else {
                            this._onClickPay()
                        }
                    }
                }
            }
            else if (order.orderlines.length == 0) {
                const { confirmed } = await this.showPopup('ConfirmPopup', {
                    title: _lt('No Products'),
                    body: _lt(`Select Some Products!`),
                    cancelText: null,
                    confirmText: _lt('Ok')
                });
                // if (confirmed) {
                //     super._onClickPay()
                // }
            }
            else if (order.location == undefined){
                const { confirmed } = await this.showPopup('ConfirmPopup', {
                    title: _lt("Location Required"),
                    body: _lt(`Looks like you haven't selected order location`),
                    confirmText: _lt('Select Location'),
                });
                if (confirmed) {
                    // this.showPopup('SelectionPopup')
                    console.log()
                    // InitialPayment.template = xml`<OrderLocation />`
                    // super._onClickPay()
                }
            }
            else {
                super._onClickPay()
            }
        }
    }
    InitialPayment.components = {

    }
    Registries.Component.extend(ProductScreen, InitialPayment);
});