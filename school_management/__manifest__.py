{
    "name": "School Management",
    "version": "16.0",
    "application": True,
    "depends": ["base", "mail"],
    "data": [
        'security/ir.model.access.csv',
        # 'data/data.xml',
        'views/school_class.xml',
        'views/teacher_information.xml',
        'views/school_information.xml',
        'views/parent_information.xml',
        'views/student_information.xml',
        'views/school_menus.xml',
    ],
    "installable": True,
    "license" : "LGPL-3",
}
