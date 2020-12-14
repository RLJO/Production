# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    custom_mrp_checklist_status_ids = fields.One2many(
        'mrp.checklist.status', 
        'custom_mrp_id', 
        string='Mrp Checklist Status',
        copy=True
    )
    custom_mrp_instruction_ids = fields.Many2many(
        'mrp.instruction',
        string='Mrp Instructions ',
        copy=True
    )

    @api.model
    def create(self, values):
        res =  super(MrpProduction, self).create(values)
        product_id = res.product_id
        if product_id:
            res.write({
                'custom_mrp_instruction_ids': [(6,0,product_id.custom_instruction_ids.ids)],
            })
        for checklist in product_id.custom_checklist_ids:
            self.env['mrp.checklist.status'].create({
                'custom_mrp_id':res.id,
                'mrp_checklist_id':checklist.id,
                })
            
        return res

class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    workorder_checklist_status_ids = fields.One2many(
        'workorder.checklist.status', 
        'custom_workorder_id', 
        string='WorkOrder Checklist Status',
        copy=True
    )
    workorder_instruction_ids = fields.Many2many(
        'work.order.instruction',
        string='Mrp Instructions ',
        copy=True
    )
    @api.model
    def create(self, values):
        res =  super(MrpWorkorder, self).create(values)
        operation_id = res.operation_id
        if operation_id:
            res.write({
                'workorder_instruction_ids': [(6,0,operation_id.custom_workorder_instruction_ids.ids)],
            })
        for checklist in operation_id.custom_workorder_checklist_ids:
            self.env['workorder.checklist.status'].create({
                'custom_workorder_id':res.id,
                'workorder_checklist_id':checklist.id,
                })
            
        return res

class MrpRoutingWorkcenter(models.Model):
    _inherit = 'mrp.routing.workcenter'

    custom_workorder_instruction_ids = fields.Many2many(
        'work.order.instruction',
        string='Mrp Instructions ',
        copy=True
    )
    custom_workorder_checklist_ids = fields.Many2many(
        'work.order.checklist',
        string='Mrp Checklists',
        copy=True
    )
