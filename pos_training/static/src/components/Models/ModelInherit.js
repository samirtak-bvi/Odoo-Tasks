odoo.define('pos_training.model_inherit', function (require) {
    'use strict';
    const { PosGlobalState } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');

    const InheritModel = (PosGlobalState) => class InheritModel extends PosGlobalState {
        constructor(obj) {
            super(obj);
        }

        async _processData(loadedData) {
            super._processData(...arguments)
            this.locations = loadedData['pos.available.location']
        }
    }
    Registries.Model.extend(PosGlobalState, InheritModel);

});

