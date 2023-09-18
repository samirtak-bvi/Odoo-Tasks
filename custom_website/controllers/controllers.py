# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, route


class OwlPlayground(http.Controller):
    @http.route(['/form'], type='http', auth='public', website=True)
    def sales_detail(self):
        return request.render('custom_website.custom_webpage')

    @http.route(['/register'], type='json', auth='public', methods=["POST"])
    def form_details(self, **kwargs):
        print(kwargs)
        print('asdashassaydasasiudasgidasgudgs', request.env.user.id)
        try:
            if (request.env.user.id==8):
                return {'msg': "Please login to send query!" ,'title': "Required", 'btn':True}
            
            request.env['customer.submission'].create(kwargs)
            return {'msg': 'Query Reported Successfully!', 'title': "Success", 'btn':False}
        except:
            return {'msg': 'Query Report was not able to submit...', 'title': "Unsuccessful :(", 'btn':False}