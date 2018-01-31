# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2018 EDISON GARCIA.

######################################################################

{
    'name': 'Módulo de Compañia',
    'version': '1.0',
    'author': 'Edison Garcia',
    'category': 'Nueva',
    'summary': 'Ejemplo módulo de compañia',
    'description': """

======================


    """,
    'license' : 'AGPL-3',
    'depends': ['sale'],
    'update_xml': [
        'template_view.xml',
    ],
    'installable': True,
    'active': False,
}