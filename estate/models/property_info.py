from odoo import fields, models
from random import randint

class EstatePropertyInfo(models.Model):
    _name = "estate.property.info"
    _description = "This will contain the type of the Estate Property Info!"

    def _get_default_color(self):
            return randint(1, 11)
    
    name = fields.Char(required=True)
    color = fields.Integer('Color', default=_get_default_color)