# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class EmployeesDetail(http.Controller):
    @http.route('/employee/detail',type="json", method=["POST"], auth='public')
    def index(self, **kw):
        details = request.env['employee.detail'].search_read([])
        # print(details)
        return details