odoo.define('pos_training.training', function (require) {
    "use strict";
    
    // const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Chrome = require('point_of_sale.Chrome')
    const Registries = require('point_of_sale.Registries');
    const { useState, useSubEnv } = owl;
    var { Gui } = require('point_of_sale.Gui');
    const { _lt } = require('@web/core/l10n/translation');


    const Training = (Chrome) => class Training extends Chrome{
        setup() {
            useSubEnv({key:'value'})
            console.log(this.env.pos)
            // console.log(this.env.services)
            super.setup();
        }

        display() {
            // console.log('HELLO')
            Gui.showPopup("ConfirmPopup", {
                title: _lt("Hello There"),
                body: _lt("Nothing Much to show"),
                confirmText: _lt("Close it?"),
                cancelText: _lt("Don't Close it.")
            })
        }
    }

    Training.template = 'pos_training.training';
    Registries.Component.extend(Chrome, Training);

    return Training;
});