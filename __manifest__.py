# -*- coding: utf-8 -*-
{
    'name': "Meetlily REST API",

    'summary': """
        Meetlily REST API is tool to enable connection using RESTful services""",

    'description': """
        Meetlily REST API is tool to enable connection using RESTful services
    """,

    'author': "Eddie Villanueva",
    'website': "http://www.meetlily.net",
    'category': 'developers',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    "application": True,
    "installable": True,
    "auto_install": False,

    'external_dependencies': {
        'python': ['pypeg2', 'requests']
    }
}