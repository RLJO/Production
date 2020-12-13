# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import date


class MergeMRP(models.TransientModel):
    _name = "merge.mrp"
    _description = "Merge  Manufacturing Order"
    
    name = fields.Char('Name')
    
    
    def merge_mrp(self):
        active_ids = self._context.get('active_ids')
        if len(active_ids) <= 1:
            raise ValidationError(_('You must select more then one Manufacturing Order'))
        mrp_ids = self.env['mrp.production'].browse(active_ids)
        mrp_id = mrp_ids[0]
        product_id = mrp_id.product_id.id
        bom_id = mrp_id.bom_id.id
        qty = 0.0
        origin = ''
        for mrp in mrp_ids:
            qty += mrp.product_qty
            if mrp.state not in ['draft','confirmed']:
                raise ValidationError(_('Manufacturing Order must in draft or confirmed state'))
            if mrp.product_id.id != product_id:
                raise ValidationError(_('Manufacturing Order must be same product'))
            if mrp.bom_id.id != bom_id:
                raise ValidationError(_('Manufacturing Order must be same BOM'))
            
            if origin:
                origin = origin +' ,'+ mrp.name
            else:
                origin = mrp.name
        
        new_id = mrp_id.copy()
        update_id = self.env['change.production.qty'].with_context(active_id=new_id.id).create({'product_qty':qty})
        update_id.change_prod_qty()
        new_id.origin = origin
        for mrp in mrp_ids:
            mrp.button_unreserve()
            mrp.action_cancel()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
