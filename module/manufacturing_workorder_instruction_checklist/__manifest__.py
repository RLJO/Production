# -*- coding: utf-8 -*-
# Part of Probuse Consulting Service Pvt. Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': "Manufacturing and Workorders with Instructions and Checklists",
    'version': '3.1.1',
    'category': 'Manufacturing/Manufacturing',
    'license': 'Other proprietary',
    'price': 50.0,
    'currency': 'EUR',
    'summary':  """Instructions and Checklists for Manufacturing and Workorders """,
    'description': """
Manufacturing and Workorders with Instructions and Checklists
mrp
    """,
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'www.probuse.com',
    'support': 'contact@probuse.com',
   'images': ['static/description/image.jpg'],
    'live_test_url': 'https://youtu.be/32g8wEA6uSw',
    'depends': [
        'mrp',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/mrp_instruction_view.xml',
        'views/mrp_checklist_view.xml',
        'views/product_product_view.xml',
        'views/mrp_production_view.xml',
        'views/work_order_instruction_view.xml',
        'views/workorder_checklist_view.xml',
    ],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
