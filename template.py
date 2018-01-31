# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2018 EDISON GARCIA.


######################################################################

from openerp.osv import fields, osv , orm
from openerp.tools.translate import _


class template_modelo(osv.osv):
	_name = 'template.modelo'
	_description = 'Formulario de Ejemplo'
	_columns = {
	     # Campo oblidatorio para buscar , readonly = True
	   'empresa' : fields.char('Empresa' , size=256, required=True, help='Este es el nombre'),
       'direccion' : fields.char('Dirección' , size=256, required=True, help='Este es el nombre'),
       'web' : fields.char('Web' , size=256, required=True, help='Este es el nombre'),
       
       }
	_defaults = {
       'state' : 'draft',
       'active' : 'true',
	}


template_modelo()