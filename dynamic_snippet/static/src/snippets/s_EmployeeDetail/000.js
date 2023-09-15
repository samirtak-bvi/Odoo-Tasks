/** @odoo-module **/
import publicWidget from "web.public.widget"
import core from 'web.core'

var Qweb = core.qweb
publicWidget.registry.DynamicEmployeeCarousel = publicWidget.Widget.extend({
    selector: '.s_EmployeeDetail',

    start() {
        this._rpc({
            route: "/employee/detail",
            params: {}
        }).then((data) => {
            this.$target.replaceWith(Qweb.render("dynamic_snippet.s_carousel_EmployeeDetail", {data: data}))
            console.log('Done')
        });
    }
});
export default publicWidget.registry.DynamicEmployeeCarousel;