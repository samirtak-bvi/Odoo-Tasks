from odoo import fields, models, api
from odoo.exceptions import ValidationError
from odoo import tools


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This will contain the type of the Estate Property!"

    name = fields.Char(required=True)
    new_field = fields.Char()
    property_name_ids = fields.One2many('estate.property', 'property_type_id')
    property_type_img = fields.Image()
           
    def name_get(self):
        print(self._context)
        arr = []

        if self._context.get('field'):
            for rec in self:
                arr.append((rec.id, rec.new_field))

        else:
            for rec in self:
                arr.append((rec.id, rec.name))

        return arr