# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class pos_training(models.Model):
    _inherit=['pos.order']

    phoneNumber = fields.Char(string="Order Note")
    
    @api.model
    def _order_fields(self, ui_order):
        res = super(pos_training, self)._order_fields(ui_order)
        res['phoneNumber'] = ui_order.get('phoneNumber') if ui_order.get('phoneNumber') else False
        return res
    
    
class CustomerMobile(models.Model):
    _inherit = ['res.partner']

    mobile_no = fields.Char(string="Mobile Number")

class CustomerMobilePosSession(models.Model):
    _inherit=['pos.session']

    def _loader_params_res_partner(self):
        result= super()._loader_params_res_partner()
        result.get('search_params').get('fields').append('mobile_no')
        return result