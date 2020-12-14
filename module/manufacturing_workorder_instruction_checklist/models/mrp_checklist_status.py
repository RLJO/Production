# -*- coding: utf-8 -*

from odoo import models, fields, api

class MrpChecklistStatus(models.Model):
    _name = 'mrp.checklist.status'
    
    mrp_checklist_id = fields.Many2one(
        'mrp.checklist', 
        string='Checklist Name',
        copy=True,
        required=True
    )
    state = fields.Selection([
        ('pass', 'Pass'),
        ('fail', 'Fail'),
        ('draft','Draft')
     ], 
        string="Status",
        default='draft',
        copy=False,
        required=True
    )
    custom_mrp_id = fields.Many2one(
        'mrp.production', 
        string='Manufacturing Order',
        copy=False
    )
    comment = fields.Char(
        string="Comment",
        required=False,
        copy=False
    )

    def custom_action_reset_draft(self):
        for rec in self:
            rec.state = 'draft'

    def custom_action_pass(self):
        for rec in self:
            rec.state = 'pass'

    def custom_action_fail(self):
        for rec in self:
            rec.state = 'fail'