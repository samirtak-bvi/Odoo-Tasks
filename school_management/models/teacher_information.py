from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TeacherInformation(models.Model):
    _name = 'teacher.information'
    _description = 'It will contain the basic information field of the Teachers.'

    name=fields.Char(required=True)
    std = fields.Many2one("school.standards")
    div = fields.Many2one("school.divisions", domain="[('std', '=', std)]")
    assigned_class=fields.Many2one("school.classname")
    
    @api.onchange('std', 'div')
    def _check_class(self):
        for rec in self:
            rec.assigned_class = self.env['school.classname'].search([("std", '=', rec.std.id), ("div", '=', rec.div.id)]).id

    @api.constrains('assigned_class')
    def _check_unique(self):
            
        for rec in self:
            # print(rec.assigned_class.std.std)
            rec.std = rec.assigned_class.std.id
            rec.div = rec.assigned_class.div.id
        # for rec in self:
        #     if rec.std and rec.div:
        #         search_res = self.env['school.classname'].search([("std", '=', rec.std.id), ("div", '=', rec.div.id)])
        #         if not(search_res.id):
                    
        #             new_record_vals = {
        #                 "std" : rec.std.id,
        #                 "div" : rec.div.id,
        #             }
        #             self.env['school.classname'].create(new_record_vals)
        #         print(rec.assigned_class)
        #         rec.assigned_class = search_res.id
            # print(rec.search_count([('assigned_class', '=', rec.assigned_class.id)]), 'asiudgsaiudg')
            if rec.search_count([('assigned_class', '=', rec.assigned_class.id)])>1:
                raise ValidationError("Cannot assign more than 1 teacher to same class.")
        # print(self.std.id, self.div.id)    
        # search_res = self.search([("std.id", '=', self.std.id), ("div.id", '=', self.div.id)])
        # print(search_res)

    # def write(self, vals):
    #     res = super(TeacherInformation, self).write(vals)

    #     new_record_vals = {
    #         "std" : self.std.id,
    #         "div" : self.div.id,
    #     }
    #     print(new_record_vals)
    #     search_res = self.env['school.classname'].search([("std.id", '=', new_record_vals["std"]), ("div.id", '=', new_record_vals["div"])], limit=1)
    #     if search_res:
    #         vals['assigned_class'] = search_res.id
    #     else:
    #         rec = self.env['school.classname'].create(new_record_vals)
    #         vals['assigned_class'] = rec.id
    
    #     return res
    