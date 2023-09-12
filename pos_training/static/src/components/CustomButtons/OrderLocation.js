odoo.define('pos_training.location', function (require) {
    'use strict';
    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require('@web/core/utils/hooks')

    class OrderLocation extends PosComponent {
        setup() {
            super.setup()
            useListener('click', this.onClick);
            this.currentOrder = this.env.pos.get_order()
            this.locations_from_config = this.env.pos.locations.filter(method => this.env.pos.config.location_ids.includes(method.id));
        }
        async onClick() {
            const selectionList = this.locations_from_config.map(location => ({
                id: location.id,
                label: location.name,
                isSelected: this.currentOrder.location ? location.id === this.currentOrder.location.id : false,
                item: location
            }))
            // console.log(selectionList)
            const selectedLocationIndex = selectionList.findIndex(location => location.isSelected === true)

            if (selectedLocationIndex !== -1){
                const selectedLocation = selectionList.splice(selectedLocationIndex, 1)
                selectionList.unshift(selectedLocation[0])
            }

            const { confirmed, payload: selectedlocation } = await this.showPopup("SelectionPopup", {
                title: "Select Location",
                list: selectionList
            })
            if (confirmed) {
                const currentLocationId = this.currentOrder.location?.id;
                const selectedLocationId = selectedlocation?.id;

                if (currentLocationId !== selectedLocationId) {
                    this.currentOrder.set_location(selectedlocation);
                    this.showNotification("Selected " + selectedlocation.name)
                } else {
                    this.showNotification("Deselected " + selectedlocation.name)
                    this.currentOrder.set_location(undefined);
                }
            }
        }

    }

    OrderLocation.template = 'pos_training.LocationButton'
    ProductScreen.addControlButton({
        component: OrderLocation,
        position: ['before', 'SetFiscalPositionButton']
    });
    Registries.Component.add(OrderLocation)
});