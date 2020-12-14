# -*- coding: utf-8 -*

from odoo import models, fields, api

class WorkOrderInstruction(models.Model):
    _name = 'work.order.instruction'
    
    name = fields.Char(
        string="Name",
        required=True
    )