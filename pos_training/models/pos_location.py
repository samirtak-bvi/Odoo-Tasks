from odoo import models, fields, api
from odoo.exceptions import ValidationError

class POSLocation(models.Model):
    _inherit = ['pos.config']
    location_ids = fields.Many2many('pos.available.location', string="Available Locations")

class POSLocation(models.TransientModel):
    _inherit = ['res.config.settings']
    pos_location_ids = fields.Many2many(related='pos_config_id.location_ids', string="Available Locations", readonly=False)

class AvailableLocations(models.Model):
    _name='pos.available.location'
    _description = 'Contains the available locations for the orders.'
    
    name = fields.Char(string='Location')

    @api.constrains('name')
    def _check_duplicate_location(self):
        for rec in self:
            if(self.search_count([('name', '=ilike', rec.name), ('id', '!=', rec.id)]) > 0):
                raise ValidationError('Location Already Exists')


class POSLocationSession(models.Model):
    _inherit = ['pos.session']

    @api.model
    def _pos_ui_models_to_load(self):
       models = super()._pos_ui_models_to_load()
       models.append('pos.available.location')
       return models
    
    def _loader_params_pos_available_location(self):
        return{
            'search_params':{
                'fields' : ['name']
            }
        }

    def _get_pos_ui_pos_available_location(self, params):
        print(params)
        return [self.env['pos.available.location'].search_read(**params['search_params'])][0]
    
class POSLocationOrder(models.Model):
    _inherit=['pos.order']

    location = fields.Many2one('pos.available.location', string="Order Location")
    
    @api.model
    def _order_fields(self, ui_order):
        res = super(POSLocationOrder, self)._order_fields(ui_order)
        res['location'] = ui_order.get('location').get('id') if ui_order.get('location') else False
        return res
    
    