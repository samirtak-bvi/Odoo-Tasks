from odoo import models, fields, api

class POSQuantitySession(models.Model):
    _inherit = ['pos.session']

    def _loader_params_product_product(self):
        result= super()._loader_params_product_product()
        result.get('search_params').get('fields').append('qty_available')
        return result