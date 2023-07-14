from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
import phonenumbers
from ....addons.sale.models.account_move_line import AccountMoveLine


class StudentInformation(models.Model):
    _name = 'student.information'
    _description = 'It will contain the basic information field of the student'
    _inherit = "mail.thread"

    name = fields.Char(required=True)
    standard = fields.Many2one("school.standards")
    division = fields.Many2one("school.divisions")
    roll_number = fields.Integer()
    enroll_number = fields.Char(readonly=True)
    country_name = fields.Many2one("res.country")
    address = fields.Text(compute="_get_address")
    phone_number = fields.Char(copy=False, tracking=True, default="")
    dob = fields.Date(required=True)
    age = fields.Integer(store=True, compute="_calc_age")
    parent_ids = fields.Many2many("parent.information")
    school_ids = fields.Many2many("school.information")
    class_name = fields.Many2one("school.classname", required=True)
    assigned_teacher = fields.Many2one("teacher.information")
    address_line_1 = fields.Char()
    address_line_2 = fields.Char()
    zip_code = fields.Char()
    state = fields.Many2one("res.country.state",
                            domain="[('country_id', '=', country_name)]")
    birth_month = fields.Char()
    is_good = fields.Boolean(string="Check Box", default=True)
    # reference_no = fields.Char(string="Enrollment Number")

    @api.model
    def create(self, vals_list):
        pass
    

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id , rec.name.upper()))
        return res



    @api.depends('address_line_1', 'address_line_2', 'zip_code', 'state', 'country_name')
    def _get_address(self):
        for rec in self:
            if rec.address_line_1 and rec.address_line_2 and rec.zip_code and rec.state and rec.country_name:
                rec.address = f'''{rec.address_line_1},
{rec.address_line_2},
{rec.country_name.name},
{rec.state.name} - {rec.zip_code}'''
            else:
                rec.address = ''

    @api.onchange('country_name')
    def _country_code(self):
        for rec in self:
            code = phonenumbers.country_code_for_region(rec.country_name.code)

            if rec.phone_number != "":
                rec.phone_number = ""
            if code:
                rec.phone_number += str("+") + str(code)

    @api.onchange("standard", "division")
    def _class_teacher(self):
        for rec in self:
            if rec.standard.std and rec.division.div:
                rec.assigned_teacher = self.env['teacher.information'].search(
                    [('std', '=', self.standard.id), ('div', '=', self.division.id)]).id

                rec.class_name = self.env['school.classname'].search(
                    [('std', '=', self.standard.id), ('div', '=', self.division.id)]).id
                print(rec.class_name)

    @api.onchange('class_name')
    def _check_std_div(self):
        for rec in self:
            if rec.class_name:
                print(rec.class_name)
                rec.standard = rec.class_name.std
                rec.division = rec.class_name.div

    @api.onchange("assigned_teacher")
    def _std_div(self):
        for rec in self:
            if rec.assigned_teacher:
                search_teacher = self.env['teacher.information'].search(
                    [('id', '=', rec.assigned_teacher.id)])
                rec.standard = search_teacher.std
                rec.division = search_teacher.div
                rec.class_name = self.env['school.classname'].search(
                    [('std', '=', search_teacher.std.id), ('div', '=', search_teacher.div.id)]).id

    @api.constrains("phone_number")
    def _check_number(self):
        # country_regex = '^[+][9][1]'
        for rec in self:
            # if (len(rec.phone_number) != 10):
            #     raise ValidationError("Enter Correct Phone Number")
            try:
                parsed_number = phonenumbers.parse(rec.phone_number, None)
                expected_country = str(
                    phonenumbers.country_code_for_region(rec.country_name.code))
                is_valid = phonenumbers.is_valid_number(parsed_number)
                actual_country = str(parsed_number.country_code)

                print(is_valid, actual_country, expected_country)

                if not (is_valid):
                    if not (actual_country == expected_country):
                        raise ValidationError("Country Code has been altered!")
                    raise ValidationError("Number is wrong!")

            except phonenumbers.phonenumberutil.NumberParseException:
                raise ValidationError("Enter Phone Number!")

    @api.constrains('phone_number')
    def check_phone_number(self):
        for rec in self:
            record = self.search_count(
                [('phone_number', '=', rec.phone_number), ('id', '!=', rec.id)])
            if record > 0:
                raise ValidationError(
                    "Another student has the same phone number!")
        #     if record>0:
        # self.env.user.notify_warning(
        #             title='Warning',
        #             message='Another student has the same phone number!'
        #         )

    @api.depends("dob")
    def _calc_age(self):
        for rec in self:
            if rec.dob:

                age = relativedelta(datetime.now(), rec.dob).years

                if age > 4:
                    rec.age = age
                    rec.birth_month = rec.dob.strftime("%B")
                else:
                    raise ValidationError("Age cannot be less than 4")

                # if rec.standard:
                #     if not(age-6<=int(rec.class_name.std.std) and age-4>=int(rec.class_name.std.std)):
                #         raise ValidationError("Check Age! It does not match with the Standard")

    @api.model_create_multi
    def create(self, vals):
        # record = super(StudentInformation, self).create(vals_list=vals)

        # for rec in record:
        #     print(rec.id)
        #     rec.enroll_number = "ENR00" + str(rec.id)
        
        for val in vals:
            val['enroll_number'] = self.env['ir.sequence'].next_by_code('school.enrollment.sequence')
        res = super(StudentInformation, self).create(vals)
        return res

        # return record

    def test_button_2(self):
        return {
            "type": "ir.actions.act_url",
            "url": "https://google.com",
            "target": "self",
        }

    def action_done(self):
        for rec in self:
            if rec.is_good == False:
                rec.is_good = True
        self.env.context['lsadf'] = 'sdaug'
        print(self.env.context)
        print(type(self.env.context))
        # print(['view_type'])
        # self.env.context['params']['view_type'] = 'tree'
        # print(self.env.context)     
        # new = self.with_context(name='assigned_teacher')
        # self._fields['display_name'] = 'siadgsiaudgsuia'
        # print(self.env.context)
        # print(self._fields)    

        # for rec in self:
        #     print(rec._fields)    

    def write(self, vals):
        print('iasdgdsuiag')
        return super(StudentInformation,self.with_context(mail_notify_force_send=True)).write(vals)



    def test_button(self):
         action = {
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "res_model": "teacher.information",
                "res_id" : self.assigned_teacher.id,
                "target" : "new",

                    }
         return action
    
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):

        args = args or []
        recs = self.browse()
        if name:
            recs = self.search((args + [('name', operator, name), ('enroll_number', operator, name)]),
                               limit=limit)
        if not recs:
            recs = self.search([('name', operator, name)] + args, limit=limit)
        return recs.name_get()
    
    # @api.model
    # def create(self, vals):
    #     # vals
    #     return super(StudentInformation, self.with_context(name='qwetrt')).create(vals)

    # class NewClass(AccountMoveLine):
    
        
class Test(models.Model):
    _name = 'test.model'
    _description = 'siaudbgsuiadh'
    _inherit = 'student.information'

