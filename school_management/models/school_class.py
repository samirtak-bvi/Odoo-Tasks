from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Standard(models.Model):
    _name="school.standards"
    _description="School Standards"
    _rec_name = 'std'

    std = fields.Char()
    div = fields.Many2many('school.divisions')
    students = fields.One2many('student.information', 'standard')

    @api.constrains('std', 'div')
    def new_class(self):
        for rec in self:
            for ids in rec.div:
                exists = self.env['school.classname'].search_count([('std', '=', rec.id), ('div', '=', ids.id)])
                if not(exists):
                    print(rec.id, ids)
                    self.env['school.classname'].create({'std':rec.id, 'div':ids.id})

        for rec in self:
            if self.search_count([('std', '=', rec.std)])>1:
                raise ValidationError("Standard Exists!")

class Division(models.Model):
    _name="school.divisions"
    _description="School Divisions"
    _rec_name="div"

    div = fields.Char()
    std = fields.Many2many('school.standards')


    @api.constrains('std', 'div')
    def new_class(self):
        for rec in self:
            for ids in rec.std:
                exists = self.env['school.classname'].search_count([('div', '=', rec.id), ('std', '=', ids.id)])
                if not(exists):
                    print(rec.id, ids)
                    self.env['school.classname'].create({'div':rec.id, 'std':ids.id})
        
        for rec in self:
            if self.search_count([('div', '=', rec.div)])>1:
                raise ValidationError("Division Exists!")

    # def unlink(self):
    #     for rec in self:
            


class ClassName(models.Model):
    _name="school.classname"
    _description="Gets created when student selects from dropdown."
    _rec_name = "classname"

    std = fields.Many2one("school.standards")
    div = fields.Many2one("school.divisions")
    classname = fields.Char(store=True, compute='_combined_name')
    students = fields.One2many("student.information", "class_name")
    assigned_teacher = fields.One2many("teacher.information", "assigned_class", readonly=True)

    @api.depends('std', 'div')
    def _combined_name(self):
        for rec in self:
            try:
                rec.classname = str(rec.std.std) + " " + str(rec.div.div)
            except TypeError:
                rec.classname = "New"


    # @api.constrains('classname')
    # def _check_class(self):
    #     for rec in self:
    #         if self.search_count([('classname', '=', rec.classname)]) > 1:
    #             raise ValidationError("Class Exists")            
    #         print(self.env['school.standards'].search([('std', '=', rec.std.id)]))
            
    #         divisions = self.env['school.standards'].search([('std', '=', rec.std.id)])

    #         rec.std.div = [divisions.id]
            
            # rec.div.std = self.env['school.divisions'].search([('div', '=', rec.div.id)]).id

    # @api.constrains('classname')
    # def _add_class(self):
    #     for rec in self:
    #         print(self.env['school.divisions'].search([('std', '=', rec.std.id)]))
    #         rec.std.div = self.env['school.divisions'].search([('std', '=', rec.std.id)]).id
    #         rec.div.std = self.env['school.standards'].search([('div', '=', rec.div.id)]).id

