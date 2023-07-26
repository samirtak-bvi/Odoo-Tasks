from odoo import models, fields, api

class CancelWizard(models.TransientModel):
    _name='cancel.wizard'
    _description = "A Cancel Wizard!"
    _rec_name = 'partner_id'
    _transient_max_hours= 0.003

    partner_id = fields.Many2one('res.partner', string='Name', required=True)
    