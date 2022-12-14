# -*- coding: utf-8 -*-
{
    'name': "Test imagen",

    'summary': """
       Valida e indica donde puede existir errores de timbrado""",

    'description': """
        Valida direcciones basándose en el CP y datos adicionales
    """,

    'author': "Gerardo Soto (gera)",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        #'views/views.xml',
        #'templates.xml',
    ],
    
    "external_dependencies": {"python": ['numpy']},
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
