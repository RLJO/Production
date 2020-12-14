# -*- coding: utf-8 -*

from odoo import models, fields, api

class MrpChecklist(models.Model):
    _name = 'mrp.checklist'
    
    name = fields.Char(
        string="Name",
        required=True
    )