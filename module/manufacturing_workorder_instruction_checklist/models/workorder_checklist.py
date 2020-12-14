# -*- coding: utf-8 -*

from odoo import models, fields, api

class WorkOrderChecklist(models.Model):
    _name = 'work.order.checklist'
    
    name = fields.Char(
        string="Name",
        required=True
    )