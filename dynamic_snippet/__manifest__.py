# -*- coding: utf-8 -*-
{
    'name': "dynamic_snippet",

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
    'application' : True,
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/snippets/snippets.xml',
        'views/snippets/s_EmployeeDetail.xml'
    ],

    # 'assets': {
    # 'website.assets_wysiwyg': [
    #         ('include', 'web._assets_helpers'),
    #         'dynamic_snippet/static/src/snippets/s_EmployeeDetail/options.js'
    # ]
    # }
}
