from odoo import http
from odoo.http import request, route
from odoo.addons.website_sale.controllers.main import WebsiteSale

class OwlPlayground(http.Controller):
    @http.route(['/sales_detail'], type='http', auth='public', website=True)
    def sales_detail(self):
        sale_details = request.env['sale.order'].sudo().search([])
        return request.render('owl_playground.sales_detail', {'details': sale_details})

class WebsiteSaleInherit(WebsiteSale):
    @http.route()
    def cart(self, **post):
        res_super = super(WebsiteSaleInherit, self).cart(**post)
        # return "UNDER WORK"
        print(res_super)
        return res_super

class Sales(http.Controller):
   @http.route(['/total_product_sold'], 
                auth="public")
   def sold_total(self):
        sale_obj = request.env['sale.order'].sudo().search([
            ('state', 'in', ['done', 'sale']),
        ])
        print(sale_obj)
        vals = {}
        for i in sale_obj:
           vals[i.name] = [i.name, i.state]
        print(vals, '=======================')
        # total_sold = sum(sale_obj.mapped('order_line.product_uom_qty'))
        # return total_sold
        return request.render('owl_playground.basic_snippet', {'orders': vals})
