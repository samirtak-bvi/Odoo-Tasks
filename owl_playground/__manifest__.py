# -*- coding: utf-8 -*-
{
    'name': "owl_playground",

    'summary': """
        Play with Owl in this playground module""",

    'description': """
        Play with Owl in this playground module
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com",
    "license": "LGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],
    'application': True,
    'installable': True,
    'data': [
        'views/SaleDetails.xml',
        'views/snippets/s_customBanner.xml',
        'views/snippets/s_customCarousel.xml',
        'views/snippets/snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'owl_playground/static/src/scss/banner.scss'
        ],
        
    }
}
