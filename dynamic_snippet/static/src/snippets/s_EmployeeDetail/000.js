odoo.define('dynamic_snippet.s_EmployeeDetail', function (require) {
    'use strict';
    
    const publicWidget = require('web.public.widget');
    const DynamicSnippet = require('website.s_dynamic_snippet');
    const config = require('web.config');
    
    const DynamicEmployeeCarousel = DynamicSnippet.extend({
        selector: '.s_EmployeeDetail',
        /**
         * @override
         */
        init: function (uiFragment) {
            this._super.apply(this, arguments);
            this.template_key = 'dynamic_snippet.s_carousel_EmployeeDetail';

            console.log(uiFragment)
        },
    
        //--------------------------------------------------------------------------
        // Private
        //--------------------------------------------------------------------------
        
        /**
         * @override
         */
        _getQWebRenderOptions: function () {
            return Object.assign(
                this._super.apply(this, arguments),
                {
                    interval: parseInt(this.$target[0].dataset.carouselInterval),
                    rowPerSlide: parseInt(config.device.isMobile ? 1 : this.$target[0].dataset.rowPerSlide || 1),
                    arrowPosition: this.$target[0].dataset.arrowPosition || '',
                },
            );
        },
    });
    publicWidget.registry.dynamic_snippet_employees_carousel = DynamicEmployeeCarousel;
    
    return DynamicEmployeeCarousel;
    });
    