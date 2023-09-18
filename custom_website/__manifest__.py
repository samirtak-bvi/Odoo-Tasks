# -*- coding: utf-8 -*-
{
    'name': "custom_website",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/test.xml',
        'views/webpage/custom_webpage.xml',
        'views/snippets/snippets.xml',
        # 'views/snippets/s_Slider.xml',
        'views/customer_query.xml'
    ],
    'assets': {
    'web.assets_frontend': [
        'custom_website/static/src/custom_webpage/custom_webpage.js',
        'custom_website/static/src/custom_webpage/modal.xml',
        'custom_website/static/src/custom_webpage/modal.scss'
    ]
    }
}
