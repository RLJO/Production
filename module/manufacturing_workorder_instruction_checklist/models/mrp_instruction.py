# -*- coding: utf-8 -*

from odoo import models, fields, api

class MrpInstrtuction(models.Model):
    _name = 'mrp.instruction'
    
    name = fields.Char(
        string="Name",
        required=True
    )