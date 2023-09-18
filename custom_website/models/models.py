# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SubmissionData(models.Model):
    _name = 'customer.submission'
    _description = 'Saves Costumer Query Records'

    name = fields.Char()
    job = fields.Char()
    query = fields.Text()

    