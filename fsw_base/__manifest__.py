# -*- coding: utf-8 -*-
{
    'name': "FenuaSoftware",

    'summary': """
    """,

    'description': """
    """,

    'author': "Fenua Software",
    'website': "http://www.fenuasoftware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sample',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'qweb': [
        "static/src/xml/*.xml",
    ],
}