# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class pos_training(models.Model):
    _inherit=['pos.order']

    phoneNumber = fields.Char(string="Phone Number")
    
    # @api.constrains('phoneNumber')
    def search_phone(number):
        # for rec in self:
        #     record = self.search_count(
        #         [('phoneNumber', '=', rec.phoneNumber), ('id', '!=', rec.id)])
        #     if record > 0:
        #         raise ValidationError(
        #             "Number Already Exists!")
        return number    
    @api.model
    def _order_fields(self, ui_order):
        res = super(pos_training, self)._order_fields(ui_order)
        # print("raw res" ,res)
        res['phoneNumber'] = ui_order.get('phoneNumber') if ui_order.get('phoneNumber') else False
        # print("updated res" ,res)
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