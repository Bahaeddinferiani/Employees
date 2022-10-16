# -*- coding: utf-8 -*-
{
    'name': "gestion_ics",

    'summary': """Gestion des employées de ics""",

    'description': """
        Cette module vous permet de gérer vos emplpyées 
    """,

    'author': "Infotech consulting services",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
         'views/employee.xml',
        'views/heures.xml',

        'views/employeegraph.xml',
        'reports/report_employee.xml',
        'reports/report.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}