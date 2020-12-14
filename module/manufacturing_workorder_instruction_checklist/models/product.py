# -*- coding: utf-8 -*-

from odoo import models, fields


class Product(models.Model):
    _inherit = 'product.product'

    custom_instruction_ids = fields.Many2many(
        'mrp.instruction',
        string='Mrp Instructions ',
        copy=True
    )
    custom_checklist_ids = fields.Many2many(
        'mrp.checklist',
        string='Mrp Checklists',
        copy=True
    )
