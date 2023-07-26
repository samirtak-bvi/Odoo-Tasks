from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class SchoolInformation(models.Model):
    _name = 'school.information'
    # _inherit = "sale.order"
    _description = 'It will contain the basic information field of the Previous School.'

    name=fields.Char(required=True)
    enroll_number = fields.Char()
    admission_date = fields.Date(required=True)
    leaving_date = fields.Date(required=True)
    student_ids = fields.Many2many("student.information")

    @api.onchange("admission_date")
    def check_date(self):
        for rec in self:
            if relativedelta(rec.leaving_date, rec.admission_date).days < 0:
                raise ValidationError("Leaving Date Cannot be before Admission date!")


    def cancel_wizard_button(self):
        print(self._context)
        res = self.with_context({'enroll_number':'qwerty'})
        print(self._context)
        return {
            "type" : "ir.actions.act_window",
            "view_mode" : "form",
            "res_model" : "cancel.wizard",
            "target" : "new",
        }
    
    def testing(self):
        return True