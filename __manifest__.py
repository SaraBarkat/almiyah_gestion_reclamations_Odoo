# -*- coding: utf-8 -*-
{
    'name': "Client SpecH",

    'summary': """Gestion Clients Grossiste""",

    'description': """
        Gestion client grossiste module pour :
            - Gerer client et commandes
            - Gerer assurances            
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing    
    'category': 'Test',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'views/clientspec.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
