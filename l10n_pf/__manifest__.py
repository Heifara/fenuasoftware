# -*- coding: utf-8 -*-
{
    'name': "Polynésie Française - Accounting",

    'summary': """
This is the module to manage the accounting chart for French Polynesia in Odoo.
    """,

    'description': """
This is the module to manage the accounting chart for French Polynesia in Odoo.

This module applies to companies based in French Polynesia.
    """,

    'author': "Fenua Software",
    'website': "http://www.fenuasoftware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Localization',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['l10n_fr', 'account_accountant'],

    # always loaded
    'data': [
        #data
        'data/res_currency.xml',
        'data/res_company.xml',

        #report
        'reports/vat_real_report.xml',
        'reports/vat_real_templates.xml',

        #security
        'security/ir.model.access.csv',

        #views
        'views/assets.xml',
        'views/dicp_views.xml',
        'views/report_sage_views.xml',

        #wizard
        'wizard/vat_real_report_views.xml',

    ],
}