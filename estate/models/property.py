from odoo import fields, models, api
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz
from odoo.exceptions import ValidationError


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is the description of test model!"
    _inherit = ['mail.activity.mixin',
                ]

    handle = fields.Integer()
    name = fields.Char("Title", help="Enter the name", required=True)
    description = fields.Char(translate=True)
    postcode = fields.Char("Postcode")
    date_availabilty = fields.Date(
        "Available From", copy=False, default=lambda self: fields.Date.context_today(self))
    month_availabilty = fields.Char(compute="_calc_month", store=True)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", copy=False)
    bedrooms = fields.Integer("Bedrooms", default=2)
    facades = fields.Integer()
    garage = fields.Boolean(default=1, readonly=True)
    garden = fields.Boolean()
    garden_orientation = fields.Selection(default='north', selection=[(
        'north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    active = fields.Boolean(required=True, default=True)
    state = fields.Selection(selection=[('new', 'New'), ('order recieved', 'Order Recieved'), (
        'offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], default='new', copy=False)
    property_type_id = fields.Many2one(
        "estate.property.type", string="Property Type")
    new_id = fields.Many2one("estate.property.type")
    partner_id = fields.Many2one("res.partner", string="Partner")
    buyer_id = fields.Many2one("res.users", copy=False)
    salesperson_id = fields.Many2one(
        "res.users", default=lambda self: self.env.user)
    property_info_id = fields.Many2many("estate.property.info", context={'from_python': True})
    offer_id = fields.One2many(
        "estate.property.offer", "property_id", string="Property Offer")
    living_area = fields.Integer("Living Area (sqm.)", default=1)
    garden_area = fields.Integer()
    total_area = fields.Integer(compute="_total_area")
    best_price = fields.Char(compute="_best_price")
    new_field = fields.Char(readonly=True)
    total_properties = fields.Char(
        "Total Properties Type", compute="_total_proprties")
    user = fields.Char()
    price = fields.Monetary(string='Price', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency')
    a = fields.Integer()
    b = fields.Integer()
    c = fields.Char(compute='some', depends=['a', 'b'])
    state = fields.Selection(
        selection=[('draft', 'default'), ('posted', 'success')])
    sale = fields.Many2one('sale.order')
    check_box_value = fields.Integer(
        store=True, compute='_get_ratings', string="Progress")
    ratings = fields.Selection(readonly=True, selection=[(
        '0', 'None'), ('1', 'Very Low'), ('2', 'Low'), ('3', 'Medium'), ('4', 'High'), ('5', 'Very High')])
    checkfield = fields.Many2many('progress.check', context={'text': True}, required=False)
    property_context = fields.Many2one('properties.context', 'properties')
    duplicate_buyer_count = fields.Integer(compute='_calc_duplicate_buyer')
    manager_name = fields.Many2one('res.partner',string='Manager Name')


    @api.onchange('checkfield')
    def _get_check(self):
        print(self._context)

    def _calc_duplicate_buyer(self):
        for rec in self:
            if rec.buyer_id:
                rec.duplicate_buyer_count = self.search_count([('buyer_id', '=', rec.buyer_id.id)]) 
            else:
                rec.duplicate_buyer_count = 0


    def action_show_potential_duplicates(self):
        return {
            'name' : self.buyer_id.name,
            'type' : 'ir.actions.act_window',
            'view_mode' : 'tree',
            'res_model': 'estate.property',
            'domain' : [('buyer_id', '=', self.buyer_id.id)]
        }

    @api.model
    def default_get(self, fields):
        print(self._context, 'qwertyuiosdfgh')
        return super(EstateProperty, self).default_get(fields)

    @api.onchange('property_info_id')
    def on_change_info(self):
        print(self._context)
    def action_change(self):
        print(self.env['estate.property'].search([]))
        print(self.with_context(mail_notify_force_send=True))
        print(self._context)

        self._context.update({'mail_notify_force_send' : True})
        print(type(self._context))
        print(self._context)
        

    def cancel_property_context(self):
        print(self._context)
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "estate.property.cancel",
            "target": "new",
            "context": {"default_property_id": self.id}
        }

    @api.model
    def name_search(self, name='', args=None, operator='=', limit=100):
        domain = args
        if self._context.get('get_properties'):
            domain+=[('salesperson_id', '=', self._context.get('uid'))]
        return super(EstateProperty, self).search(domain, limit=limit).name_get()

    @api.depends('checkfield')
    def _get_ratings(self):

        for rec in self:
            total = self.env['progress.check'].search_count([])
            checked = len(rec.checkfield)
            rec.check_box_value = (checked/total)*100

            if rec.check_box_value == 0:
                rec.ratings = '0'
            elif rec.check_box_value <= 20:
                rec.ratings = '1'
            elif rec.check_box_value > 20 and rec.check_box_value <= 40:
                rec.ratings = '2'
            elif rec.check_box_value > 40 and rec.check_box_value <= 60:
                rec.ratings = '3'
            elif rec.check_box_value > 60 and rec.check_box_value <= 80:
                rec.ratings = '4'
            else:
                rec.ratings = '5'

    def some(self):
        for rec in self:
            rec.c = str(rec.a+rec.b)

    # total_properties_owned = fields.Char("Total Properties Owned")

    def _calc_month(self):
        for rec in self:
            rec.month_availabilty = rec.date_availabilty.strftime("%B")

    # @api.onchange("property_type_id")
    # def _total_properties_owned(self):
    #     for sales in self:
    #         sales.total_properties_owned = sales.browse(sales.property_type_id)

    @api.depends("property_type_id")
    def _total_proprties(self):
        domain = [('property_type_id', '=', self.property_type_id.id)]
        record_count = self.search_count(domain)
        self.total_properties = record_count

    @api.depends("garden_area", "living_area")
    def _total_area(self):

        for area in self:
            area.total_area = area.garden_area + area.living_area

    @api.depends("offer_id")
    def _best_price(self):
        temp = 0
        for price in self.offer_id:
            if temp < price.price:
                temp = price.price

        for best_price in self:
            best_price.best_price = temp

    # def unlink(self):
    #     for record in self:
    #         if record.active != False:
    #             raise ValidationError("Cannot Delete")
    #     return super(EstateProperty, self).unlink()

    def write(self, values):

        # if 'garden' in values and values['garden'] == True:
        #     raise ValidationError("No Garden!")
        # if 'property_type_id' in values:
        #     property_types = self.property_type_id.browse(
        #         values['property_type_id'])
        #     print(property_types)
        #     for property_type in property_types:
        #         if property_type.name == 'House':
        #             self.postcode = '38000'
        ids = []
        for id in self:
            ids.append(id.id)
        print(ids)
        print(self.browse([107,115]), 'sadghiug')
    
        print(values, 'Write Values()')
        response = super(EstateProperty, self).write(values)

        # rec = self.env['progress.check'].with_context(test="Has TV").create({'name': 'Has Nothing'})
        # print(rec, 'asidgsa')
        # print(self)

        return response

    def copy(self, default=None):
        if default is None:
            default = {}

        default.update({
            'name': self.name[:-3] + " " + str(self.id+1)
        })
        print(self.search_read([], ['name']))

        return super(EstateProperty, self).copy(default)

    # def search(self, domain, offset=0, limit=None, order=None, count=False):
    #     args = [('garden', '=', True)]
    #     # domain += args
    #     return super(EstateProperty, self).search(domain, offset=0, limit=None, order='name ASC', count=False)

    # def browse(self, ids=None):

    #     records =  super(EstateProperty, self).browse(ids)

    #     print(records)
    #     # for rec in records:
    #     #     rec.name = rec.name.upper()

    #     return records

    # def read_group(self, domain, fields, groupby," options="{'color_field': 'color', 'no_create_edit': T offset=0, limit=None, orderby=False, lazy=True):
    #     # domain = [('bedrooms', '=', 2)]
    #     fields = ['date_availabilty']
    #     groupby = ['day']
    #     return super(EstateProperty, self).read_group(domain, fields, groupby, offset, limit, orderby, lazy)


class NewSaleFields(models.Model):
    _inherit = ['sale.order']

    new_field = fields.One2many('estate.property', 'sale')


class PropertyCancel(models.TransientModel):
    _name = "estate.property.cancel"
    _description = "A Cancel Wizard Model"

    property_id = fields.Many2one("estate.property", string="Browse Property")

    def delete_property(self):
        for rec in self:
            if self._context.get('active_id'):
                pass

            if self._context.get('active_model'):
                id = rec.property_id.id
                print(id, 'asidusgadig')
                print(rec._context, 'This is it!')
                property = self.env['estate.property'].browse(id)
                property.unlink()

                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'type': 'success',
                        'message': ("Successfully deleted."),
                        'next': {'type': 'ir.actions.act_window_close',
                                 },
                    }
                }
            else:
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'type': 'success',
                        'message': ("You can not delete the property."),
                        'next': {'type': 'ir.actions.act_window_close'},
                    }
                }


class ProgressCheck(models.TransientModel):
    _name = 'progress.check'
    _description = 'A Progress Checkbox'

    name = fields.Char()

    # @api.model
    # def create(self, vals):
    #     rec = super(ProgressCheck, self).create(vals)
    #     properties = self.env['estate.property'].search([])
    #     for property in properties:
    #         property._get_ratings()
    #     return rec

    def unlink(self):
        rec = super(ProgressCheck, self).unlink()
        print(self._context)
        properties = self.env['estate.property'].search([])
        for property in properties:
            property._get_ratings()
        return rec


class PropertiesContext(models.Model):
    _name = 'properties.context'
    _description = 'This is a test for context in properties.'

    name = fields.Char(multi_company=True)
    properties = fields.One2many('estate.property', 'property_context')


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    manager_name = fields.Many2one('res.partner',string='Manager Name', config_parameter='estate.manager_name')
    abcd = fields.Boolean(string="Check")
    defg = fields.Boolean(string="Check")
    qwer = fields.Boolean(string="Check")
    asdf = fields.Boolean(string="Check")
    zxcv = fields.Boolean(string="Check")
    wert = fields.Boolean(string="Check")
    sdfg = fields.Boolean(string="Check")

    # def write(self, vals):
    #     print('abcd')
    #     res = super(ResConfigSettings, self).write(vals)
    #     return res
    
    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        print(res, 'asigsadihsduiauhi')
        # print(self.env.ref('estate.model_estate_property'))
        # res.update(
        #     manager_name = self.env.ref('estate.model_estate_property').manager_name,
        # )
        return res
    

# class PriceListWizard(models.TransientModel):
#     _name="price.list.wizard"
#     _description="Price List Wizard Description."

    # report_type = fields.Selection([()])