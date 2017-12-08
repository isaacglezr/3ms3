# -*- coding: utf-8 -*-
{
    'name': "Employee Privacity Report",
    'description': """This Module Gives PDF Report of Privacity Form.""",
    'description': """This Module Gives PDF Report of Privacity Form.""",
    "category": "Generic Modules/Human Resources",
    'version': '0.1',
    'author': "E&G Tech System",
    'company': "E&G Tech System",
    'website': "",
    'depends': ['base', 'hr', 'hr_contract', 'hr_payroll', 'report'],
    'data': [
        'views/contract_report.xml',
        'views/report_contract.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
