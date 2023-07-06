from odoo import models, fields, api


class ParentInformation(models.Model):
    _name = 'parent.information'
    _description = 'It will contain the relation of the parent with the student.'

    name = fields.Char(required=True)
    relation = fields.Selection([('father', 'Father'), ('mother', 'Mother'), ('guardian', 'Guardian')])
    phone_number = fields.Integer(default="+91", required=True)
    email = fields.Char()
    child_ids = fields.Many2many("student.information")
    # total_child = fields.Integer(compute="_total_child")

    # @api.depends('child')
    # def total_child(self):
    #     self.search_count([('child_ids', '=', )])



