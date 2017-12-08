# -*- coding: utf-8 -*-
{
    'name': "Employee Indefined Contracts Report",
    'description': """This Module Gives PDF Report of Indefined Contract Form.""",
    'description': """This Module Gives PDF Report of Indefined Contract Form.""",
    "category": "Generic Modules/Human Resources",
    'version': '0.1',
    'author': "E&G TechSystem",
    'company': "E&G TechSystem",
    'website': "http://www.hola.com",
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
