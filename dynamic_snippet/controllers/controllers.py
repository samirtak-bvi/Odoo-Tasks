# -*- coding: utf-8 -*-
# from odoo import http


# class DynamicSnippet(http.Controller):
#     @http.route('/dynamic_snippet/dynamic_snippet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dynamic_snippet/dynamic_snippet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dynamic_snippet.listing', {
#             'root': '/dynamic_snippet/dynamic_snippet',
#             'objects': http.request.env['dynamic_snippet.dynamic_snippet'].search([]),
#         })

#     @http.route('/dynamic_snippet/dynamic_snippet/objects/<model("dynamic_snippet.dynamic_snippet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dynamic_snippet.object', {
#             'object': obj
#         })
