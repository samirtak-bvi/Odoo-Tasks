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
    salesperson_img=fields.Image(compute="_get_image", store=True, string="Image")

    @api.depends('salesperson_id')
    def _get_image(self):
        for rec in self:
            rec.salesperson_img = rec.salesperson_id.image_1920
    # @api.model
    # def create(self, vals_list):
    #     rec = super(PropertyOffer, self).create(vals_list)
    #     if rec.property_id.salesperson_id.id:
    #         rec.salesperson_id = rec.property_id.salesperson_id.id
        
    #     return rec

    @api.model
    def _send_mail_cron(self):
        print('saddfsadfsasa')
        self.create({'partner_id':14})

        recs = self.env['estate.property.offer'].search([('status', '=', 'accepted')])
        for rec in recs:
            template_id = rec.env.ref('estate.estate_mail_template').id
            rec.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)            
    
    def action_send_info(self):
        template_id = self.env.ref('estate.estate_mail_template').id
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)