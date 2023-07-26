from odoo import fields, models


class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "This will contain the type of the Estate Property!"

    name = fields.Char(required=True)
    new_field = fields.Char()

    def name_get(self):
        print(self._context)
        arr = []
       
        if self._context.get('field'):
           for rec in self:
               arr.append((rec.id, rec.new_field))

        if self._context.get('property'):
            for rec in self:
                arr.append((rec.id, rec.name))

        return arr