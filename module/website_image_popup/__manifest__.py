# -*- coding: utf-8 -*-
###############################################################################
#
#   website_image_popup for Odoo
#   Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
#   Copyright (C) 2016-today Geminate Consultancy Services (<http://geminatecs.com>).
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Website Image Popup',
    'category': 'Website',
    'version': '14.1.1.0',
    'author': 'Geminate Consultancy Services',
    'website': 'www.geminatecs.com',
    'license': 'Other proprietary',
    'summary': 'Website Image Popup',
    'description': """

This module will introduce a new option of 'Popup' and 'Reset Popup' on 'Image' Control Customization tozoom add magnific popup effect.

""",
    'depends': ['website'],
    'data': [
        'views/template.xml',
    ],
    'images': [],
    "price": 9.99,
    "currency": 'EUR',
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
