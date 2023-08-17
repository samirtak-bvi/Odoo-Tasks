{
    "name": "Estate",  # The name that will appear in the App list
    "version": "1.1.2",  # Version
    "application": True,  # This line says the module is an App, and not a module
    # dependencies
    "depends": ["base", "sale", "mail", "excel_report_designer"],
    "summary": "A basic Property Estate Module",
    "author": "Samir Tak",
    "support": "BVI",
    "data": [
        'security/ir.model.access.csv',
        'views/estate_property_offer_views.xml',
        'views/estate_property_info_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        'views/estate_settings.xml',
        'views/estate_cancel_property.xml',
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml',
        'data/estate_mail_template.xml',
        'data/cron.xml',
    ],
    'assets': {'web.assets_backend': ['excel_report_designer/static/src/js/action_manager.js',]},

    "installable": True,
    "license": "LGPL-3",
}
