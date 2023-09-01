# -*- coding: utf-8 -*-
{
    'name': "POS TRAINING",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,    
    "application": True, 
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    "application": True,  # This line says the module is an App, and not a module
    'depends': ['point_of_sale', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/CustomerDetail.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_training/static/src/components/**/*',
        ],
    },
    "installable": True,

}
