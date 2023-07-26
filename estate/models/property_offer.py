from odoo import fields, models, api

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This will contain the offers of the Property!"
    _rec_name = "partner_id"
    
    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one("res.partner", required="True")
    property_id = fields.Many2one("estate.property")
    salesperson_id = fields.Many2one("res.users", string="Partner")

    # @api.model
    # def create(self, vals_list):
    #     rec = super(PropertyOffer, self).create(vals_list)
    #     if rec.property_id.salesperson_id.id:
    #         rec.salesperson_id = rec.property_id.salesperson_id.id
        
    #     return rec
    