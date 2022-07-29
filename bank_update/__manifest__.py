# -*- coding: utf-8 -*-
{
    'name': "Bank update",
    'summary':
        """
        Hace que la tranferencia internas pueda aceptar diarios de tipo cash. 
        Adem�s, genera el movimiento de entrada de forma autom�tica.
        """,
    'version': '14.0',
    'category': 'Extra Tools',
    'author': "PROINTEC",
    'website': "http://www.prointeccr.com",
    'license': 'AGPL-3',
    'depends': ['base', 'account', 'account_batch_payment'],
    'data': [
        'views/account_payment_views.xml',
        'views/account_batch_payment.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
