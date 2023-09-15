# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
    _name = 'employee.detail'
    _description = 'Contains Employee Details'

    name = fields.Char()
    employee_id = fields.Char()
    occupation = fields.Selection(selection=[('',''), ('business', 'Business'), ('job', 'Job')])
    salary_pm = fields.Integer(store=True)
    salary_annual = fields.Integer(store=True, compute='_compute_annual', inverse='_compute_pm')
    image = fields.Image()

    @api.depends('salary_pm')
    def _compute_annual(self):
        for rec in self:
            rec.salary_annual = rec.salary_pm * 12
    
    def _compute_pm(self):
        for rec in self:
            rec.salary_pm = rec.salary_annual / 12
