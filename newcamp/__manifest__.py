# -*- coding: utf-8 -*-
{
    'name': "new_camp",

    'summary': """Campos inext""",

    'description': """
	Creacion de campos nuevos para modulo de empleados
    """,

    'author': 'E&G',

    'website': "3Mind",
    'category': 'hr',
    'version': '0.1',

    'depends': ['base', 'hr'],

    'data': [
	'view/Ver_Campos.xml',
#	'templates.xml',
    ],

    'demo':[
	'demo.xml',
    ],
    'auto_install': False,
    'installable': True,
}
